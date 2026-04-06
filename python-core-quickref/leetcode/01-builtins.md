# 01 · 高频内置函数

完整演示：`scripts/01_builtins.py`  
运行：`python 01_builtins.py`（在 `leetcode/scripts` 目录下）

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

## 与刷题强相关的注意点

- **`sorted` vs `list.sort`**：`list.sort()` 是原地排序，返回 `None`；`sorted(x)` 返回新列表。  
- **`min`/`max` 单参数**：`min(arr)` 是元素最值；`min(arr, b)` 若写成「列表 + 标量」要小心——通常用 `min(arr)` 或 `min(a, b)`。  
- **`zip` 长度不一**：以最短为准，长序列尾部会被丢弃；需要「补齐」时用 `itertools.zip_longest`（见 `04`）。  
- **Top K / 多路归并**：常用 `heapq`（见 `05`）；在**已排序**列表上二分定位见 `bisect`（见 `05`）。  
- **`open`**：写文本时建议显式 `encoding="utf-8"`，避免 Windows 默认编码问题。

## 官方文档

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
