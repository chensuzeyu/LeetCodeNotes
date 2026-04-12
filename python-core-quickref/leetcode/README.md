# Python 3 速查 · 刷题（力扣 / 竞赛写法）

内置与标准库中**写算法题最常遇到**的部分：`enumerate`、`heapq`、`bisect`、`Counter`、`defaultdict`、记忆化、位运算等。  
每节有对应 `scripts/` 演示，**运行即见输出**。

## 怎么用

```bash
cd python-core-quickref/leetcode/scripts
python3 run_all.py
```

或单课：`python3 05_heapq_bisect.py`  

要求：**Python 3.9+**。Windows 终端乱码见上层总 [README.md](../README.md)。

## 文档索引

| 文档 | 演示脚本 | 内容 |
|------|----------|------|
| [01-builtins.md](01-builtins.md) | [scripts/01_builtins.py](scripts/01_builtins.py) | `len` `range` `enumerate` `zip` `sorted` `min/max` `sum` `any/all` `open` |
| [02-containers.md](02-containers.md) | [scripts/02_containers.py](scripts/02_containers.py) | `list` `dict` `str` `set` |
| [03-math-rounding.md](03-math-rounding.md) | [scripts/03_math_rounding.py](scripts/03_math_rounding.py) | 取整/`round`、`gcd`/`lcm`/`pow(..., mod)`/`isqrt`/`comb`/`perm`、`decimal` |
| [04-collections-itertools.md](04-collections-itertools.md) | [scripts/04_collections_itertools.py](scripts/04_collections_itertools.py) | `Counter` `deque`、`itertools` |
| [05-heapq-bisect.md](05-heapq-bisect.md) | [scripts/05_heapq_bisect.py](scripts/05_heapq_bisect.py) | `heapq`、`bisect` |
| [06-defaultdict-functools.md](06-defaultdict-functools.md) | [scripts/06_defaultdict_functools.py](scripts/06_defaultdict_functools.py) | `defaultdict`、`cache` / `lru_cache`、`reduce` |
| [07-chr-bitwise.md](07-chr-bitwise.md) | [scripts/07_chr_bitwise.py](scripts/07_chr_bitwise.py) | `ord`/`chr`、位运算 |
| [08-loops.md](08-loops.md) | [scripts/08_loops.py](scripts/08_loops.py) | `for` / `while`、`break` / `continue`、`enumerate`、`zip`、倒序遍历 |

## 学习顺序

`01` → `08` → `02` → `04` →（按需 `03`）→ `05` → `06` → `07`

**日常写脚本、JSON/正则/路径**见并列目录 [dev/README.md](../dev/README.md)。

## 维护

新增刷题向主题：在本目录加 `0x-*.md`，在 `scripts/` 加 `0x_*.py`，并更新 `scripts/run_all.py` 的 `demos` 列表。

## 编写规范

- 各课 Markdown 是对应脚本的说明层；读者应能从文档直接对照到 `scripts/*.py` 的真实输入与真实输出。
- 每个表格项都必须能在对应脚本中找到演示。表格若写了多个变体，脚本必须逐个跑到。
- 若正文已点名参数变体、别名、默认行为、返回值差异或常见报错，脚本至少要把高频分支真实跑到；不适合演示的边角分支，文档要明确写“只说明、不演示”。
- 每个知识点默认包含：
  - **输入代码**：与脚本变量、参数、调用一致。
  - **输出结果**：来自当前脚本真实运行结果。
  - **注意点**：只在容易误解时补充。
- 本册默认不使用“**预期输出摘录**”作为主展示形式，优先写完整的“输入代码 / 输出结果”。
- 输出应尽量确定、可复现；若只是为了稳定展示某个集合/映射结果，可在脚本中做最小限度的规范化打印。
- 修改脚本时必须同步更新对应 Markdown；若表格新增了用法，先补脚本，再补文档。

## 维护

- 新增刷题向主题：先补 `scripts/0x_*.py`，再写 `0x-*.md`，最后更新 `scripts/run_all.py`。
- 旧文档若仍保留“预期输出摘录”写法，应逐步迁移到完整的“输入代码 / 输出结果”格式。
- 文档与脚本的总约定见 [上级 README.md](../README.md)。
