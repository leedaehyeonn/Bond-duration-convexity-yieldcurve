import requests
import json
import pandas as pd
from datetime import datetime as dt
from tqdm import tqdm
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

API_KEY = ''
"시장금리 일별: 817Y002[D], 시장금리(월,분기,년): 721Y001[A,M,Q]"

# url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + API_KEY + '/json/kr/1/100/817Y002/D/20221201/20221217'
# response = requests.get(url)
# result = response.json()
# list_total_count=(int)(result['StatisticSearch']['list_total_count'])
# list_count=(int)(list_total_count/100) + 1

# rows=[]
# for i in range(list_count):
#     start = str(i * 100 + 1)
#     end = str((i + 1) * 100)
#     url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + API_KEY + '/json/kr/' + start + '/' + end + '/817Y002/D/20221201/20221217'
#     response = requests.get(url)
#     result = response.json()
#     rows = rows + result['StatisticSearch']['row']
    
# df=pd.DataFrame(rows)
# df2 = df.groupby('ITEM_CODE1')[['ITEM_CODE1','ITEM_NAME1']].first()
# df2

def get_daily_yield(ITEM_CODE1, fromdate, todate):

    url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + API_KEY \
            + '/json/kr/1/100/817Y002/D/'+ fromdate +'/'+ todate + '/' + ITEM_CODE1
    response = requests.get(url).json()
    list_total_count=(int)(response['StatisticSearch']['list_total_count'])
    list_count=(int)(list_total_count/100) + 1

    temp = []
    for i in tqdm(range(0,list_count)):
        start = str(i * 100 + 1)
        end = str((i + 1) * 100)

        url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + API_KEY + '/json/kr/' \
                + start + '/' + end + '/817Y002/D/' + fromdate + '/' + todate + '/' + ITEM_CODE1
        response = requests.get(url).json()
        temp += response['StatisticSearch']['row']

    df=pd.DataFrame(temp)
    df['Date']= pd.to_datetime(df['TIME'])
    df = df[['Date','DATA_VALUE']].set_index('Date').rename(columns={"DATA_VALUE":"Yield(%)"})
    df=df.astype('float')
    
    return df

def get_yield(ITEM_CODE1, fromdate, todate, freq = "A"):
    """시장금리(연, 월,분기): 721Y001[A,M,Q] 검색일자(주기에 맞는 형식으로 입력: 2021, 2021Q1, 202101, 20210101 등), dailybase와 통계코드, 아이템코드 둘다 다름"""

    url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + API_KEY \
            + '/json/kr/1/100/721Y001/'+ freq +'/'+ fromdate +'/'+ todate + '/' + ITEM_CODE1
    response = requests.get(url).json()
    response
    list_total_count=(int)(response['StatisticSearch']['list_total_count'])
    list_count=(int)(list_total_count/100) + 1

    temp = []
    for i in tqdm(range(0,list_count)):
        start = str(i * 100 + 1)
        end = str((i + 1) * 100)

        url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + API_KEY + '/json/kr/' \
                + start + '/' + end + '/721Y001/'+ freq +'/' + fromdate + '/' + todate + '/' + ITEM_CODE1
        response = requests.get(url).json()
        temp += response['StatisticSearch']['row']

    df=pd.DataFrame(temp)
    df['Date']= pd.to_datetime(df['TIME'],errors='ignore')
    df = df[['Date','DATA_VALUE']].set_index('Date').rename(columns={"DATA_VALUE":"Yield(%)"})
    df=df.astype('float')
    
    return df

# df1Y = get_yield('5030000', '202001', '202401', freq="M")..
fromdate = '20190101'
todate = '20240211'
df1Y = get_daily_yield('010190000', fromdate, todate)
df3Y = get_daily_yield('010200000', fromdate, todate)
df5Y = get_daily_yield('010200001', fromdate, todate)
df10Y = get_daily_yield('010210000', fromdate, todate)
df20Y = get_daily_yield('010220000', fromdate, todate)  


"""plot"""
fig = make_subplots(rows=3, cols=2, 
       subplot_titles=("1년", "3년", "5년", "10년","20년"))

fig.add_trace(
    go.Scatter(x=df1Y.index, y=df1Y['Yield(%)'], name="국채 1년"),
    row=1,col=1,
)
fig.add_trace(
    go.Scatter(x=df3Y.index, y=df3Y['Yield(%)'], name="국채 3년"),
    row=1,col=2,
)
fig.add_trace(
    go.Scatter(x=df5Y.index, y=df5Y['Yield(%)'], name="국채 5년"),
    row=2,col=1,
)
fig.add_trace(
    go.Scatter(x=df10Y.index, y=df10Y['Yield(%)'], name="국채 10년"),
    row=2,col=2,
)
fig.add_trace(
    go.Scatter(x=df20Y.index, y=df20Y['Yield(%)'], name="국채 20년"),
    row=3,col=1,
)

fig.update_layout(title_text='한국 장단기 국채', title_x=0.5)
fig.show()

fig = go.Figure()
fig.add_trace(
    go.Scatter(x=df1Y.index, y=df1Y['Yield(%)'], name="국채 1년"),
)
fig.add_trace(
    go.Scatter(x=df3Y.index, y=df3Y['Yield(%)'], name="국채 3년"),
)
fig.add_trace(
    go.Scatter(x=df5Y.index, y=df5Y['Yield(%)'], name="국채 5년"),
)
fig.add_trace(
    go.Scatter(x=df10Y.index, y=df10Y['Yield(%)'], name="국채 10년"),
)
fig.add_trace(
    go.Scatter(x=df20Y.index, y=df20Y['Yield(%)'], name="국채 20년"),
)

fig.update_layout(title_text='한국 장단기 국채', title_x=0.5)
fig.show()


df = pd.concat([df1Y,df3Y,df5Y,df10Y,df20Y],axis=1)
df.columns = ['국채1년','국채3년','국채5년','국채10년','국채20년']
df.loc[df.index.strftime('%y%d').isin(['1901','2001','2101','2201','2301'])]
# df1 = df.loc[df.index.strftime('%y%d').isin(['2201','2203'])]
# df1 = df.loc[df.index.year.isin([2023])]
df1 = df.loc[df.index.strftime('%Y%m%d').isin(['20190102','20200102','20210104','20220103','20230102','20240102'])]
df2 = df1.transpose()
fig=px.line(data_frame=df2,x=df2.index, y=list(df2.columns.strftime("%Y-%m-%d")),
           facet_col='variable',facet_col_wrap=4)
fig.update_layout(title_text='연도별 국채 장단기금리 수익률곡선',title_x=0.5)
fig.show()

df
