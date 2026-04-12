# 08 · 循环与遍历模式

完整演示：[scripts/08_loops.py](scripts/08_loops.py)  
运行：`python3 08_loops.py`（在 `leetcode/scripts` 目录）

下文各「输入代码 / 输出结果」与脚本逐段对应；若你改动了脚本，请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## 速查表

| 写法 | 什么时候用 |
|------|------------|
| `for x in nums` | 只关心元素，不关心下标 |
| `for _ in range(k)` | 固定重复 `k` 次 |
| `for i in range(len(nums))` | 需要下标，或要访问 / 修改 `nums[i]` |
| `for i, x in enumerate(nums)` | 同时需要下标和值 |
| `for a, b in zip(A, B)` | 并行遍历多条序列 |
| `for x in reversed(nums)` | 倒序遍历元素 |
| `for i in range(len(nums) - 1, -1, -1)` | 倒序遍历下标 |
| `for k, v in d.items()` | 遍历字典键值 |
| `while 条件:` | 次数不固定；双指针、二分常用 |
| `break` / `continue` | 提前结束 / 跳过本轮 |
| `for ... else` | 只有**没被 `break` 打断**才进 `else` |

## `for x in nums`

- 这是最基本的遍历写法：只拿元素，不拿下标。
- 如果循环体里根本用不到位置编号，优先写这种最直接的形式。

**输入代码**：

```python
nums = [10, 20, 30]
for x in nums:
    print("x =", x)
```

**输出结果**：

```text
nums = [10, 20, 30]
依次访问元素:
x = 10
x = 20
x = 30
```

## `for _ in range(k)`

- `_` 表示“这个变量我不会用到”，常见于“固定做几次”。

**输入代码**：

```python
count = 0
for _ in range(3):
    count += 1
```

**输出结果**：

```text
固定循环 3 次后 count = 3
```

## `range(len(nums))` 与 `enumerate(nums)`

- `range(len(nums))`：适合“必须按下标访问”的情况。
- `enumerate(nums)`：适合“下标和值都要”的情况，通常更直观。
- 只为了拿下标去反查元素时，先想想 `enumerate` 会不会更清晰。
- `enumerate(nums, start=1)` 常用于题目里的“第 1 个、第 2 个”这种自然编号。

**输入代码**：

```python
nums = [10, 20, 30]

for i in range(len(nums)):
    print(i, nums[i])

for i, x in enumerate(nums):
    print(i, x)

for i, x in enumerate(nums, start=1):
    print(i, x)
```

**输出结果**：

```text
range(len(nums)) -> ['i=0, nums[i]=10', 'i=1, nums[i]=20', 'i=2, nums[i]=30']
enumerate(nums) -> ['i=0, x=10', 'i=1, x=20', 'i=2, x=30']
enumerate(nums, start=1) -> ['i=1, x=10', 'i=2, x=20', 'i=3, x=30']
```

## `zip(A, B)`

- 适合并行遍历；长度以较短序列为准。
- 如果两列长度可能不一致，先确认“截断长列尾巴”是不是你想要的行为。

**输入代码**：

```python
names = ["Tom", "Amy", "Bob"]
scores = [90, 95]
for name, score in zip(names, scores):
    print(name, score)
```

**输出结果**：

```text
zip(names, scores) -> ['Tom:90', 'Amy:95']  （较长的 names 尾部 'Bob' 被截断）
```

## 倒序遍历：`reversed(nums)` 与 `range(..., -1, -1)`

- `reversed(nums)`：只关心倒序后的元素。
- `range(len(nums) - 1, -1, -1)`：需要倒序下标时常用。

**输入代码**：

```python
nums = [10, 20, 30]

for x in reversed(nums):
    print(x)

for i in range(len(nums) - 1, -1, -1):
    print(i, nums[i])
```

**输出结果**：

```text
reversed(nums) -> [30, 20, 10]
range(len(nums) - 1, -1, -1) -> ['i=2, nums[i]=30', 'i=1, nums[i]=20', 'i=0, nums[i]=10']
```

## 遍历字典：`for k in d` 与 `for k, v in d.items()`

- `for k in d`：只拿键。
- `for k, v in d.items()`：同时拿键和值。

**输入代码**：

```python
d = {"a": 1, "b": 2}

for k in d:
    print(k)

for k, v in d.items():
    print(k, v)
```

**输出结果**：

```text
for k in d -> ['a', 'b']
for k, v in d.items() -> ['a:1', 'b:2']
```

## `while 条件:`

- `for` 更像“把一个序列走完”。
- `while` 更像“条件还成立就继续”，二分、快慢指针、滑动窗口里常见。

**输入代码**：

```python
nums = [1, 3, 5, 7, 9]
target = 7
left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

**输出结果**：

```text
二分 trace -> ['l=0, r=4, mid=2, nums[mid]=5', 'l=3, r=4, mid=3, nums[mid]=7']
found index = 3
```

## `break` 与 `continue`

- `continue`：跳过本轮后面的代码，直接进入下一轮。
- `break`：整个循环立即结束。

**输入代码**：

```python
seen = []
for x in [1, 2, 3, 4, 5]:
    if x == 3:
        continue
    seen.append(x)
    if x == 4:
        break
```

**输出结果**：

```text
跳过 3，遇到 4 停止 -> [1, 2, 4]
```

## `for ... else`

- `else` 只有在循环**正常结束**时才执行。
- 只要中途发生了 `break`，就**不会**进 `else`。

**输入代码**：

```python
for x in [1, 3, 5]:
    if x % 2 == 0:
        print("found")
        break
else:
    print("no even")

for x in [1, 4, 5]:
    if x % 2 == 0:
        print("found")
        break
else:
    print("no even")
```

**输出结果**：

```text
[1, 3, 5] -> no even
[1, 4, 5] -> found 4
```

## 什么时候优先用哪种

- 只关心元素：`for x in nums`
- 只关心次数：`for _ in range(k)`
- 关心下标：`for i in range(len(nums))`
- 下标和值都要：`enumerate(nums)`
- 两列一起走：`zip(A, B)`
- 倒序：`reversed(nums)` 或 `range(..., -1, -1)`
- 条件控制、次数不固定：`while`
