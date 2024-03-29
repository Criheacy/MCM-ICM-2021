<h2><center>4&nbsp;&nbsp;&nbsp;模型计算与简化</center></h2>

### 4.1 一般模型（General / Trivial Model）

首先考虑携带中继器的无人机在风险区域探查的一般排布模型。该模型旨在解决在平坦空旷、无外界因素干扰情况下无人机的最佳排列方式，从而扩大有效覆盖面积，达到良好的通信效果。需要注意的是，因为该模型应用于普通场合的一般模型，因此模型约束于以下条件：

- 区域面积足够大。在考虑区域边界影响时可视为区域为环状连续的（Continuous）。
- 区域地形开阔空旷，地势平坦，无遮挡物。
- 区域任意子区域之间特征一致。

在此条件下，考虑无人机的最优排布方案。

#### 4.1.1 单无人机监测

首先考虑单一无人机在其飞行范围内的监测情况。单架无人机受限于该种类飞机的飞行距离（Flight Range），监测范围存在最大值，且最大监测区域为以无人机基点为中心的圆。又因为受制于飞行速度（Maximun Speed）以及飞机续航时间（Maximum Flight Time），无人机无法在每时每刻监测到最大监测区域的每一处，因此该模型需要设计方案以权衡监测面积与监测有效率的关系。

以下引入观测量“监测密度（Monitor Density）”与“响应时间（Response Time）”。监测密度定义为无人机能监测到的区域面积与最大监测区域面积的比值。注意到由于无人机有限的飞行速度，单一无人机能监测到的区域中并非每个位置都能被实时监测，即当监测区域内有前线探查人员发出警报后并不一定能立即被覆盖该区域的无人机监测到，而通常需要等待一段时间后才会有无人机进入该范围内并通过中继器将信号传递出去。为衡量警报被由无人机挂载的中继器传出的时间，引入观测量“响应时间”，表示在无人机监测区域内发出警报到信号被传出的时间，在理想模型中即任意时刻指定一点到下一次由无人机挂载的中继器的信号传递范围覆盖该点的时间。一般而言，在计算中通常取响应时间的数学期望值，即响应时间期望作为排布规律的属性。

在实际问题中，我们希望监测密度尽可能高，同时响应时间尽可能小；但此二者是矛盾的。若要增大监测密度，则需要无人机飞行到最大检测区域的每一个角落，但飞行路径的延长也意味着飞行周期延长，致使响应时间上升；而提升缩短响应时间和飞行周期又限制了飞机的飞行距离，使得监测密度下降。因此首先考虑响应时间不变，即飞行路径长度固定的情况下，对飞行路径形状的优化。易知在路径长度固定的情况下，飞行路径形状为圆形时围成的面积取得最大值，且中继器信号范围扫过的面积最大。

在飞行路径为圆形的情况下，注意到监测密度和响应时间的矛盾围绕“路径半径”这一观测量展开。将路径半径作为输入模型中的参数，在后续模型中根据其它参数，协调此二者的最佳取值。此外为增加监测密度，在同一小区域内设置多架无人机共同监测也是一种可行的方案。单元区域内多架无人机监测方案将在后文论述。

#### 4.1.2 多无人机排布阵列

以下讨论多架无人机排布阵列问题。假设无人机数量固定，根据一般模型的约束条件得区域任意子区域特征一致，则最优排布方案各处统一。上述已经确定，单一无人机的监测范围的外围围成圆形，则多架无人机的排布阵列问题即为若干大小相等圆形的区域填充问题。在多种填充方案中，六边形填充【可以引用参考文献】具有最高的填充密度，即在排布单元个数相同的条件下，未填充部分面积取得最小值。

考虑在全局排布中的区域总监视密度。类似于单个无人机监视的情况，多架无人机监视区域的总监视密度也可以用面积的比值定义，即每架无人机能监测到的面积总和之和除以区域的总面积。引入观测量“监测密度因子（Monitor Density Factor）”，定义为单个无人机的监测密度与总监测密度的比值，用于衡量无人机的排布方案对监测密度的影响。考虑无人机监测密度的面积定义，监测密度因子即为每个小区域的面积之和与区域的总面积之比。由于任意子区域特征一致性，加之六边形填充又具备填充单元可重复性，可得整个区域的监测密度因子与单元区域内的监测密度因子相等。因此可以利用六边形填充的最小排列单位，即单位三角形，作为监测密度因子的计算单元。

#### 4.1.3 模型参数声明及计算

声明模型参数如下表：

| Parameters | Description        |
| ---------- | ------------------ |
| r          | 中继器监测信号半径 |
| R          | 无人机最大航程     |
| d          | 无人机环绕路径半径 |
| D          | 监测单元半径       |
| \rho       | 单元监测密度       |
| \varOmega  | 总监测密度         |
| \mu        | 监测密度因子       |
| t_s        | 响应时间           |
| E(t_s)     | 响应时间的数学期望 |
| k          | 单元间圆心距       |

此外，题目中所给数据即公设参数变量含义对应表如下表所示：

| Parameters | Description      |
| ---------- | ---------------- |
| n          | 区域内无人机数量    |
| v_{fire}   | 火的蔓延速度       |
| a          | 灭火造成的反向加速度 |
| Q_{cost}   | 火灾损失           |
| S_m        | 区域总面积          |

首先计算针对单个无人机的监测情况。根据上述模型图形关系可得：
$$
\left\{
\begin{matrix}
D = r + d \\ 
r < d < 2r
\end{matrix}
\right.
$$
由监测密度定义式：

$$
\left\{
\begin{matrix}
\rho = \frac{S_{sweep}}{S_0} \\ 
S_{sweep} = \pi D^2 - \pi (d - r)^2 \\
S_0 = \pi D^2
\end{matrix}
\right.
$$

计算得：

$$
\rho = \frac{\pi D^2 - \pi (d - r)^2} {\pi D^2} = \frac{4dr} {D^2}
$$

考虑监测密度因子对总体监测密度的影响。由因子定义式得：

$$
\left\{
\begin{matrix}
\mu = \frac {\sum_{adj(i)} S_{i}} {S_t}  \\ 
S_{i} = \frac{1} {6} \times \pi D^2 \\
S_t = \frac {\sqrt{3}} {4} k^2
\end{matrix}
\right.
$$
计算得：

$$
\mu = \frac {\sum_{adj(i)} S_{i}} {S_t} = \frac {\frac{1}{2} \pi D^2} {\frac {\sqrt{3}} {4} k^2} = \frac {2 \pi} {\sqrt{3} k^2}
$$

由①②【标注\rho和\mu的计算式】可得：

$$
\varOmega = \rho \mu = \frac {8\pi dr} {\sqrt{3}D^2 k^2}
$$

由数学期望表达式得：
$$
E(t_s) = \frac {T(1 - \varOmega)^2} {2} = \frac{\pi d} {v_{p}}(1 - (\frac{r}{k})^2 \times \frac{2 \pi} {\sqrt{3}})^2
$$
将上述条件转化为非线性规划模型：
$$
goal = \min(\pi(v_{fire}E(t_s)+\frac{{v_{fire}}^2} {2a}) \times Q_{cost} + W_{cost}) \\
s.t.
\left \{
\begin{matrix}
 n \times \frac{\sqrt{3}} {2}k^2 \geq S_m \\
 E(t_s) = \frac {T(1 - \varOmega)^2} {2} = \frac{\pi d} {v_{p}}(1 - (\frac{r}{k})^2 \times \frac{2 \pi} {\sqrt{3}})^2 \\
 r < d < 2r
\end{matrix}
\right.
$$

### 4.2 风险度变化模型

#### 4.2.1 

