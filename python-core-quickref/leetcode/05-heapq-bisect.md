# 05 · heapq 与 bisect

完整演示：[scripts/05_heapq_bisect.py](scripts/05_heapq_bisect.py)  
运行：`python3 05_heapq_bisect.py`

下文各「输入代码 / 输出结果」与脚本逐段对应；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## heapq（小顶堆）

| 要点 | 说明 |
|------|------|
| 语义 | `heappop` 总是弹出当前最小元素 |
| 常用 API | `heapify`、`heappush`、`heappop`、`heapreplace`、`nlargest`、`nsmallest` |
| 元组压栈 | `heappush(h, (priority, seq, item))` 可破平手、携带真实数据 |
| 大顶堆 | 压入 `(-x)`；或压入 `(-priority, item)` |

### `heappush` / `heappop` / `heapify` / `heapreplace`

- 堆的内部列表不要求全局有序，但 `h[0]` 永远是当前最小值。
- `heapify` 会**原地**把现有列表改造成堆，时间复杂度通常比一个个 `heappush` 更合适。
- `heapreplace` 会“先弹最小、再压新值”；它适合堆非空且你确定要替换堆顶的场景。

**输入代码**：

```python
h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 2)

data = [9, 5, 7, 1]
heapq.heapify(data)

tmp = [1, 3, 5]
heapq.heapreplace(tmp, 2)
```

**输出结果**：

```text
堆中依次 push 3,1,2 -> list 形态（非全局有序）: [1, 3, 2]
heappop x3 -> 1 2 3
heapify([9,5,7,1]) 后首元素（最小）: 1  整堆: [1, 5, 7, 9]
heapreplace([1,3,5], 2) -> 返回 1  新堆: [2, 3, 5]
```

### 元组破平手

- 堆比较元组时会先比第 0 项；第 0 项相同时再继续比第 1 项。
- 所以刷题里常见 `(priority, seq, item)`：`priority` 决定主顺序，`seq` 用来稳定破平手。

**输入代码**：

```python
h2 = []
heapq.heappush(h2, (2, "b"))
heapq.heappush(h2, (2, "a"))
heapq.heappush(h2, (1, "z"))
[heapq.heappop(h2) for _ in range(len(h2))]
```

**输出结果**：

```text
按 (代价, 附加信息) pop 顺序: [(1, 'z'), (2, 'a'), (2, 'b')]
```

### 用负数模拟大顶堆

- `heapq` 只有小顶堆语义；想取“最大值优先”时，最常见写法就是压入负数。

**输入代码**：

```python
big = [1, 5, 3]
neg_h = [-x for x in big]
heapq.heapify(neg_h)
[-heapq.heappop(neg_h) for _ in range(len(neg_h))]
```

**输出结果**：

```text
原 big = [1, 5, 3]  大顶 pop 等价于 -heappop(neg_h): [5, 3, 1]
```

### `nlargest` / `nsmallest` / `merge`

- `heapq.merge(*iterables)` 要求每个输入序列本身已按升序排列。
- `merge` 返回的是迭代器；不立刻 `list(...)` 时，它会按需逐个产出元素。

**输入代码**：

```python
arr = [3, 1, 4, 1, 5, 9, 2]
heapq.nlargest(3, arr)
heapq.nsmallest(3, arr)
list(heapq.merge([1, 4, 7], [2, 5]))
```

**输出结果**：

```text
arr = [3, 1, 4, 1, 5, 9, 2]
nlargest(3, arr) = [9, 5, 4]
nsmallest(3, arr) = [1, 1, 2]
merge([1,4,7], [2,5]) -> [1, 2, 4, 5, 7]
```

## bisect（有序序列上的二分）

| 函数 | 作用 |
|------|------|
| `bisect_left(a, x)` | 第一个 `>= x` 的下标 |
| `bisect_right` / `bisect` | 第一个 `> x` 的下标（`bisect` 是 `bisect_right` 别名） |
| `insort_left` / `insort` | 在有序列表中原地插入 |

### `bisect_left` / `bisect_right` / `bisect` / `insort_left` / `insort`

- `bisect_left(a, x)` 找的是第一个 `>= x` 的位置；`bisect_right(a, x)` 找的是第一个 `> x` 的位置。
- `bisect(a, x)` 就是 `bisect_right(a, x)` 的别名。
- `insort` 会保持列表有序，但底层仍是 `list.insert`，插入本身不是 O(1)。
- `insort_left` / `insort` 的区别只出现在“要插入的值和现有值相等”时：前者靠左，后者靠右。

**输入代码**：

```python
a_sorted = [1, 2, 2, 2, 6, 7]
x = 2
bisect.bisect_left(a_sorted, x)
bisect.bisect_right(a_sorted, x)
bisect.bisect(a_sorted, x)
bisect.bisect_left(a_sorted, 5)

tmp = [1, 3, 5]
bisect.insort(tmp, 4)
dup = [1, 3, 3, 5]
bisect.insort_left(dup, 3)
bisect.insort(dup, 3)
```

**输出结果**：

```text
a = [1, 2, 2, 2, 6, 7]  x = 2
bisect_left(a, x)  = 1
bisect_right(a, x) = 4
bisect(a, x)       = 4
应插入以保持有序的下标（左/右）即上二值
bisect_left(a, 5)（不存在：落在第一个 >5 或 len）= 4
insort([1,3,5], 4) -> [1, 3, 4, 5]
对重复值 3：bisect_left = 1  bisect = 3
insort_left / insort 后 -> [1, 3, 3, 3, 5] [1, 3, 3, 3, 5] （内容相同，但插入点分别对应 left/right）
```

## 官方文档

- [heapq](https://docs.python.org/3/library/heapq.html)  
- [bisect](https://docs.python.org/3/library/bisect.html)
