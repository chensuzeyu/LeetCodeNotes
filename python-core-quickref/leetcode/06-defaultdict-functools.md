# 06 · defaultdict 与 functools

完整演示：[scripts/06_defaultdict_functools.py](scripts/06_defaultdict_functools.py)  
运行：`python3 06_defaultdict_functools.py`

下文各「输入代码 / 输出结果」与脚本逐段对应；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## collections.defaultdict

| 工厂 | 典型用途 |
|------|----------|
| `defaultdict(list)` | 邻接表、分组：`d[k].append(v)` 无需 `setdefault` |
| `defaultdict(int)` | 计数：等价于对缺失键当 0 再加 |
| `defaultdict(set)` | 去重聚合：`d[k].add(v)` |

### `defaultdict(list)`

**输入代码**：

```python
edges = [("a", 1), ("b", 2), ("a", 3)]
g = defaultdict(list)
for k, v in edges:
    g[k].append(v)
```

**输出结果**：

```text
edges -> {'a': [1, 3], 'b': [2]}
```

### `defaultdict(int)` 与 `defaultdict(set)`

**输入代码**：

```python
dd = defaultdict(int)
for ch in "abacb":
    dd[ch] += 1

ds = defaultdict(set)
ds["k"].add(1)
ds["k"].add(1)
```

**输出结果**：

```text
频数 -> {'a': 2, 'b': 2, 'c': 1}
{'k': {1}}
```

### 与 `Counter`

- **`Counter`**：专用于频次统计，带 `most_common` 等现成 API。
- **`defaultdict`**：更泛化，值类型不限；需要自己决定如何初始化与累加。

## functools

| 对象 | 说明 |
|------|------|
| `functools.cache`（Py3.9+） | 无上限缓存，适合递归 / DP，前提是状态参数都可哈希 |
| `functools.lru_cache(maxsize=...)` | 有上限 LRU；`maxsize=None` 时接近“尽量存满” |
| `functools.reduce` | 把二元函数累积到序列上；多数场景 `sum` / `for` 更清晰 |

### `cache`

**输入代码**：

```python
@cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

fib(6)
fib.cache_info()
```

**输出结果**：

```text
fib(6) = 8
cache_info = CacheInfo(hits=4, misses=7, maxsize=None, currsize=7)
```

### `lru_cache(maxsize=...)`

- 参数必须可哈希；`list` / `dict` 这类可变对象不能直接拿来做缓存键。

**输入代码**：

```python
calls = 0

@lru_cache(maxsize=32)
def path_count(m: int, n: int) -> int:
    ...

path_count(3, 3)
path_count.cache_info()
```

**输出结果**：

```text
path_count(3,3) = 20  递归函数实际调用次数: 15
lru_cache_info = CacheInfo(hits=4, misses=15, maxsize=32, currsize=15)
```

### `reduce`

**输入代码**：

```python
reduce(add, [1, 2, 3, 4], 0)
```

**输出结果**：

```text
reduce(add, [1,2,3,4], 0) = 10
```

## 官方文档

- [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)  
- [functools](https://docs.python.org/3/library/functools.html)
