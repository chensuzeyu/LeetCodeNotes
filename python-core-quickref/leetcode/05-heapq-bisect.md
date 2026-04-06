# 05 · heapq 与 bisect

完整演示：[scripts/05_heapq_bisect.py](scripts/05_heapq_bisect.py)  
运行：`python 05_heapq_bisect.py`

下文「预期输出」与脚本一致；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## heapq（小顶堆）

| 要点 | 说明 |
|------|------|
| 语义 | **最小堆**：`heappop` 总是弹出当前最小元素 |
| 常用 API | `heapify`、`heappush`、`heappop`、`heapreplace`、`nlargest`、`nsmallest` |
| 元组压栈 | `heappush(h, (priority, seq, item))` 用多余字段**破平手**、携带真实数据 |
| 大顶堆 | 压入 `(-x)`；或压入 `(-priority, item)`，等价于「按原 key 取最大」 |

### 堆列表形态与 `heapify`

- 内部用列表存堆，**整体不一定升序**；**`h[0]`** 始终是当前最小元。

**预期输出摘录**：

```text
堆中依次 push 3,1,2 -> list 形态（非全局有序）: [1, 3, 2]
heappop x3 -> 1 2 3
heapify([9,5,7,1]) 后首元素（最小）: 1  整堆: [1, 5, 7, 9]
```

### 元组破平手

```text
按 (代价, 附加信息) pop 顺序: [(1, 'z'), (2, 'a'), (2, 'b')]
```

### 用负数模拟大顶堆（单键）

```text
原 big = [1, 5, 3]  大顶 pop 等价于 -heappop(neg_h): [5, 3, 1]
```

### `nlargest` / `nsmallest` / `merge`

- **`heapq.merge(*iterables)`**：各输入序列须**已排序**，结果惰性合并为有序迭代。

**预期输出摘录**：

```text
nlargest(3, arr) = [9, 5, 4]
nsmallest(3, arr) = [1, 1, 2]
merge([1,4,7], [2,5]) -> [1, 2, 4, 5, 7]
```

## bisect（有序序列上的二分）

| 函数 | 作用 |
|------|------|
| `bisect_left(a, x)` | 在升序列表 `a` 中，`x` 插在左侧以保持有序 → **第一个 `>= x` 的下标**（若全 `< x` 则 `len(a)`） |
| `bisect_right` / `bisect` | 插右侧 → **第一个 `> x` 的下标** |
| `insort_left` / `insort` | 在插入位置**原地**插入（比手写 `list.insert` 找位更语义化） |

前提一般是 **`a` 已按升序**；降序题可手写二分或对 key 取反后再想映射。

**预期输出摘录**：

```text
a = [1, 2, 2, 2, 6, 7]  x = 2
bisect_left(a, x)  = 1
bisect_right(a, x) = 4
bisect_left(a, 5)（不存在：落在第一个 >5 或 len）= 4
insort([1,3,5], 4) -> [1, 3, 4, 5]
```

## 官方文档

- [heapq](https://docs.python.org/3/library/heapq.html)  
- [bisect](https://docs.python.org/3/library/bisect.html)
