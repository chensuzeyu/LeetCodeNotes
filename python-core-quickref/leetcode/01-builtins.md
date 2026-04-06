# 01 · 高频内置函数

完整演示：[scripts/01_builtins.py](scripts/01_builtins.py)  
运行：`python 01_builtins.py`（在 `leetcode/scripts` 目录下）

下文「预期输出」与脚本当前打印一致；若你改动了脚本，请同步更新本文对应块（见上层 [README.md 维护约定](../README.md)）。

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

---

### `len` / `range`

- **`range(a, b)`**：生成从 `a` 到 **`b-1`** 的整数，**不含** `b`。`range(stop)` 等价于 `range(0, stop)`；`step` 可为负。

**示例**（见脚本首节）：

```python
nums = [2, 7, 11, 15]
len(nums)                          # 4
list(range(len(nums)))             # [0, 1, 2, 3]
list(range(1, 4))                  # [1, 2, 3]，注意没有 4
list(range(4, 1, -1))              # [4, 3, 2]
```

**预期输出摘录**：

```text
nums = [2, 7, 11, 15]
len(nums) = 4
list(range(len(nums))) = [0, 1, 2, 3]
list(range(1, 4)) = range(a,b) -> [1, 2, 3]
list(range(4, 1, -1)) = step=-1 -> [4, 3, 2]
```

---

### `enumerate(iterable, start=0)`

- **`iterable`**：要遍历的序列（或迭代器）。
- **`start`**：计数起点，默认 `0`。设为 `k` 时，**第一对**为 `(k, 首元素)`，之后每次 `i` 加 1，与元素一一对应。

**示例**：

```python
items = ["a", "b", "c"]
for start in (0, 1, 2):
    print(f"  start={start}:")
    for i, x in enumerate(items, start=start):
        print(f"    i={i}, x={x!r}")
```

**预期输出**（`!r` 为 `repr`，字符串带引号）：

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

---

### `zip(*iterables)`

- 并行迭代多条序列，每次迭代得到一个元组 `(a[i], b[i], …)`。
- **长度以最短为准**：较长序列**尾部会被丢弃**。需要和 `04` 中 `itertools.zip_longest` 对比时见该篇。

**示例**：

```python
a = [1, 2, 3]
b = [10, 20]
list(zip(a, b))   # [(1, 10), (2, 20)]，3 没有配对对象
```

**预期输出摘录**：

```text
a = [1, 2, 3]  b = [10, 20]
list(zip(a, b)) = [(1, 10), (2, 20)]
for i, j in zip(a, b): (1+10) (2+20)
```

---

### `sorted` / `list.sort`

- **`sorted(iterable, …)`**：**返回新列表**，不修改原可迭代对象（若传入列表，原列表不变）。
- **`list.sort()`**：**原地**排序，返回 **`None`**（不要写 `y = arr.sort()` 当排序结果用）。

**示例与注意**：Top K 堆、多路归并常用 `heapq`；在**已排序**列表上二分查找见 [05-heapq-bisect.md](05-heapq-bisect.md)。

**预期输出摘录**：

```text
原 arr = [3, 1, 4, 1, 5]
sorted(arr) -> [1, 1, 3, 4, 5]  原 arr 仍为 [3, 1, 4, 1, 5]
arr.sort() 后 arr = [1, 1, 3, 4, 5] （list.sort 原地排序，返回 None）
sorted(words, key=len) -> ['a', 'bb', 'ccc']
sorted(arr, reverse=True) -> [5, 4, 3, 1, 1]
```

---

### `min` / `max`

- **多标量**：`min(5, 2, 8)` 比较这几个数。
- **单序列**：`min([5, 2, 8])` 在列表里找最值。
- **慎写** `min(arr, b)`：除非你就是要在「`arr` 与标量 `b`」之间比大小；常见笔误是想对列表求最值却多传了参数。

**预期输出摘录**：

```text
pairs = [(1, 9), (5, 2), (3, 7)]
min(pairs) = (1, 9)
min(pairs, key=lambda p: p[1]) = (5, 2)
min(5, 2, 8) = 2
min([5, 2, 8]) = 2
```

---

### `sum(iterable, start=0)`

- **`start`**：累加初值；空序列时 `sum([], start=10) == 10`。

**预期输出摘录**：

```text
sum([1, 2, 3]) = 6
sum([], start=10) = 10
```

---

### `any` / `all`

- 短路求值：`any` 遇第一个真值即 `True`；`all` 遇第一个假值即 `False`。

**预期输出摘录**：

```text
any([False, False, True]) = True
all([1, 2, 0]) = False
```

---

### `open(path, mode, encoding="utf-8")`

- 读写文本时建议**显式** `encoding="utf-8"`，避免 Windows 默认编码与预期不符。

**预期输出形态**（临时文件路径因本机而异）：

```text
写入(mode=w, encoding=utf-8): ...\sample.txt
readlines() -> ['hello\n', 'world\n']
```

---

## 官方文档

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
