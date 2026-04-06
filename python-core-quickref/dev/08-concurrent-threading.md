# 08 · concurrent.futures / threading（并发入门）

完整演示：`scripts/08_concurrent_threading.py`  
运行：`python 08_concurrent_threading.py`（在 `dev/scripts` 目录下）

**I/O 等待**（读盘、请求网络）常用线程池；**CPU 密集**在 CPython 中线程帮助有限，可考虑 `ProcessPoolExecutor` 或多进程（各有代价）。

## concurrent.futures

| 用法 | 说明 |
|------|------|
| `ThreadPoolExecutor(max_workers=4)` | 线程池；`with` 管理生命周期 |
| `executor.map(fn, iterable)` | 保序、惰性迭代 |
| `future.result(timeout=...)` | 取结果；异常会在此抛出 |

## threading

| 用法 | 说明 |
|------|------|
| `Lock` | 互斥；`with lock:` |
| `Event` | `wait()` / `set()` 简易信号 |

## 官方文档

- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)  
- [threading](https://docs.python.org/3/library/threading.html)
