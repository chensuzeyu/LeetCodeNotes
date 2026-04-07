# 08 · concurrent.futures / threading（并发入门）

完整演示：[scripts/08_concurrent_threading.py](scripts/08_concurrent_threading.py)  
运行：`python3 08_concurrent_threading.py`（在 `dev/scripts` 目录）

I/O 等待场景常用线程池；线程间共享状态则需要最小限度的同步原语。  
下文各「输入代码 / 输出结果」与脚本逐段对应；`as_completed(...)` 的完成顺序不固定，可写作 `<DONE_A>` / `<DONE_B>` 两种排列。

## concurrent.futures

| 用法 | 说明 |
|------|------|
| `ThreadPoolExecutor(max_workers=4)` | 线程池；`with` 自动管理生命周期 |
| `executor.map(fn, iterable)` | 保序返回结果 |
| `as_completed(futures)` | 谁先完成先返回 |
| `future.result(timeout=...)` | 取结果；异常会在这里抛出 |

### `map(...)` 与 `as_completed(...)`

**输入代码**：

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

**输出结果**（`stdout`）：

```text
map -> [1, 4, 9, 16]
done: 25
done: 36
```

或

```text
map -> [1, 4, 9, 16]
done: 36
done: 25
```

## threading

| 用法 | 说明 |
|------|------|
| `Lock` | 互斥；建议配合 `with lock:` |
| `Event` | `wait()` / `set()` 做简易信号同步 |

### `Lock` 与 `Event`

**输入代码**：

```python
lock = threading.Lock()
counter = {"n": 0}

def bump() -> None:
    for _ in range(1000):
        with lock:
            counter["n"] += 1

evt = threading.Event()
```

**输出结果**（`stdout`）：

```text
Lock 后 counter = 2000
Event 已收到信号
```

## 官方文档

- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)  
- [threading](https://docs.python.org/3/library/threading.html)
