



### 要求：

1. 创建一个模型，以确定为维多利亚州消防局（CFA）的新部门“丛林大火快速响应局”购买的SSA无人机和无线电直放站无人机的最佳数量和混合策略。您的模型应该在能力和安全性与经济性之间取得平衡，并考虑观察和通信任务的需求和地形。您的模型还应将火灾事件的大小和频率作为参数。

##### 部署的总体规划：

- 确定要防范的区域
- 填充完全度 每个位置都要监测

- 无人机路径规划
- “快速” -> 重合度

##### 部署的具体细则（要考虑的点）

- 森林起火原因分析 -> 在易着火点附近多部署无人机看守
- 应该将火情作为参数实时输入





2. 说明您的模型如何适应未来十年内极端火灾事件不断变化的可能性。假设无人机系统的成本保持不变，请估计什么设施的成本将会增加。

- 【侧重变化】结合【1】：
  - 火情是动态在变化的 【（有可能发生的火情）与（时间）的模型】
  - 极端情况下（多处起火/发现时火势较大/火势发展迅猛）调动与监测
  - 结合气候关系：
    - 引入降水量与火情的关系
    - 引入风向和风的大小对火情的影响
- 估算成本：





3. 确定一个模型，以优化用于在不同地形上发生不同大小火灾的VHF / UHF无线电中继无人机的位置，如图2所示：东维多利亚州地形图。请注意，海拔范围从沿海的海平面到维多利亚山的Bogong的1,986米。

- 引入海拔对模型的影响
  - 



4. 在模型的支持下，准备一份一页到两页带注释的预算请求，以供CFA提交给维多利亚州政府。

   

![1](F:\Projects\2021-2 数学建模美赛\MCM-ICM-2021\B\1.jpg)

图1显示了该地区从2019年10月1日到2020年1月7日的野火热点，黄色表示从10月1日到1月6日的大火，红色表示2020年1月7日的正在燃烧的火。



![2](F:\Projects\2021-2 数学建模美赛\MCM-ICM-2021\B\2.jpg)
