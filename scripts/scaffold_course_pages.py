from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

COURSES = [
    ("foundations", "calculus-a-1", "微积分（甲）Ⅰ", "MATH1135G", "5.0", "一(秋冬)"),
    ("foundations", "calculus-a-2", "微积分（甲）Ⅱ", "MATH1136G", "5.0", "一(春夏)"),
    ("foundations", "linear-algebra-a", "线性代数（甲）", "MATH1232G", "3.5", "一(秋冬)/一(春夏)"),
    ("foundations", "college-physics-a-1", "大学物理（甲）Ⅰ", "PHY1001G", "4.0", "一(春夏)"),
    ("foundations", "college-physics-a-2", "大学物理（甲）Ⅱ", "PHY2001G", "4.0", "二(秋冬)"),
    ("foundations", "college-physics-lab", "大学物理实验", "PHY2005G", "1.5", "二(秋冬)"),
    ("foundations", "ode", "常微分方程", "MATH1138F", "1.0", "一(春)"),
    ("foundations", "complex-functions", "复变函数与积分变换", "MATH2131F", "1.5", "二(秋)"),
    ("foundations", "probability-statistics", "概率论与数理统计", "MATH2432F", "2.5", "二(秋冬)"),
    ("foundations", "pde", "偏微分方程", "MATH2132F", "2.0", "二(冬)"),
    ("foundations", "c-programming", "C程序设计基础及实验", "CS1001G", "4.0", "一(秋冬)"),
    ("foundations", "ai-foundations-a", "人工智能基础（A）", "CS1241G", "2.0", "一(春夏)"),
    ("foundations", "engineering-graphics", "工程图学", "ME1001F", "2.5", "一(春夏)"),
    ("foundations", "engineering-training", "工程训练", "ME1002F", "1.5", "二(秋冬)"),
    ("required", "intro-optoelectronics", "光电信息科学与工程导论", "OPT1001M", "2.0", "一(春夏)"),
    ("required", "circuit-foundations-lab", "电子电路基础及实验", "OPT2002M", "4.0", "二(秋冬)"),
    ("required", "digital-circuits", "数字电路", "OPT2003M", "2.0", "二(春夏)"),
    ("required", "electromagnetic-fields", "电磁场与电磁波", "OPT2004M", "2.5", "二(春夏)"),
    ("required", "discrete-math", "离散数学", "OPT2005M", "2.5", "二(春夏)"),
    ("required", "microcomputer-principles", "微机原理与接口技术", "OPT2006M", "3.5", "二(春夏)"),
    ("required", "applied-optics", "应用光学", "OPT2007M", "3.0", "二(春夏)"),
    ("required", "applied-optics-lab", "应用光学实验", "OPT2008M", "1.0", "二(夏)"),
    ("required", "optoelectronics", "光电子学", "OPT3009M", "3.0", "三(秋冬)"),
    ("required", "physical-optics", "物理光学", "OPT3010M", "4.0", "三(秋冬)"),
    ("required", "physical-optics-lab", "物理光学实验", "OPT3011M", "1.0", "三(冬)"),
    ("required", "optoelectronic-design-lab", "光电设计与综合实验", "OPT3012M", "2.5", "三(春夏)"),
    ("required", "optoelectronic-detection", "光电检测技术及系统", "OPT3013M", "3.0", "三(春夏)"),
    ("electives", "software-tech", "软件技术基础", "OPT2014M", "3.0", "二(秋冬)"),
    ("electives", "optical-communication-lab", "光通信技术及实验", "OPT2019M", "3.0", "二(春夏)"),
    ("electives", "advanced-optical-manufacturing", "先进光学制造", "OPT3028M", "2.0", "三(秋)"),
    ("electives", "quantum-optics", "量子光学基础及应用", "OPT3016M", "2.5", "三(秋冬)"),
    ("electives", "optoelectronic-materials", "光电材料及应用", "OPT3017M", "2.5", "三(秋冬)"),
    ("electives", "laser-technology", "激光技术及应用", "OPT3046M", "1.5", "三(春)"),
    ("electives", "nanophotonics", "纳米光子学基础", "OPT3063M", "2.0", "三(夏)"),
    ("electives", "signals-systems-b", "信号与系统（乙）", "OPT2015M", "3.0", "二(春夏)"),
    ("electives", "machine-vision-image-processing", "机器视觉与图像处理", "OPT3018M", "3.0", "三(秋冬)"),
    ("electives", "spectroscopy-applications", "光谱技术及应用", "OPT3037M", "2.0", "三(春)"),
    ("electives", "computational-imaging", "计算成像学", "OPT3065M", "1.5", "三(春)"),
    ("electives", "optical-imaging", "光学成像技术", "OPT3064M", "2.0", "三(春夏)"),
    ("electives", "data-communication-networks", "数据通信与计算机网络", "OPT2020M", "1.5", "二(春)"),
    ("electives", "solid-state-physics", "固体物理", "OPT2021M", "2.0", "二(夏)"),
    ("electives", "digital-signal-processing", "数字信号处理", "OPT3022M", "2.0", "三(秋)"),
    ("electives", "visual-information-applications", "视觉信息应用技术", "OPT3023M", "2.0", "三(秋)/三(冬)"),
    ("electives", "modern-communication", "现代通信原理", "OPT3025M", "2.0", "三(秋)"),
    ("electives", "optical-inertial-technology", "光学惯性技术", "OPT3026M", "2.0", "三(秋)"),
    ("electives", "precision-opto-mechanical-design", "光电精密机构设计", "OPT3027M", "2.0", "三(秋)"),
    ("electives", "optical-device-system-simulation", "光学器件与系统的建模仿真", "OPT3024M", "2.0", "三(秋冬)"),
    ("electives", "color-information-engineering", "颜色信息工程", "OPT3029M", "2.0", "三(冬)"),
    ("electives", "weak-signal-detection", "微弱信号检测", "OPT3030M", "2.0", "三(冬)"),
    ("electives", "quantum-precision-measurement", "量子精密测量及传感技术", "OPT3031M", "2.0", "三(冬)"),
    ("electives", "embedded-systems", "嵌入式系统与应用", "OPT3032M", "2.0", "三(春)"),
    ("electives", "error-theory", "误差理论与不确定度分析", "OPT3034M", "2.0", "三(春)"),
    ("electives", "introduction-to-optics", "Introduction to Optics", "OPT3036M", "1.5", "三(春)/四(冬)"),
    ("electives", "flexible-optoelectronics", "柔性光电子技术导论", "OPT3038M", "2.0", "三(春)"),
    ("electives", "extreme-optical-interferometry", "极端光学干涉技术与仪器", "OPT3066M", "2.0", "三(春)"),
    ("electives", "optoelectronic-entrepreneurship", "光电创新创业", "OPT3039M", "2.0", "三(春夏)"),
    ("electives", "fpga-dsp", "FPGA原理及其数字信号处理应用", "OPT3041M", "2.0", "三(夏)"),
    ("electives", "advanced-optical-topics", "先进光学技术专题", "OPT3042M", "2.0", "三(夏)"),
    ("electives", "integrated-optoelectronics", "集成光电子器件及设计", "OPT3043M", "1.5", "三(夏)"),
    ("electives", "advanced-optical-sensing", "先进光学传感技术", "OPT3069M", "1.5", "三(夏)"),
    ("electives", "thin-film-optics", "薄膜光学与技术", "OPT4044M", "1.5", "四(秋)"),
    ("electives", "optical-network", "光网络技术", "OPT4047M", "1.5", "四(秋)"),
    ("electives", "fiber-sensing", "光纤传感技术及应用", "OPT4048M", "1.5", "四(冬)"),
    ("electives", "infrared-terahertz-photonics", "红外和太赫兹光子学导论", "OPT4068M", "1.5", "四(冬)"),
    ("short_terms", "optomechanical-structure-design", "光机结构设计", "OPT1051M", "2.0", "一(短)"),
    ("short_terms", "optical-system-design", "光学系统设计", "OPT2053M", "2.0", "二(短)"),
    ("cross_major/economics", "macroeconomics-a", "宏观经济学（甲）", "", "", ""),
    ("cross_major/economics", "frontier-finance-practice", "前沿金融实务专题", "", "", ""),
    ("cross_major/economics", "securities-investment", "证券投资学（专题）", "", "", ""),
    ("cross_major/information-electronics", "signals-systems", "信号与系统", "", "", ""),
]


def render_course(title: str, code: str, credits: str, term: str) -> str:
    meta = ["---", f"title: {title}", "status: 待整理"]
    if code:
        meta.append(f"course_code: {code}")
    if credits:
        meta.append(f"credits: {credits}")
    if term:
        meta.append(f"term: {term}")
    meta.append("---")

    details = []
    if code:
        details.append(f"- 课程代码：{code}")
    if credits:
        details.append(f"- 学分：{credits}")
    if term:
        details.append(f"- 建议学期：{term}")
    if not details:
        details.append("- 课程信息：待补充")

    return (
        "\n".join(meta)
        + f"\n\n# {title}\n\n"
        + '!!! note "待整理"\n'
        + "    这里先保留课程笔记入口。整理时可以直接替换本页正文，并按需要保留上方元数据。\n\n"
        + "## 课程概览\n\n"
        + "\n".join(details)
        + "\n\n## 笔记\n\n待补充。\n\n## 资料\n\n待补充。\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Create missing course note pages.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing course pages.")
    args = parser.parse_args()

    created = 0
    skipped = 0
    for section, slug, title, code, credits, term in COURSES:
        path = DOCS / section / slug / "index.md"
        if path.exists() and not args.overwrite:
            skipped += 1
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_course(title, code, credits, term), encoding="utf-8", newline="\n")
        created += 1

    print(f"created_or_updated={created} skipped={skipped}")


if __name__ == "__main__":
    main()
