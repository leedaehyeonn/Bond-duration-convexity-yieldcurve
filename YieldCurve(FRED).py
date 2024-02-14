import pandas as pd
import fredpy as fp
from datetime import datetime as dt
from datetime import timedelta
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fp.api_key = 'ab5e65aae554e885f2fc033af16c9884'

startdate = "20190101"
enddate=(dt.now() + timedelta(days=-1)).strftime('%Y-%m-%d')
dgs2 = fp.series('DGS2', enddate)
dgs3 = fp.series('DGS3',enddate)
dgs5 = fp.series('DGS5',enddate)
dgs10 = fp.series('DGS10',enddate)
dgs20 = fp.series('DGS20',enddate)
dgs30 = fp.series('DGS30',enddate)

dgs2data = dgs2.data.loc[dgs2.data.index>'2019-01-01']
dgs3data = dgs3.data.loc[dgs3.data.index>'2019-01-01']
dgs5data = dgs5.data.loc[dgs5.data.index>'2019-01-01']
dgs10data = dgs10.data.loc[dgs10.data.index>'2019-01-01']
dgs20data = dgs20.data.loc[dgs20.data.index>'2019-01-01']
dgs30data = dgs30.data.loc[dgs30.data.index>'2019-01-01']


fig = make_subplots(rows=3, cols=2, 
       subplot_titles=("2년", "3년", "5년", "10년","20년","30년"))

fig.add_trace(
    go.Scatter(x=dgs2data.index, y=dgs2data.values, name="2년"),
    row=1,col=1,
)
fig.add_trace(
    go.Scatter(x=dgs3data.index, y=dgs3data.values, name="3년"),
    row=1,col=2,
)
fig.add_trace(
    go.Scatter(x=dgs5data.index, y=dgs5data.values, name="5년"),
    row=2,col=1,
)
fig.add_trace(
    go.Scatter(x=dgs10data.index, y=dgs10data.values, name="10년"),
    row=2,col=2,
)
fig.add_trace(
    go.Scatter(x=dgs20data.index, y=dgs20data.values, name="20년"),
    row=3,col=1,
)
fig.add_trace(
    go.Scatter(x=dgs30data.index, y=dgs30data.values, name="30년"),
    row=3,col=2
)

fig.update_layout(title_text='미국 장단기 국채', title_x=0.5)

fig.show()
""""""
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=dgs2data.index, y=dgs2data.values, name="2년"),
)
fig.add_trace(
    go.Scatter(x=dgs3data.index, y=dgs3data.values, name="3년"),
)
fig.add_trace(
    go.Scatter(x=dgs5data.index, y=dgs5data.values, name="5년"),
)
fig.add_trace(
    go.Scatter(x=dgs10data.index, y=dgs10data.values, name="10년"),
)
fig.add_trace(
    go.Scatter(x=dgs20data.index, y=dgs20data.values, name="20년"),
)
fig.add_trace(
    go.Scatter(x=dgs30data.index, y=dgs30data.values, name="30년"),
)
fig.show()


df = pd.concat([dgs2data, dgs3data, dgs5data, dgs10data, dgs20data, dgs30data], axis=1)
df.columns = ['국채2년','국채3년','국채5년','국채10년','국채20년','국채30년']
df1 = df.loc[(df.index.month == 1) & (df.index.day == 3)]
# df1=df.loc[df.index.strftime('%y%d').isin(['1901','2001','2101','2201','2301','2401'])]
df2 = df1.transpose()
df
df1
df2

fig=px.line(data_frame=df2, x=df2.index, y=list(df2.columns.strftime("%Y-%m-%d")),
           facet_col='variable',facet_col_wrap=4)
fig.update_layout(title_text='미국채 장단기금리 수익률곡선',title_x=0.5)
fig.show()

