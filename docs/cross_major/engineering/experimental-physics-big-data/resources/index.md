# 资源搜集

这里不重复收录每一讲，而是保留后续做实验数据处理、复现实验结果或搭建分析管线时最值得回看的资料。完整内容可在[课程资料总表](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/)中按节次查找。

!!! tip "建议用法"
    HTML 讲义适合边读边运行示例，PDF 课件适合快速回顾框架；遇到蒙特卡罗、Make 数据生产线、关系代数和回归分析等较难主题时，再配合录像复习。

## 开始之前

- [Linux 基本命令和 WSL 安装](https://bdiep.thudep.com/talk/Linux%E5%9F%BA%E6%9C%AC%E5%91%BD%E4%BB%A4%E5%92%8CWSL%E5%AE%89%E8%A3%85.html)：Windows 用户配置课程环境时的首选入口。
- [课程 FAQ](https://physics-data.meow.plus/faq/)：优先排查环境、Git、Python、命令行与绘图问题。
- [课前培训导航](https://bdiep.thudep.com/main)：需要补 Linux、WSL、Python 或 macOS 环境配置时再按需查阅。

## 科学工作流与版本控制

“复现、透明、一次、最佳工具”四项原则贯穿整门课；Git 也是后续作业和科研协作的基础。可配合[总论 HTML 讲义](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/l0.html)阅读。

### 总论

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/course-overview.pdf"
  title="实验物理的大数据方法总论"
></iframe>

<a class="pdf-open-link" href="../assets/course-overview.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

## 数组、张量与数据格式

NumPy 数组是科学计算的基础；CSV、HDF5、JSON 的选择直接影响精度、规模和可复现性。

### 矩阵与张量

[HTML 讲义](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/l4.html)

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/matrices-and-tensors.pdf"
  title="矩阵与张量课件"
></iframe>

<a class="pdf-open-link" href="../assets/matrices-and-tensors.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

### 数据格式

[HTML 讲义](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/l5.html)

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/data-formats.pdf"
  title="数据格式课件"
></iframe>

<a class="pdf-open-link" href="../assets/data-formats.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

## 数据绘图与蒙特卡罗

绘图用于快速检查数据与中间结果；蒙特卡罗方法是实验物理模拟和不确定性分析的核心工具。

### 数据绘图

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/data-visualization.pdf"
  title="数据绘图课件"
></iframe>

<a class="pdf-open-link" href="../assets/data-visualization.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

### 蒙特卡罗方法

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/monte-carlo-methods.pdf"
  title="蒙特卡罗方法课件"
></iframe>

<a class="pdf-open-link" href="../assets/monte-carlo-methods.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

[2025 年第八讲录像](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/20250703.webm)

## GNU 命令行与 Make 数据生产线

这组工具可以把多步处理写成可检查、可增量执行、可复现的数据管线，是课程方法论落地的关键。

### GNU 命令行

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/gnu-command-line.pdf"
  title="GNU 命令行课件"
></iframe>

<a class="pdf-open-link" href="../assets/gnu-command-line.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

### GNU Make 数据生产线

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/gnu-make-pipeline.pdf"
  title="GNU Make 数据生产线课件"
></iframe>

<a class="pdf-open-link" href="../assets/gnu-make-pipeline.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

[2025 年第十讲录像](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/20250708.webm)

## 正则表达式、sed 与 awk

处理日志、仪器输出和批量文本数据时高频使用，语法容易遗忘，适合作为速查资料保留。

### 正则表达式

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/regular-expressions.pdf"
  title="正则表达式课件"
></iframe>

<a class="pdf-open-link" href="../assets/regular-expressions.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

### 从 sed 到 awk

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/sed-and-awk.pdf"
  title="从 sed 到 awk 课件"
></iframe>

<a class="pdf-open-link" href="../assets/sed-and-awk.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

## 关系代数、DataFrame 与回归分析

从表结构、数据变换到统计建模形成完整链条，适用于多数实验数据分析任务。

### 关系代数与 SQL

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/relational-algebra.pdf"
  title="关系代数与 SQL 课件"
></iframe>

<a class="pdf-open-link" href="../assets/relational-algebra.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

[2025 年第十三讲录像](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/20250714.webm)

### DataFrame

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/dataframe.pdf"
  title="DataFrame 课件"
></iframe>

<a class="pdf-open-link" href="../assets/dataframe.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

### 回归分析

<iframe
  class="pdf-viewer pdf-viewer--compact"
  src="../assets/regression-analysis.pdf"
  title="回归分析课件"
></iframe>

<a class="pdf-open-link" href="../assets/regression-analysis.pdf" target="_blank" rel="noopener">↗ 在新标签页中查看</a>

[2025 年第十五讲录像](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/20250716.webm)

## 完整入口

- [课程资料总表](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/)：16 讲的讲义、课件和 2019—2025 年录像。
- [2025 课程资料站](https://bdep2025.dpsast.org/)：2025 年课程与课前培训入口。

!!! info "文件来源"
    本页 PDF 均整理自清华大学“实验物理的大数据方法”公开课程资料，页面内保留课程总表与原始讲义入口，便于核对更新版本。
