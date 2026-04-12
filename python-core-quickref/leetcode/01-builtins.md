# 01 · 高频内置函数

完整演示：[scripts/01_builtins.py](scripts/01_builtins.py)  
运行：`python3 01_builtins.py`（在 `leetcode/scripts` 目录下）

下文各「输入代码 / 输出结果」与脚本逐段对应；若你改动了脚本，请同步更新本文对应块（见上层 [README.md 维护约定](../README.md)）。

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

## `len` / `range`

- `range(a, b)` 生成从 `a` 到 `b - 1` 的整数，**不含** `b`。
- `range(stop)` 等价于 `range(0, stop)`；`step` 可为负。

**输入代码**：

```python
nums = [2, 7, 11, 15]
len(nums)
list(range(len(nums)))
list(range(1, 4))
list(range(4, 1, -1))
```

**输出结果**：

```text
nums = [2, 7, 11, 15]
len(nums) = 4
list(range(len(nums))) = [0, 1, 2, 3]
list(range(1, 4)) = range(a,b) -> [1, 2, 3]
list(range(4, 1, -1)) = step=-1 -> [4, 3, 2]
```

## `enumerate(iterable, start=0)`

- `start` 是计数起点，默认 `0`。

**输入代码**：

```python
items = ["a", "b", "c"]
for start in (0, 1, 2):
    for i, x in enumerate(items, start=start):
        ...
```

**输出结果**（`!r` 为 `repr`，字符串会带引号）：

```text
items = ['a', 'b', 'c']
  start=0:
    i=0, x='a'
    i=1, x='b'
    i=2, x='c'
  start=1:
    i=1, x='a'
    i=2, x='b'
    i=3, x='c'
  start=2:
    i=2, x='a'
    i=3, x='b'
    i=4, x='c'
```

## `zip(*iterables)`

- 并行遍历多条序列，每次得到一个元组。
- 长度以最短序列为准；较长序列尾部会被丢弃。

**输入代码**：

```python
a = [1, 2, 3]
b = [10, 20]
list(zip(a, b))
```

**输出结果**：

```text
a = [1, 2, 3]  b = [10, 20]
list(zip(a, b)) = [(1, 10), (2, 20)]
for i, j in zip(a, b): (1+10) (2+20)
```

## `sorted` / `list.sort`

- `sorted(...)` 返回新列表，不修改原对象。
- `list.sort()` 原地排序，返回 `None`。
- 两者默认都是**升序**；想从大到小排可传 `reverse=True`。
- `key=f` 表示：排序前先对每个元素算一次 `f(元素)`，再按这个结果比较。
- `lambda x: ...` 是匿名小函数，刷题里很常见，常配合 `key=` / `min(..., key=...)` / `max(..., key=...)` 使用。

**输入代码**：

```python
arr = [3, 1, 4, 1, 5]
sorted(arr)
arr.sort()

words = ["bb", "a", "ccc"]
sorted(words, key=len)
students = [
    {"name": "Tom", "age": 18},
    {"name": "Amy", "age": 16},
    {"name": "Bob", "age": 17},
]
sorted(students, key=lambda x: x["age"])
sorted(arr, reverse=True)
```

**输出结果**：

```text
原 arr = [3, 1, 4, 1, 5]
sorted(arr) -> [1, 1, 3, 4, 5]  原 arr 仍为 [3, 1, 4, 1, 5]
arr.sort() 后 arr = [1, 1, 3, 4, 5] （list.sort 原地排序，返回 None）
sorted(words, key=len) -> ['a', 'bb', 'ccc']
sorted(students, key=lambda x: x['age']) -> [{'name': 'Amy', 'age': 16}, {'name': 'Bob', 'age': 17}, {'name': 'Tom', 'age': 18}]
sorted(arr, reverse=True) -> [5, 4, 3, 1, 1]
```

速记：`lambda x: x["age"]` 等价于

```python
def get_age(x):
    return x["age"]
```

## `min` / `max`

- `min(5, 2, 8)` 是多标量比较。
- `min([5, 2, 8])` 是在单个序列里找最小值。
- 对元组，`min(pairs)` 默认按**逐项比较**：先比第 0 位，再比第 1 位。
- 所以 `min(pairs)` **不完全等价于** `min(pairs, key=lambda p: p[0])`；若第 0 位相同，前者会继续看第 1 位，后者只看第 0 位并保留先出现的元素。

**输入代码**：

```python
pairs = [(1, 9), (5, 2), (3, 7)]
pairs_lex = [(1, 8), (1, 9), (5, 2), (3, 7)]
pairs_tie = [(1, 9), (1, 8), (5, 2), (3, 7)]
min(pairs)
min(pairs_lex)
min(pairs_lex, key=lambda p: p[0])
min(pairs_tie)
min(pairs_tie, key=lambda p: p[0])
min(pairs, key=lambda p: p[1])
min(5, 2, 8)
min([5, 2, 8])
```

**输出结果**：

```text
pairs = [(1, 9), (5, 2), (3, 7)]
pairs_lex = [(1, 8), (1, 9), (5, 2), (3, 7)]
min(pairs) = (1, 9)
pairs_lex 中，(1, 8) < (1, 9)（先比第 0 位，相同再比第 1 位）
min(pairs_lex) = (1, 8)
min(pairs_lex, key=lambda p: p[0]) = (1, 8)
pairs_tie = [(1, 9), (1, 8), (5, 2), (3, 7)]
min(pairs_tie) = (1, 8)
min(pairs_tie, key=lambda p: p[0]) = (1, 9)
min(pairs, key=lambda p: p[1]) = (5, 2)
min(5, 2, 8) = 2
min([5, 2, 8]) = 2
```

## `sum(iterable, start=0)`

- `start` 是初始累加值；
  - 空序列：直接返回 start；
  - 非空序列：返回 start + 每个元素依次累加。

**输入代码**：

```python
sum([1, 2, 3])
sum([], start=10)
```

**输出结果**：

```text
sum([1, 2, 3]) = 6
sum([], start=10) = 10
```

## `any` / `all`

- `any`：只要有一个真值，就返回 `True`；常用于判断 “是否存在一个满足条件的元素”。
- `all`：只有全部都是真值，才返回 `True`；常用于判断 “是否全部满足条件”。
- `any` 遇到第一个真值即停止；`all` 遇到第一个假值即停止。
- 常见假值有：`False`、`0`、`None`、`""`、`[]`；其他很多非空对象通常都算真值。

**输入代码**：

```python
any([False, False, True])
any([False, False])
all([1, 2, 3])
all([1, 2, 0])
```

**输出结果**：

```text
any([False, False, True]) = True
any([False, False]) = False
all([1, 2, 3]) = True
all([1, 2, 0]) = False
```

## `open(path, mode, encoding="utf-8")`

- `utf-8` 是一种**文本编码规则**，可以理解成“程序怎样把文字变成字节保存到文件里，以及再怎样从字节还原回文字”。现在它几乎是最通用的文本编码；显式写上 `encoding="utf-8"`，能减少中文乱码。
- `with open(...) as f:` 可以理解为“打开文件，暂时命名为 `f` 来使用”；离开 `with` 代码块后，文件会自动关闭。
- 如果不用 `with`，通常就要自己手动写 `f.close()`；忘记关文件时，可能会出现资源没及时释放、内容没及时刷到磁盘、Windows 下文件暂时被占用等问题。
- 本课示例会把文件写到仓库内固定学习目录 `.tmp/leetcode/sample.txt`，方便运行后直接查看；该目录已加入根 `.gitignore`。
- 这一节把路径准备过程也直接展开写出来，方便你把脚本和讲义逐行对照着看。
- 其中 `resolve()` 可以先理解成“把当前文件路径变成完整的绝对路径”；`parents[2]` 可以先理解成“再往上回退两级目录”；parents[0] 是“当前文件所在目录”。
- `Path(...) / "a" / "b"` 这种写法是在拼路径；它会按当前系统自动使用合适的路径分隔符，所以 Windows 和 Linux 都能用。
- `mkdir(parents=True, exist_ok=True)` 可以先记成：需要的话就把目录建出来；如果目录已经存在，也不要报错。
- 这些写法**不只适用于 Windows**。`with`、`open(...)`、`encoding="utf-8"` 这些都是 Python 的跨平台基础用法，在 Linux / macOS 下同样成立。
- 真正常见的差异主要有三类：
  - 路径显示：Windows 常见 `\`，Linux / macOS 常见 `/`；但示例里用的是 `Path` 拼路径，写法本身可以跨平台。
  - 默认编码：如果你不写 `encoding=...`，不同系统和环境的默认值可能不同；显式写 `encoding="utf-8"` 就更稳。
  - 换行符：本例写了 `newline="\n"`，表示按 `\n` 写入文本，这样在不同系统上更一致。

**输入代码**：

```python
# __file__ 是当前脚本自己的路径(含脚本名)；resolve() 把它变成绝对路径
script_path = Path(__file__).resolve()
print("script_path =", script_path)
# parents[2] 表示向上退两级：scripts -> leetcode -> python-core-quickref
project_root = script_path.parents[2]
print("project_root =", project_root)
# 用 / 拼路径；Path 会按当前系统自动处理分隔符
sample_dir = project_root / ".tmp" / "leetcode"
print("sample_dir =", sample_dir)
# 若目录不存在就创建；已存在也不报错
sample_dir.mkdir(parents=True, exist_ok=True)
print("sample_dir.exists() =", sample_dir.exists())
sample_file = sample_dir / "sample.txt"
print("sample_file =", sample_file)

# "w" 表示写入：文件不存在就新建，已存在就覆盖原内容
# encoding="utf-8" 表示按 UTF-8 规则保存文本，尽量避免中文乱码
# newline="\n" 表示按 \n 写入换行，让不同系统下的结果更一致
with open(sample_file, "w", encoding="utf-8", newline="\n") as f:
    f.write("hello\nworld\n")
print("写入(mode=w, encoding=utf-8):", sample_file)
print("sample_file.exists() =", sample_file.exists())

# with 结束后文件会自动关闭；这里再重新打开一遍看看文件内容
with open(sample_file, encoding="utf-8") as f:
    lines = f.readlines()
print("readlines() ->", lines)
```

**输出结果**（`<PROJECT_ROOT>` 为 `python-core-quickref` 根目录，因本机而异）：

```text
script_path = <PROJECT_ROOT>/leetcode/scripts/01_builtins.py
project_root = <PROJECT_ROOT>
sample_dir = <PROJECT_ROOT>/.tmp/leetcode
sample_dir.exists() = True
sample_file = <PROJECT_ROOT>/.tmp/leetcode/sample.txt
写入(mode=w, encoding=utf-8): <PROJECT_ROOT>/.tmp/leetcode/sample.txt
sample_file.exists() = True
readlines() -> ['hello\n', 'world\n']
```

## 官方文档

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
