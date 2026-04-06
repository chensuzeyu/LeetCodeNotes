# Python 3 速查 · 刷题（力扣 / 竞赛写法）

内置与标准库中**写算法题最常遇到**的部分：`enumerate`、`heapq`、`bisect`、`Counter`、`defaultdict`、记忆化、位运算等。  
每节有对应 `scripts/` 演示，**运行即见输出**。

## 怎么用

```bash
cd python-core-quickref/leetcode/scripts
python run_all.py
```

或单课：`python 05_heapq_bisect.py`  

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

## 学习顺序

`01` → `02` → `04` →（按需 `03`）→ `05` → `06` → `07`

**日常写脚本、JSON/正则/路径**见并列目录 [dev/README.md](../dev/README.md)。

## 维护

新增刷题向主题：在本目录加 `0x-*.md`，在 `scripts/` 加 `0x_*.py`，并更新 `scripts/run_all.py` 的 `demos` 列表。
