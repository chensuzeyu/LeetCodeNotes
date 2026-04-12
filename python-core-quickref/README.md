# Python 3 核心速查（分册）

本仓库将速查拆成三册，避免刷题、日常开发与量化阅读混在同一目录里：

| 分册 | 路径 | 用途 |
|------|------|------|
| **刷题** | [leetcode/README.md](leetcode/README.md) | 力扣 / 竞赛常见：`heapq`、`bisect`、`Counter`、记忆化、位运算等（`01`～`08`） |
| **日常开发** | [dev/README.md](dev/README.md) | 脚本与工程打底：`01`～`11`（含 `random`/`copy` 等） |
| **量化阅读** | [quant/README.md](quant/README.md) | 围绕 `1_ETF轮动` 的 `pandas`、`numpy`、`backtrader`、`hkcodex` 速查（`01`～`10`） |

## 快速运行

**刷题向（连跑 01～07）：**

```bash
cd python-core-quickref/leetcode/scripts
python3 run_all.py
```

**日常向：**

```bash
cd python-core-quickref/dev/scripts
python3 run_all.py
```

**量化向：**

```bash
cd python-core-quickref/quant/scripts
python3 run_all.py
```

环境：**Python 3.9+**。Windows 下若中文乱码，可先 `chcp 65001` 或设置 `PYTHONIOENCODING=utf-8`。

## 维护约定

- 刷题新增：只动 `leetcode/` 与 `leetcode/scripts/run_all.py`。  
- 日常新增：只动 `dev/` 与 `dev/scripts/run_all.py`。  
- 量化新增：只动 `quant/` 与 `quant/scripts/run_all.py`。  
- 三套 scripts 各自带一份 `_io_util.py`，互不依赖，避免跨目录 import。  
- **文档与脚本对齐**：各课 `*.md` 中的「输入代码 / 输出结果」必须与对应 `scripts/*.py` 当前行为一致；若修改演示脚本，请同步更新该课 Markdown（避免读者对照跑不通）。

## 文档规范（三册共用）

- 文档是脚本输出的**说明层**，不是脱离脚本单独编写的示意文本。
- 表格是“**脚本可验证清单**”，不是“意图清单”；表格中写到的用法，必须能在对应脚本里找到真实演示。
- 一个表格行若同时列出多个变体，例如 `pop()` / `pop(i)`、`split()` / `split(",")`，脚本必须逐个跑到。
- 每个知识点默认包含三部分：
  - **输入代码**：与脚本中的真实变量、参数、调用一致。
  - **输出结果**：来自当前脚本真实运行结果。
  - **注意点**：仅在容易误解或容易踩坑时补一行。
- 默认不再使用“**预期输出摘录**”作为主展示形式；优先写完整、可对照的输入与输出。
- 修改已有主题时，先补或修 `scripts/*.py`，再同步更新对应 Markdown。
- 新增主题时，先写可运行脚本，再写文档；不要先写一份与脚本脱节的说明文。
- 动态输出的占位规则见各分册 README：`leetcode` 以确定性输出为主，`dev` 允许对少量环境敏感片段做占位规范化。

---

*与本仓库根目录 [README.md](../README.md) 中的 Python 3 说明一致。*
