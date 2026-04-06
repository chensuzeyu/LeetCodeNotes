# 05 · heapq 与 bisect

完整演示：`scripts/05_heapq_bisect.py`  
运行：`python 05_heapq_bisect.py`

## heapq（小顶堆）

| 要点 | 说明 |
|------|------|
| 语义 | **最小堆**：`heappop` 总是弹出当前最小元素 |
| 常用 API | `heapify`、`heappush`、`heappop`、`heapreplace`、`nlargest`、`nsmallest` |
| 元组压栈 | `heappush(h, (priority, seq, item))` 用多余字段**破平手**、携带真实数据 |
| 大顶堆 | 压入 `(-x)`；或压入 `(-priority, item)`，等价于「按原 key 取最大」 |

多路归并可用 `heapq.merge(*iterables)`（各序列需**已排序**，惰性迭代）。

## bisect（有序序列上的二分）

| 函数 | 作用 |
|------|------|
| `bisect_left(a, x)` | 在有序列表 `a` 中，`x` 应插在左侧以保持有序 → **第一个 `>= x` 的下标**（若全 `< x` 则 `len(a)`） |
| `bisect_right` / `bisect` | 插右侧 → **第一个 `> x` 的下标** |
| `insort_left` / `insort` | 在插入位置**原地**插入（比手写 `list.insert` 找位更语义化） |

前提一般是 **`a` 已按升序**；降序题可手写二分或对 key 取反后再想映射。

## 官方文档

- [heapq](https://docs.python.org/3/library/heapq.html)  
- [bisect](https://docs.python.org/3/library/bisect.html)
