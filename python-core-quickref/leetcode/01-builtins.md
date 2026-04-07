# 01 · 高频内置函数

完整演示：[scripts/01_builtins.py](scripts/01_builtins.py)  
运行：`python3 01_builtins.py`（在 `leetcode/scripts` 目录下）

下文各「输入代码 / 输出结果」与脚本逐段对应；若你改动了脚本，请同步更新本文对应块（见上层 [README.md 维护约定](../README.md)）。

## 速查表

| 函数 | 典型用途（刷题 / 日常） |
|------|-------------------------|
| `len(x)` | 序列长度；配合 `range(len(nums))` 遍历下标 |
| `range(stop)` / `range(a, b)` / `range(a, b, step)` | 整数序列；**不含**终点 `b` |
| `enumerate(iterable, start=0)` | 同时拿到下标和元素 |
| `zip(*iterables)` | 并行遍历多列；最短列截断 |
| `sorted(iterable, key=..., reverse=...)` | **返回新列表**，不改动原序列 |
| `min` / `max` | 可传 `key=`；多元素时刷题常用 |
| `sum(iterable, start=0)` | 求和；`start` 可设初始累加值 |
| `any` / `all` | 是否存在真值 / 是否全真（短路求值） |
| `open(path, mode, encoding="utf-8")` | 读写文件；脚本与本地数据处理 |

## `len` / `range`

- `range(a, b)` 生成从 `a` 到 `b - 1` 的整数，**不含** `b`。
- `range(stop)` 等价于 `range(0, stop)`；`step` 可为负。

**输入代码**：

```python
nums = [2, 7, 11, 15]
len(nums)
list(range(len(nums)))
list(range(1, 4))
list(range(4, 1, -1))
```

**输出结果**：

```text
nums = [2, 7, 11, 15]
len(nums) = 4
list(range(len(nums))) = [0, 1, 2, 3]
list(range(1, 4)) = range(a,b) -> [1, 2, 3]
list(range(4, 1, -1)) = step=-1 -> [4, 3, 2]
```

## `enumerate(iterable, start=0)`

- `start` 是计数起点，默认 `0`。

**输入代码**：

```python
items = ["a", "b", "c"]
for start in (0, 1, 2):
    for i, x in enumerate(items, start=start):
        ...
```

**输出结果**（`!r` 为 `repr`，字符串会带引号）：

```text
items = ['a', 'b', 'c']
  start=0:
    i=0, x='a'
    i=1, x='b'
    i=2, x='c'
  start=1:
    i=1, x='a'
    i=2, x='b'
    i=3, x='c'
  start=2:
    i=2, x='a'
    i=3, x='b'
    i=4, x='c'
```

## `zip(*iterables)`

- 并行遍历多条序列，每次得到一个元组。
- 长度以最短序列为准；较长序列尾部会被丢弃。

**输入代码**：

```python
a = [1, 2, 3]
b = [10, 20]
list(zip(a, b))
```

**输出结果**：

```text
a = [1, 2, 3]  b = [10, 20]
list(zip(a, b)) = [(1, 10), (2, 20)]
for i, j in zip(a, b): (1+10) (2+20)
```

## `sorted` / `list.sort`

- `sorted(...)` 返回新列表，不修改原对象。
- `list.sort()` 原地排序，返回 `None`。

**输入代码**：

```python
arr = [3, 1, 4, 1, 5]
sorted(arr)
arr.sort()

words = ["bb", "a", "ccc"]
sorted(words, key=len)
sorted(arr, reverse=True)
```

**输出结果**：

```text
原 arr = [3, 1, 4, 1, 5]
sorted(arr) -> [1, 1, 3, 4, 5]  原 arr 仍为 [3, 1, 4, 1, 5]
arr.sort() 后 arr = [1, 1, 3, 4, 5] （list.sort 原地排序，返回 None）
sorted(words, key=len) -> ['a', 'bb', 'ccc']
sorted(arr, reverse=True) -> [5, 4, 3, 1, 1]
```

## `min` / `max`

- `min(5, 2, 8)` 是多标量比较。
- `min([5, 2, 8])` 是在单个序列里找最小值。

**输入代码**：

```python
pairs = [(1, 9), (5, 2), (3, 7)]
min(pairs)
min(pairs, key=lambda p: p[1])
min(5, 2, 8)
min([5, 2, 8])
```

**输出结果**：

```text
pairs = [(1, 9), (5, 2), (3, 7)]
min(pairs) = (1, 9)
min(pairs, key=lambda p: p[1]) = (5, 2)
min(5, 2, 8) = 2
min([5, 2, 8]) = 2
```

## `sum(iterable, start=0)`

- `start` 是初始累加值；空序列时会直接返回它。

**输入代码**：

```python
sum([1, 2, 3])
sum([], start=10)
```

**输出结果**：

```text
sum([1, 2, 3]) = 6
sum([], start=10) = 10
```

## `any` / `all`

- `any` 遇到第一个真值即停止。
- `all` 遇到第一个假值即停止。

**输入代码**：

```python
any([False, False, True])
all([1, 2, 0])
```

**输出结果**：

```text
any([False, False, True]) = True
all([1, 2, 0]) = False
```

## `open(path, mode, encoding="utf-8")`

- 读写文本时建议显式指定 `encoding="utf-8"`。

**输入代码**：

```python
with open(p, "w", encoding="utf-8", newline="\n") as f:
    f.write("hello\nworld\n")

with open(p, encoding="utf-8") as f:
    f.readlines()
```

**输出结果**（`<TMP_PATH>` 为临时目录，因本机而异）：

```text
写入(mode=w, encoding=utf-8): <TMP_PATH>/sample.txt
readlines() -> ['hello\n', 'world\n']
```

## 官方文档

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
