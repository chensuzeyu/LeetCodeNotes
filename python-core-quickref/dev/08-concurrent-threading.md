# 08 · concurrent.futures / threading（并发入门）

完整演示：[scripts/08_concurrent_threading.py](scripts/08_concurrent_threading.py)  
运行：`python 08_concurrent_threading.py`（在 `dev/scripts` 目录）

**I/O 等待**（读盘、请求网络）常用线程池；**CPU 密集**在 CPython 中线程帮助有限，可考虑 `ProcessPoolExecutor` 或多进程（各有代价）。  
下文「预期输出」与脚本一致；`as_completed` 打印顺序**随任务完成先后而变**（见 [../README.md](../README.md) 维护约定）。

## concurrent.futures

| 用法 | 说明 |
|------|------|
| `ThreadPoolExecutor(max_workers=4)` | 线程池；`with` 管理生命周期 |
| `executor.map(fn, iterable)` | **保序**、惰性迭代；结果是按输入顺序 |
| `as_completed(futures)` | **谁先完成谁先回调**；打印顺序不一定与提交顺序一致 |
| `future.result(timeout=...)` | 取结果；异常会在此抛出 |

**预期输出摘录**：

```text
map -> [1, 4, 9, 16]
done: 36
done: 25
```

（`done` 两行顺序可能为 `25` 先于 `36`，取决于调度。）

## threading

| 用法 | 说明 |
|------|------|
| `Lock` | 互斥；`with lock:` |
| `Event` | `wait()` / `set()` 简易信号 |

**预期输出摘录**：

```text
Lock 后 counter = 2000
Event 已收到信号
```

## 官方文档

- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)  
- [threading](https://docs.python.org/3/library/threading.html)
