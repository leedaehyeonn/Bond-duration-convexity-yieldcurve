
# Bond Duration & Convexity
> Hull 책은 Taylor Series를 이용해 채권, BSM, Delta-Gamma Trading을 설명하고 있다. 이 글은 Taylor 전개를 통해 채권의 Duration과 Convexity를 정리했다.

금리 변화에 따른 채권가격의 변화율을 계산하기 위해 Taylor Series를 활용한다. Taylor 전개의 첫째항은 *Duration*(이자율 민감도), 둘째항은 *Convexity*로 정의된다. 연속복리를 가정하고 *Duration*(이자율 민감도)을 계산하면 수식의 해석상 만기의 가중평균(Macaulay Duration)이 된다. 즉, 연속복리 하에서 채권 만기의 가중평균과 이자율 민감도는 동일하다. 이산형으로 compounding 한다면 이자율 민감도는 $\frac{Macaulay \;Duration}{1+y}$ 형태가 되며 이를 단순히 *Modified Duration*이라 한다. 마지막으로 이자율 변화값이 클 때 오차를 반영하기 위해 *Convexity*를 사용한다.

## Taylor Expansion을 통한 Duration, Convexity 유도
---
Taylor 전개를 통해 함수 $f(x)$를 $x=a$에서 다항함수로 근사시킬 수 있다. 일반적으로 다음과 같이 식 변형이 가능하다.


$$
\begin{aligned}
f(x) &\approx \sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n \newline
&= f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2 \dots
\end{aligned}
$$


<!-- <br>
$$
\begin{aligned}
f(x^{*}) &\approx \sum_{n=0}^{\infty}\frac{f^{(n)}(x)}{n!}(x^{*}-x)^n \newline
&=f(x)+f'(x)(x^{*}-x) +\frac{f''(x)}{2!}(x^{*}-x)^2 \dots
\end{aligned}
$$ -->


$$
\begin{aligned}
f(x+\Delta x) &\approx \sum_{n=0}^{\infty}\frac{f^{(n)}(x)}{n!}(x+\Delta x-x)^n\newline
&=f(x)+f'(x)\Delta x+\frac{f''(x)}{2!}(\Delta x)^2 \dots
\end{aligned}
$$


채권의 가격을 이자율의 함수 $B(y)$로 가정하고 Taylor Expansion을 이용하면 Duration과 Convexity를 유도할 수 있다.


$$
\begin{aligned}
B(y+\Delta y) &\approx \sum_{n=0}^{\infty}\frac{B^{(n)}(y)}{n!}(\Delta y)^n\newline
&=B(y)+B'(y)\Delta y+\frac{B''(y)}{2!}(\Delta y)^2 \dots
\end{aligned} 
$$


이자율 변동에 따른 채권가격의 변화율로 식을 수정하면 다음과 같다.


$$
\begin{align}
B(y+\Delta y) -B(y)&\approx B'(y)\Delta y+\frac{B''(y)}{2!}(\Delta y)^2  \nonumber \dots\newline \nonumber
\Delta B &\approx \frac{dB}{dy}\Delta y + \frac{1}{2}\frac{d^2B}{dy^2}(\Delta y)\dots\newline
\frac{\Delta B}{B} &\approx \frac{1}{B}\frac{dB}{dy}\Delta y + \frac{1}{2}\frac{1}{B}\frac{d^2B}{dy^2}(\Delta y)^2\newline
&= -Duration\  \Delta y + \frac{1}{2}Convexity\ (\Delta y)^2
\end{align}
$$


## Duration
---
(1)번 식에서 유도된 Duration은 연속복리든 이산형복리든 만기의 가중평균을 포함한다. Duration 자체가 만기의 가중평균이다. 연속복리의 경우 Duration은 만기의 가중평균 그 자체가 되며, 이산형복리의 경우 만기의 가중평균/(1+y)의 값으로 계산된다. 단순히 이때의 Duration을 Modified Duration이라 한다.
흔히 Macaulay Duration은 만기의 가중평균이며 Modified Duration을 이자율 민감도로 해석하는 경우가 많은데, 이는 compounding을 이산형으로 적용했을 때의 얘기이며 연속복리라면 Macaulay Duration이 만기의 가중평균이자 이자율 민감도이다.


- $\frac{1}{B}\frac{dB}{dy}$ 에서 B(y)를 연속복리로 compounding 할 경우, 이때 Duration은 만기의 가중평균이다.


$$
\begin{aligned}
B(y) &= \sum_{i=1}^{n}c_ie^{-yt_i}\newline
\frac{1}{B}\frac{dB}{dy} &= -\frac{1}{B}\sum_{i=1}^{n}t_ic_ie^{-yt_i}\newline
&=-\sum_{i=1}^{n}t_i [\frac{c_ie^{-yt_i}}{B}]\newline
&=-Duration\quad\quad (Macaulay\ Duration)
\end{aligned}
$$


- $\frac{1}{B}\frac{dB}{dy}$ 에서 B(y)를 이산형복리로 annual compounding 할 경우, 이때 Duration은 만기의 가중평균에 (1+y)를 나눈 값이 되고, 이것을 수정 듀레이션이라 한다.


$$
\begin{aligned}
B(y) &= \sum_{i=1}^{n}\frac{c_i}{(1+y)^{t_i}}\newline
\frac{1}{B}\frac{dB}{dy} &= -\frac{1}{B}\sum_{i=1}^{n}\frac{t_ic_i}{(1+y)^{t_i}}\frac{1}{1+y}\newline
&=-\sum_{i=1}^{n}t_i [\frac{\frac{c_i}{(1+y)^{t_i}}}{B}] \frac{1}{1+y}\newline
&=-\frac{Macaulay\ Duartion}{1+y}\newline
&=-Duration^*\quad\quad (Modified\ Duration)
\end{aligned}
$$


- $\frac{1}{B}\frac{dB}{dy}$ 에서 B(y)를 이산형복리로 1년에 m번 compounding 할 경우로 일반화


$$
\begin{aligned}
B(y) &= \sum_{i=1}^{n}\frac{c_i}{(1+\frac{y}{m})^{mt_i}}\newline
\frac{1}{B}\frac{dB}{dy} &= -\frac{1}{B}\sum_{i=1}^{n}\frac{t_ic_i}{(1+\frac{y}{m})^{mt_i}}\frac{1}{1+\frac{y}{m}}\newline
&=-\sum_{i=1}^{n}t_i [\frac{\frac{c_i}{(1+\frac{y}{m})^{t_i}}}{B}] \frac{1}{1+\frac{y}{m}}\newline
&=-\frac{Macaulay\;Duartion}{1+\frac{y}{m}}\newline
&=-Duration^*\quad\quad (Modified\ Duration)
\end{aligned}
$$


## Convexity
---
(1)번식에서 유도된 convexity는 연속복리든 이산복리든 듀레이션과 달리 그 자체로 직관적인 의미를 가지지는 않는다. 다만 $\Delta y$의 크기가 크다면 곡률을 고려하여 보다 정확하게 근사시킬 수 있다.


- $\frac{1}{B}\frac{d^2B}{dy^2}$에서 B(y)를 연속복리로 compounding 한다고 가정하면


$$
\begin{aligned}
\frac{1}{B}\frac{dB}{dy} &= -\frac{1}{B}\sum_{i=1}^{n}t_ic_ie^{-yt_i}\newline
\frac{1}{B}\frac{d^2B}{dy^2}&=\frac{1}{B}\sum_{i=1}^{n}t_i^2c_ie^{-yt_i}\newline
\end{aligned}
$$


- $\frac{1}{B}\frac{d^2B}{dy^2}$에서 B(y)를 이산형 복리로 compounding 한다고 가정하면


$$
\begin{aligned}
\frac{1}{B}\frac{dB}{dy} &= -\frac{1}{B}\sum_{i=1}^{n}\frac{t_ic_i}{(1+y)^{t_i}}\frac{1}{1+y}\newline
\frac{1}{B}\frac{d^2B}{dy^2} &= \frac{1}{B}\sum_{i=1}^{n}\frac{t_i(t_i+1)c_i}{(1+y)^{t_i}}\frac{1}{(1+y)^2}\newline
\end{aligned}
$$


- 두 채권이 다른 모든 조건은 동일하다 가정하고 Convexity만 다를 경우 금리변화에 따른 채권가격의 변화율을 관찰해보자. $X$의 곡률이 $Y$의 곡률보다 크기 때문에, 금리가 상승하든 하락하든 채권 $X$의 가격변화율이 채권 $Y$의 가격변화율보다 항상 유리하다. 즉, 금리 하락으로 인한 가격 상승폭은 더 크고, 금리 상승으로 인한 가격하락의 폭은 더 작다. 또한, Convexity가 큰 채권이라면 Duration만으로 가격변화율을 추정하는데 한계가 있음을 알 수 있다.

<p align="center">
  <img src="https://github.com/leedaehyeonn/Bond-duration-convexity-yieldcurve/assets/144612668/648eed54-c279-4b68-9b09-da1ca0440351" alt="Convexity">
</p>


Convexity가 큰 채권이란 Duration이 큰 채권과 맥락이 같다. 수식에서 봐도 잔존만기가 길수록, coupon rate이 작을수록, YTM이 작을수록 볼록성이 클 것이다. YTM이 작을수록 볼록성이 크다는 것은, 채권이 비쌀수록 이자율 변동에 유리하다는 것과 같다.
  
<!-- $$
\begin{aligned}
\frac{1}{B}\frac{d^2B}{dy^2}=\frac{1}{B}\sum_{i=1}^{n}t_i^2c_ie^{-yt_i}\newline
\end{aligned}
$$ -->
---


<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [['$', '$']]},
    messageStyle: "none",
    "HTML-CSS": { availableFonts: "TeX", preferredFont: "TeX" },
  });
</script>

