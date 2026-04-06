# 06 · defaultdict 与 functools

完整演示：`scripts/06_defaultdict_functools.py`  
运行：`python 06_defaultdict_functools.py`

## collections.defaultdict

| 工厂 | 典型用途 |
|------|----------|
| `defaultdict(list)` | 邻接表、分组：`d[k].append(v)` 无需 `setdefault` |
| `defaultdict(int)` | 计数：等价于对缺失键当 0 再加 |
| `defaultdict(set)` | 去重聚合：`d[k].add(v)` |

与 `Counter`：`Counter` 更偏「频次数数**专用**」；`defaultdict` 更泛化（值不一定是 int）。

## functools

| 对象 | 说明 |
|------|------|
| `functools.cache`（Py3.9+） | 无上限缓存，适合递归 / DP **状态参数都可哈希** |
| `functools.lru_cache(maxsize=…)` | 有上限 LRU，可 `maxsize=None` 等价「尽量存满」（注意内存） |
| `functools.reduce` | 把二元函数累积到序列上；多数场景 `sum`/`for` 更清晰，偶尔一题一行 |

`lru_cache` / `cache` 要求参数**可哈希**（`list` / `dict` 需转成 `tuple` 等）。

## 官方文档

- [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)  
- [functools](https://docs.python.org/3/library/functools.html)
