# 仿真文件及实验报告

!!! warning "仅供参考，请勿直接抄袭！"
    这里的仿真文件和报告用于复习、排查建模思路和对照参数设置。请独立完成课程作业和报告。

## Basic

- 仿真文件下载：[basic.osd](../../assets/simulations/basic.osd)
- 要点：
    - 熟悉 OptiSystem 基本组件和全局参数。
    - 检查码型、比特率、采样点数和接收端分析器连接是否正确。

## DCM

- 仿真文件下载：[dcm.osd](../../assets/simulations/dcm.osd)
- 要点：
    - 比较前补偿、后补偿和前后补偿。
    - 注意 DCF 色散符号、长度和放大器增益补偿。
    - 观察 Q 值、BER 和眼图随补偿方案变化的趋势。

## DWDM（抽查作业1）

- 仿真文件下载：[dwdm.osd](../../assets/simulations/dwdm.osd)
- 要点：
    - 关注通道数、波长间隔、传输距离和串扰之间的关系。
    - 调整复用/解复用器、滤波器和接收端参数时保持通道对应。
    - 多通道系统先从单通道调通，再逐步扩展。

### 实验报告

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../../assets/reports/assignment-1-report.pdf"
  title="抽查作业 1 实验报告"
></iframe>

<a class="pdf-open-link" href="../../assets/reports/assignment-1-report.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

## FWM

- 仿真文件下载：[fwm.osd](../../assets/simulations/fwm.osd)
- 要点：
    - 四波混频强度与相位匹配、通道间隔和色散有关。
    - 可以从有效面积、色散管理、通道间隔和偏振分配几个角度观察抑制效果。

## EDFA

- 仿真文件下载：[edfa.osd](../../assets/simulations/edfa.osd)
- 要点：
    - 关注泵浦功率、增益、噪声系数和增益饱和。
    - 观察 ASE 噪声对系统 Q 值和眼图的影响。

## Raman

- 仿真文件下载：[raman.osd](../../assets/simulations/raman.osd)
- 要点：
    - 关注泵浦波长、泵浦功率、光纤长度和增益之间的关系。
    - 对比 Raman 放大器和 EDFA 的应用差异。

## Hybrid

- 仿真文件下载：[hybrid.osd](../../assets/simulations/hybrid.osd)
- 要点：
    - 将 Raman 与 EDFA 组合，观察增益带宽扩展。
    - 优化时同时关注增益平坦度、噪声系数和输出功率。

## TDFA

- 仿真文件下载：[tdfa.osd](../../assets/simulations/tdfa.osd)
- 要点：
    - 关注放大波段、泵浦设置和增益曲线。
    - 可与 EDFA / Raman / Hybrid 的增益特性对照理解。

## PON

- 仿真文件下载：[pon.osd](../../assets/simulations/pon.osd)
- 要点：
    - 关注分光比、链路损耗、接收端功率预算和用户侧质量指标。
    - PON 是点到多点架构，核心器件是光分束器。

## Metro（抽查作业2）

- 仿真文件下载：[metro.osd](../../assets/simulations/metro.osd)
- 要点：
    - 关注城域网中的环形/网状结构、链路损耗和放大补偿。
    - 检查各节点接收质量，避免只优化单一路径。

### 实验报告

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../../assets/reports/assignment-2-report.pdf"
  title="抽查作业 2 实验报告"
></iframe>

<a class="pdf-open-link" href="../../assets/reports/assignment-2-report.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

## COC

- 仿真文件下载：待补充。
- 要点：待补充。

## OTDM

- 仿真文件下载：待补充。
- 要点：待补充。

## 公司出题

- 仿真文件下载：待补充。
- 要点：待补充。
