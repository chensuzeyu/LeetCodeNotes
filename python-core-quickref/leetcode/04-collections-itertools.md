# 04 · collections 与 itertools

完整演示：`scripts/04_collections_itertools.py`  
运行：`python 04_collections_itertools.py`

## collections

| 类型 | 何时用 |
|------|--------|
| `Counter(iterable)` | 频次统计；常与哈希/滑动窗口一起出现 |
| `deque(maxlen=…)` | 两端 O(1) 进出；单调队列、BFS；`maxlen` 满时一侧自动挤掉旧元素 |

## itertools（高频子集）

| 函数 | 作用 |
|------|------|
| `permutations(iterable, r)` | 排列 |
| `combinations(iterable, r)` | 组合（无序、不重复选） |
| `accumulate(iterable)` | 前缀和/累乘等（可传 `func`） |
| `groupby(iterable, key)` | **需要先按已排序**；相邻相同键分组 |

与 `zip` 搭配：若要多条序列等长对齐且可能要补齐，可用 `zip_longest`（演示见脚本）。  
**堆**（Top K、合并多路有序流）见 [05-heapq-bisect.md](05-heapq-bisect.md)。

## 官方文档

- [collections](https://docs.python.org/3/library/collections.html)  
- [itertools](https://docs.python.org/3/library/itertools.html)
