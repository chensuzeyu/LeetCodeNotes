"""对应 08-concurrent-threading.md：ThreadPoolExecutor、Lock、Event"""

from __future__ import annotations

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def slow_square(x: int) -> int:
    time.sleep(0.05)
    return x * x


def main() -> None:
    utf8_stdout()
    section("ThreadPoolExecutor：map / as_completed")
    with ThreadPoolExecutor(max_workers=3) as ex:
        mapped = list(ex.map(slow_square, [1, 2, 3, 4]))
        print("map ->", mapped)

    with ThreadPoolExecutor(max_workers=3) as ex:
        futures = [ex.submit(slow_square, i) for i in (5, 6)]
        for fut in as_completed(futures):
            print("done:", fut.result())

    section("threading：Lock / Event")
    lock = threading.Lock()
    counter = {"n": 0}

    def bump() -> None:
        for _ in range(1000):
            with lock:
                counter["n"] += 1

    t1 = threading.Thread(target=bump)
    t2 = threading.Thread(target=bump)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Lock 后 counter =", counter["n"])

    evt = threading.Event()

    def waiter() -> None:
        evt.wait(timeout=2)
        print("Event 已收到信号")

    th = threading.Thread(target=waiter)
    th.start()
    time.sleep(0.05)
    evt.set()
    th.join()


if __name__ == "__main__":
    main()
