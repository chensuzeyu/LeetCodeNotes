# 08 · concurrent.futures / threading（并发入门）

完整演示：[scripts/08_concurrent_threading.py](scripts/08_concurrent_threading.py)  
运行：`python 08_concurrent_threading.py`（在 `dev/scripts` 目录）

**I/O 等待**（读盘、请求网络）常用线程池；**CPU 密集**在 CPython 中线程帮助有限，可考虑 `ProcessPoolExecutor` 或多进程（各有代价）。  
下文「输入输出示例」与脚本 **一一对应**；`as_completed` 打印顺序**随任务完成先后而变**（见 [../README.md](../README.md) 维护约定）。

## concurrent.futures

| 用法 | 说明 |
|------|------|
| `ThreadPoolExecutor(max_workers=4)` | 线程池；`with` 管理生命周期 |
| `executor.map(fn, iterable)` | **保序**、惰性迭代；结果是按输入顺序 |
| `as_completed(futures)` | **谁先完成谁先回调**；打印顺序不一定与提交顺序一致 |
| `future.result(timeout=...)` | 取结果；异常会在此抛出 |

**输入输出示例**

**输入**（`08_concurrent_threading.py`）：

```python
def slow_square(x: int) -> int:
    time.sleep(0.05)
    return x * x

with ThreadPoolExecutor(max_workers=3) as ex:
    list(ex.map(slow_square, [1, 2, 3, 4]))

with ThreadPoolExecutor(max_workers=3) as ex:
    futures = [ex.submit(slow_square, i) for i in (5, 6)]
    for fut in as_completed(futures):
        fut.result(timeout=2)
```

**输出**（`stdout`；`done` 两行顺序可能为 `25` / `36` 互换）：

```text
map -> [1, 4, 9, 16]
done: 36
done: 25
```

## threading

| 用法 | 说明 |
|------|------|
| `Lock` | 互斥；`with lock:` |
| `Event` | `wait()` / `set()` 简易信号 |

**输入输出示例**

**输入**（`08_concurrent_threading.py`）：

```python
# 两线程各 bump 1000 次，with lock: counter["n"] += 1
# Event：waiter 线程 evt.wait(timeout=2)；主线程 sleep(0.05) 后 evt.set()
```

**输出**（`stdout`）：

```text
Lock 后 counter = 2000
Event 已收到信号
```

## 官方文档

- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)  
- [threading](https://docs.python.org/3/library/threading.html)
