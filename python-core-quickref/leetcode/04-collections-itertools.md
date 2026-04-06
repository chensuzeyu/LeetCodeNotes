# 04 · collections 与 itertools

完整演示：[scripts/04_collections_itertools.py](scripts/04_collections_itertools.py)  
运行：`python 04_collections_itertools.py`

下文「预期输出」与脚本一致；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## collections

| 类型 | 何时用 |
|------|--------|
| `Counter(iterable)` | 频次统计；常与哈希/滑动窗口一起出现 |
| `deque(maxlen=…)` | 两端 O(1) 进出；单调队列、BFS；`maxlen` 满时一侧自动挤掉旧元素 |

### `Counter`

- **未见过的键**：`c[k]` 读到 **`0`**（不抛异常），适合直接加减计数。
- **`most_common(n)`**：返回出现次数最高的若干 `(元素, 次数)`。

**预期输出摘录**：

```text
Counter([...]) -> Counter({'a': 3, 'b': 1, 'c': 1})
c['a'] = 3   c['z']（未见过的键）= 0
c.most_common(2) = [('a', 3), ('b', 1)]
```

### `deque` 与 `maxlen`

- **`maxlen`** 满后从对侧 `append`，**最先进入的一侧会被挤出**（常用于定长滑动窗口）。

**预期输出摘录**：

```text
deque([1,2,3], maxlen=3).append(4) -> [2, 3, 4] （左端被挤掉）
```

## itertools（高频子集）

| 函数 | 作用 |
|------|------|
| `permutations(iterable, r)` | 排列 |
| `combinations(iterable, r)` | 组合（无序、不重复选） |
| `accumulate(iterable)` | 前缀和/累乘等（可传 `func`） |
| `groupby(iterable, key)` | **需要先按 key 有序**（至少相邻同键）；否则分组语义是「相邻段」而非「全局同键」 |

### `permutations` 与 `combinations`

**预期输出摘录**：

```text
permutations([1,2,3], 2) = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
combinations([1,2,3], 2) = [(1, 2), (1, 3), (2, 3)]
```

### `groupby` 必须先排好序

- 对无序数据：`sorted(iterable, key=...)` 再 `groupby`，否则同键不相邻会拆成多段。

**预期输出摘录**：

```text
runs = 'aaabbbcca' -> groupby -> [('a', ['a', 'a', 'a']), ('b', ['b', 'b', 'b']), ('c', ['c', 'c']), ('a', ['a'])]
groupby(sorted, key=首元) -> [(1, [(1, 'b')]), (2, [(2, 'a'), (2, 'c')])]
```

### `zip_longest` 与内置 `zip`

- 内置 **`zip`** 以**最短**序列为准（见 [01-builtins.md](01-builtins.md)）。
- **`itertools.zip_longest`**：用 **`fillvalue`** 补齐较短序列。

**预期输出摘录**：

```text
zip([1,2], [10]) -> [(1, 10)]
zip_longest([1,2], [10], fillvalue=0) -> [(1, 10), (2, 0)]
```

与 `zip` 搭配：若要多条序列等长对齐且可能要补齐，可用 `zip_longest`（演示见脚本）。  
**堆**（Top K、合并多路有序流）见 [05-heapq-bisect.md](05-heapq-bisect.md)。

## 官方文档

- [collections](https://docs.python.org/3/library/collections.html)  
- [itertools](https://docs.python.org/3/library/itertools.html)
