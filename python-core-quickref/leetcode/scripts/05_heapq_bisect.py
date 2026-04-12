"""对应 05-heapq-bisect.md：heapq、bisect"""

from __future__ import annotations

import bisect
import heapq

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("heapq：heappush / heappop / heapify / heapreplace")
    h: list[int] = []
    heapq.heappush(h, 3)
    heapq.heappush(h, 1)
    heapq.heappush(h, 2)
    print("堆中依次 push 3,1,2 -> list 形态（非全局有序）:", h)
    print("heappop x3 ->", heapq.heappop(h), heapq.heappop(h), heapq.heappop(h))

    data = [9, 5, 7, 1]
    heapq.heapify(data)
    print("heapify([9,5,7,1]) 后首元素（最小）:", data[0], " 整堆:", data)
    tmp2 = [1, 3, 5]
    removed = heapq.heapreplace(tmp2, 2)
    print("heapreplace([1,3,5], 2) -> 返回", removed, " 新堆:", tmp2)

    section("heapq：元组破平手（先比较第一域）")
    h2: list[tuple[int, str]] = []
    heapq.heappush(h2, (2, "b"))
    heapq.heappush(h2, (2, "a"))
    heapq.heappush(h2, (1, "z"))
    print("按 (代价, 附加信息) pop 顺序:", [heapq.heappop(h2) for _ in range(len(h2))])

    section("heapq：用负数模拟大顶堆（单元素键）")
    big = [1, 5, 3]
    neg_h = [-x for x in big]
    heapq.heapify(neg_h)
    print("原 big =", big, " 大顶 pop 等价于 -heappop(neg_h):", [-heapq.heappop(neg_h) for _ in range(len(neg_h))])

    section("nlargest / nsmallest")
    arr = [3, 1, 4, 1, 5, 9, 2]
    print("arr =", arr)
    print("nlargest(3, arr) =", heapq.nlargest(3, arr))
    print("nsmallest(3, arr) =", heapq.nsmallest(3, arr))

    section("heapq.merge：多路有序迭代器（惰性）")
    a = [1, 4, 7]
    b = [2, 5]
    print("merge([1,4,7], [2,5]) ->", list(heapq.merge(a, b)))

    section("bisect：left / right / insort（升序列表）")
    a_sorted = [1, 2, 2, 2, 6, 7]
    x = 2
    print("a =", a_sorted, " x =", x)
    print("bisect_left(a, x)  =", bisect.bisect_left(a_sorted, x))
    print("bisect_right(a, x) =", bisect.bisect_right(a_sorted, x))
    print("bisect(a, x)       =", bisect.bisect(a_sorted, x))
    print("应插入以保持有序的下标（左/右）即上二值")

    y = 5
    print("bisect_left(a, 5)（不存在：落在第一个 >5 或 len）=", bisect.bisect_left(a_sorted, y))

    tmp = [1, 3, 5]
    bisect.insort(tmp, 4)
    print("insort([1,3,5], 4) ->", tmp)
    dup = [1, 3, 3, 5]
    dup_left = dup.copy()
    dup_right = dup.copy()
    bisect.insort_left(dup_left, 3)
    bisect.insort(dup_right, 3)
    print("对重复值 3：bisect_left =", bisect.bisect_left(dup, 3), " bisect =", bisect.bisect(dup, 3))
    print("insort_left / insort 后 ->", dup_left, dup_right, "（内容相同，但插入点分别对应 left/right）")


if __name__ == "__main__":
    main()
