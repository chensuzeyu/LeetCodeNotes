# 06 · defaultdict 与 functools

完整演示：[scripts/06_defaultdict_functools.py](scripts/06_defaultdict_functools.py)  
运行：`python 06_defaultdict_functools.py`

下文「预期输出」与脚本一致；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## collections.defaultdict

| 工厂 | 典型用途 |
|------|----------|
| `defaultdict(list)` | 邻接表、分组：`d[k].append(v)` 无需 `setdefault` |
| `defaultdict(int)` | 计数：等价于对缺失键当 0 再加 |
| `defaultdict(set)` | 去重聚合：`d[k].add(v)` |

### 与 `Counter`

- **`Counter`**：专用于**频次**、`most_common` 等 API。
- **`defaultdict`**：更泛化（值类型任意、逻辑自定义）；计数时 `dd[k] += 1` 与 `Counter` 二选一即可。

**预期输出摘录**：

```text
edges -> {'a': [1, 3], 'b': [2]}
频数 -> {'a': 2, 'b': 2, 'c': 1}
{'k': {1}}
```

## functools

| 对象 | 说明 |
|------|------|
| `functools.cache`（Py3.9+） | 无上限缓存，适合递归 / DP **状态参数都可哈希** |
| `functools.lru_cache(maxsize=…)` | 有上限 LRU，可 `maxsize=None` 等价「尽量存满」（注意内存） |
| `functools.reduce` | 把二元函数累积到序列上；多数场景 `sum`/`for` 更清晰，偶尔一题一行 |

### `cache` / `lru_cache`：参数必须可哈希

- **`list` / `dict`** 不能作缓存在参数时，需改成 `tuple` 等不可变形式。

**预期输出摘录**：

```text
fib(6) = 8
cache_info = CacheInfo(hits=4, misses=7, maxsize=None, currsize=7)
path_count(3,3) = 20  递归函数实际调用次数: 15
reduce(add, [1,2,3,4], 0) = 10
```

## 官方文档

- [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)  
- [functools](https://docs.python.org/3/library/functools.html)
