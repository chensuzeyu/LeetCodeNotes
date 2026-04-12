"""对应 08-loops.md：for / while 常见循环与遍历模式。"""

from __future__ import annotations

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()

    section("for x in nums：只关心元素")
    nums = [10, 20, 30]
    print("nums =", nums)
    print("依次访问元素:")
    for x in nums:
        print("x =", x)

    section("for _ in range(k)：固定重复 k 次")
    count = 0
    for _ in range(3):
        count += 1
    print("固定循环 3 次后 count =", count)

    section("range(len(nums)) 与 enumerate(nums)")
    nums = [10, 20, 30]
    by_index = []
    for i in range(len(nums)):
        by_index.append(f"i={i}, nums[i]={nums[i]}")
    by_both = []
    for i, x in enumerate(nums):
        by_both.append(f"i={i}, x={x}")
    by_both_from_one = []
    for i, x in enumerate(nums, start=1):
        by_both_from_one.append(f"i={i}, x={x}")
    print("range(len(nums)) ->", by_index)
    print("enumerate(nums) ->", by_both)
    print("enumerate(nums, start=1) ->", by_both_from_one)

    section("zip：并行遍历")
    names = ["Tom", "Amy", "Bob"]
    scores = [90, 95]
    pairs = []
    for name, score in zip(names, scores):
        pairs.append(f"{name}:{score}")
    print("zip(names, scores) ->", pairs)

    section("倒序遍历：reversed(nums) 与 range(..., -1, -1)")
    nums = [10, 20, 30]
    rev_vals = []
    for x in reversed(nums):
        rev_vals.append(x)
    rev_index = []
    for i in range(len(nums) - 1, -1, -1):
        rev_index.append(f"i={i}, nums[i]={nums[i]}")
    print("reversed(nums) ->", rev_vals)
    print("range(len(nums) - 1, -1, -1) ->", rev_index)

    section("遍历字典：for k in d 与 for k, v in d.items()")
    d = {"a": 1, "b": 2}
    only_keys = []
    for k in d:
        only_keys.append(k)
    key_values = []
    for k, v in d.items():
        key_values.append(f"{k}:{v}")
    print("for k in d ->", only_keys)
    print("for k, v in d.items() ->", key_values)

    section("while 条件：二分搜索常见骨架")
    nums = [1, 3, 5, 7, 9]
    target = 7
    left, right = 0, len(nums) - 1
    trace = []
    found = -1
    while left <= right:
        mid = (left + right) // 2
        trace.append(f"l={left}, r={right}, mid={mid}, nums[mid]={nums[mid]}")
        if nums[mid] == target:
            found = mid
            break
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("二分 trace ->", trace)
    print("found index =", found)

    section("break 与 continue")
    seen = []
    for x in [1, 2, 3, 4, 5]:
        if x == 3:
            continue
        seen.append(x)
        if x == 4:
            break
    print("跳过 3，遇到 4 停止 ->", seen)

    section("for ... else：没 break 才进 else")
    for seq in ([1, 3, 5], [1, 4, 5]):
        for x in seq:
            if x % 2 == 0:
                print(f"{seq} -> found {x}")
                break
        else:
            print(f"{seq} -> no even")


if __name__ == "__main__":
    main()
