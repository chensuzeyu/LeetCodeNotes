# 04 · collections 与 itertools

完整演示：[scripts/04_collections_itertools.py](scripts/04_collections_itertools.py)  
运行：`python3 04_collections_itertools.py`

下文各「输入代码 / 输出结果」与脚本逐段对应；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## collections

| 类型 / 用法 | 何时用 |
|-------------|--------|
| `Counter(iterable)` | 频次统计；常与哈希/滑动窗口一起出现 |
| `Counter.update(iterable)` | 批量累加频次 |
| `deque(maxlen=...)` | 两端 O(1) 进出；BFS、单调队列、滑动窗口 |

### `Counter`

- **未见过的键**：`c[k]` 直接读到 `0`，不抛异常。
- **`most_common(n)`**：返回出现次数最高的若干 `(元素, 次数)`。
- `update(iterable)` 是**累加已有计数**，不是把旧结果覆盖掉。

**输入代码**：

```python
c = Counter(["a", "b", "a", "a", "c"])
c["a"], c["z"]
c.most_common(2)
c.update(["a", "b", "b"])
```

**输出结果**：

```text
Counter([...]) -> Counter({'a': 3, 'b': 1, 'c': 1})
c['a'] = 3   c['z']（未见过的键）= 0
c.most_common(2) = [('a', 3), ('b', 1)]
update(['a','b','b']) 后 -> {'a': 4, 'b': 3, 'c': 1}
```

### `deque` 与 `maxlen`

- `appendleft` / `popleft` 是 `deque` 的强项；如果你经常在普通 `list` 头部插删，通常就该想到 `deque`。
- `maxlen` 满后继续 `append`，最早进入的一端会被自动挤掉。

**输入代码**：

```python
dq = deque([1, 2])
dq.appendleft(0)
dq.append(3)
dq.popleft()
dq.pop()

win = deque([1, 2, 3], maxlen=3)
win.append(4)
```

**输出结果**：

```text
deque 操作后 list(dq) = [0, 1, 2, 3]
popleft -> 0  pop -> 3  剩下 [1, 2]
deque([1,2,3], maxlen=3).append(4) -> [2, 3, 4] （左端被挤掉）
```

## itertools（高频子集）

| 函数 | 作用 |
|------|------|
| `permutations(iterable, r)` | 排列 |
| `combinations(iterable, r)` | 组合（无序、不重复选） |
| `accumulate(iterable, func=...)` | 前缀和 / 累乘等 |
| `groupby(iterable, key)` | 需要先按 key 有序，否则只是相邻段分组 |
| `zip_longest(*iterables, fillvalue=...)` | 用指定值补齐较短序列 |

### `permutations` 与 `combinations`

- `permutations` 把顺序当成不同结果；`(1, 2)` 和 `(2, 1)` 都会出现。
- `combinations` 不看顺序，所以结果更少。

**输入代码**：

```python
list(itertools.permutations([1, 2, 3], 2))
list(itertools.combinations([1, 2, 3], 2))
```

**输出结果**：

```text
permutations([1,2,3], 2) = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
combinations([1,2,3], 2) = [(1, 2), (1, 3), (2, 3)]
```

### `accumulate`

- 默认是前缀和；传 `func=` 后可以变成前缀积、前缀最大值等“逐步累积”逻辑。

**输入代码**：

```python
list(itertools.accumulate([1, 2, 3, 4]))
list(itertools.accumulate([1, 2, 3, 4], func=operator.mul))
```

**输出结果**：

```text
accumulate([1,2,3,4]) -> [1, 3, 6, 10]
accumulate([1,2,3,4], func=operator.mul) -> [1, 2, 6, 24]
```

### `groupby`

- 对无序数据，先 `sorted(..., key=...)` 再 `groupby`，否则同键会被拆成多段。
- `groupby` 分的是“**相邻连续段**”，不是“全局所有相同键自动聚到一起”。

**输入代码**：

```python
runs = "aaabbbcca"
[(k, list(g)) for k, g in itertools.groupby(runs)]

raw = [(2, "a"), (1, "b"), (2, "c")]
ordered = sorted(raw, key=lambda t: t[0])
[(k, list(g)) for k, g in itertools.groupby(ordered, key=lambda t: t[0])]
```

**输出结果**：

```text
runs = 'aaabbbcca' -> groupby -> [('a', ['a', 'a', 'a']), ('b', ['b', 'b', 'b']), ('c', ['c', 'c']), ('a', ['a'])]
raw = [(2, 'a'), (1, 'b'), (2, 'c')]  sorted(key=首元) -> [(1, 'b'), (2, 'a'), (2, 'c')]
groupby(sorted, key=首元) -> [(1, [(1, 'b')]), (2, [(2, 'a'), (2, 'c')])]
```

### `zip_longest` 与内置 `zip`

- 内置 `zip` 以最短序列为准；`zip_longest` 会用 `fillvalue` 补齐。
- 如果你只是并行遍历且宁愿丢掉长序列尾巴，用普通 `zip` 更自然。

**输入代码**：

```python
list(zip([1, 2], [10]))
list(itertools.zip_longest([1, 2], [10], fillvalue=0))
```

**输出结果**：

```text
zip([1,2], [10]) -> [(1, 10)]
zip_longest([1,2], [10], fillvalue=0) -> [(1, 10), (2, 0)]
```

## 官方文档

- [collections](https://docs.python.org/3/library/collections.html)  
- [itertools](https://docs.python.org/3/library/itertools.html)
