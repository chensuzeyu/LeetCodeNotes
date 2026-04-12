# 02 · 容器常用方法（list / tuple / dict / str / set）

完整演示：[scripts/02_containers.py](scripts/02_containers.py)  
运行：`python3 02_containers.py`（在 `leetcode/scripts` 目录）

下文各「输入代码 / 输出结果」与脚本逐段对应；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。  
为稳定展示，`set` 相关结果统一在脚本里用 `sorted(...)` 打印。

## list

| 方法 / 写法 | 作用 |
|-------------|------|
| `append(x)` | 尾部加入一个元素 |
| `extend(iterable)` | 在末尾一次性追加多个元素 |
| `pop()` / `pop(i)` | 弹出末尾或下标 `i` |
| `remove(x)` | 删除第一个匹配值，找不到会报 `ValueError` |
| `insert(i, x)` | 在位置 `i` 插入 |
| `reverse()` | 原地反转列表，返回 `None` |
| `clear()` | 清空列表 |
| `nums[i:j]` | 切片，**左闭右开** |
| `nums[i:j:step]` | 带步长切片；可隔位取值 |
| `nums[::-1]` | 反转副本（新序列） |

### `append(x)` 与 `extend(iterable)`

- `append(x)` 是“把 **x 整个对象** 追加进去”；如果 `x` 本身是列表，也会作为**一个元素**放进去。
- `extend(iterable)` 是“把 iterable 里的元素**逐个展开**后追加进去”。

**输入代码**（`02_containers.py`）：

```python
nums = [1, 2]
nums.append(3)
nums_append = [1, 2]
nums_append.append([4, 5])
nums.extend([4, 5])
```

**输出结果**（`stdout`）：

```text
append(3) -> [1, 2, 3]
append([4, 5]) -> [1, 2, [4, 5]]
extend([4, 5]) -> [1, 2, 3, 4, 5]
```

### `pop()` 与 `pop(i)`

- `pop()` / `pop(i)` 都是**按下标删除**，并且**返回被删掉的值**。
- `pop()` 默认删最后一个元素；`pop(i)` 删第 `i` 个元素。
- 下标越界会报 `IndexError`。

**输入代码**：

```python
last = nums.pop()
mid = nums.pop(1)
nums.pop(99)
```

**输出结果**：

```text
pop() -> 5  nums -> [1, 2, 3, 4]
pop(1) -> 2  nums -> [1, 3, 4]
pop(99) -> IndexError: pop index out of range
```

### `remove(x)` 与 `insert(i, x)`

- `remove(x)` 是**按值删除**，不是按下标删除。
- 它只会删掉**第一个**匹配到的值；后面相同的值不会一次性全删掉。
- `remove()` 只接受**一个参数**；如果想删多个值，通常用循环或列表推导。

**输入代码**：

```python
removed = [1, 4, 4, 2]
removed.remove(4)
removed.remove(4)
removed.remove(99)
removed.remove(1, 2)
removed.insert(1, 8)
```

**输出结果**：

```text
初始 removed = [1, 4, 4, 2]
remove(4) -> [1, 4, 2]
再次 remove(4) -> [1, 2]
remove(99) -> ValueError: list.remove(x): x not in list
remove(1, 2) -> TypeError: list.remove() takes exactly one argument (2 given)
insert(1, 8) -> [1, 8, 2]
```

### `reverse()` 与 `clear()`

- `reverse()` 是**原地修改**列表，返回值是 `None`。
- `clear()` 会把列表清空。

**输入代码**：

```python
rev = [9, 2, 3]
reverse_result = rev.reverse()
cleared = [7, 8]
cleared.clear()
```

**输出结果**：

```text
rev.reverse() 返回 -> None  rev -> [3, 2, 9]
clear() 后 -> []
```

### `nums[i:j]` / `nums[i:j:step]` 与 `nums[::-1]`

- `nums[i:j]` 含 `i`，**不含** `j`；省略端点表示从头到尾。
- 第三个参数 `step` 表示步长；`nums[::2]` 就是“从头到尾，每隔 2 个位置取一个”。
- 切片会返回**新列表**；`nums[::-1]` 也是新列表，原列表不变。

**输入代码**：

```python
sliced = [9, 2, 3, 4]
sliced[1:3]
sliced[::2]
sliced[::-1]
```

**输出结果**：

```text
nums[1:3]（左闭右开）-> [2, 3]
nums[::2]（step=2）-> [9, 3]
nums[::-1]（新序列，原列表不变）-> [4, 3, 2, 9]  原 nums = [9, 2, 3, 4]
```

### `list` 与 `tuple`

- `[]` 是 **list**，可修改；`()` 是 **tuple**，通常表示固定记录，不可原地改元素。
- 在 `min([[1, 9], [5, 2], [3, 7]])` 这类场景里，**换成列表也能比**；列表和元组都按逐项比较。
- 刷题里若只是临时存一组固定值，常写成 tuple；若后面还要改内容，用 list 更自然。

**输入代码**：

```python
pairs_tuple = [(1, 9), (5, 2), (3, 7)]
pairs_list = [[1, 9], [5, 2], [3, 7]]
min(pairs_tuple)
min(pairs_list)
pairs_list[0][0] = 8
t = (1, 9)
t[0] = 8
```

**输出结果**：

```text
min([(1, 9), (5, 2), (3, 7)]) -> (1, 9)
min([[1, 9], [5, 2], [3, 7]]) -> [1, 9]
列表可改：pairs_list[0][0] = 8 后 -> [[8, 9], [5, 2], [3, 7]]
元组不可改：t[0] = 8 -> TypeError: 'tuple' object does not support item assignment
```

## dict

| 方法 / 写法 | 作用 |
|-------------|------|
| `d[key]` | 读；键不存在会 `KeyError` |
| `d.get(key, default)` | 安全读取，带默认值 |
| `d.setdefault(key, default)` | 无则插入再返回 |
| `d.pop(key[, default])` | 删除并返回值；可选默认值避免 `KeyError` |
| `d.popitem()` | 删除并返回最后插入的一对 `(key, value)` |
| `d.update(mapping)` | 批量更新键值 |
| `d.keys()` | 返回所有键 |
| `d.values()` | 返回所有值 |
| `d.items()` | 返回键值对 |
| `d.copy()` | 浅拷贝 |
| `d.clear()` | 清空字典 |
| `key in d` | 判断是否含有键 |
| `for k, v in d.items()` | 遍历键值 |

### `[]` 与 `get` / `setdefault`

- `d[k]`：键不存在时抛 **`KeyError`**，适合“键必定存在”的路径。
- `d.get(k, default)`：缺失时返回 `default`，**不修改**字典。
- `d.setdefault(k, default)`：缺失时写入 `default` 再返回；如果键已存在，就返回旧值，**不会覆盖原值**。

### `d[key]`、`get`、`setdefault` 与 `key in d`

**输入代码**：

```python
d = {"a": 1}
d["a"]
d["missing"]
d.get("b", 0)
d.setdefault("a", 99)
d.setdefault("b", 2)
"a" in d
"z" in d
```

**输出结果**：

```text
d = {'a': 1}
d['a'] = 1
d['missing'] -> KeyError: 'missing'
d.get('b', 0) = 0  d -> {'a': 1}
setdefault('a', 99) -> 1  d -> {'a': 1}
setdefault('b', 2) -> 2  d -> {'a': 1, 'b': 2}
'a' in d = True   'z' in d = False
```

### `pop(key[, default])` 与 `update(mapping)`

- `pop(key)` 会**删除并返回**该键的值；键不存在时会报错。
- `pop(key, default)` 在键不存在时返回 `default`，并且不会报 `KeyError`。
- `update(mapping)` 会把传入映射里的键值**写回原字典**。

**输入代码**：

```python
d.pop("b")
d.pop("missing", -1)
d.update({"b": 2, "c": 3})
```

**输出结果**：

```text
pop('b') -> 2  d -> {'a': 1}
pop('missing', -1) -> -1  d -> {'a': 1}
update({'b': 2, 'c': 3}) 后 d -> {'a': 1, 'b': 2, 'c': 3}
```

### `keys()`、`values()`、`items()` 与 `copy()`

- `keys()` / `values()` / `items()` 返回的是“视图”；为了稳定展示，脚本里通常会包一层 `list(...)`。
- `copy()` 是**浅拷贝**：外层字典是新的，但内部可变对象不会递归复制。

**输入代码**：

```python
list(d.keys())
list(d.values())
list(d.items())
d.copy()
```

**输出结果**：

```text
list(d.keys()) -> ['a', 'b', 'c']
list(d.values()) -> [1, 2, 3]
list(d.items()) -> [('a', 1), ('b', 2), ('c', 3)]
copy() -> {'a': 1, 'b': 2, 'c': 3}
```

### `popitem()`、`for k, v in d.items()` 与 `clear()`

- `popitem()` 会删除并返回**最后插入**的一对 `(key, value)`。
- `for k, v in d.items()` 是最常见的字典遍历写法。

**输入代码**：

```python
d.popitem()
for k, v in d.items():
    ...
d.clear()
```

**输出结果**：

```text
popitem() -> ('c', 3)  d -> {'a': 1, 'b': 2}
  item: 'a' -> 1
  item: 'b' -> 2
clear() 后 -> {}
```

### `dict` 与 `list` 的 `[]` 区别

- `[]` 在 `dict` 里表示**按 key 取值 / 赋值**：`d[key]`
- `[]` 在 `list` 里表示**按下标取值 / 赋值**：`arr[i]`
- 刷题里常见的 `seen[need]` 是 dict 取值，不是列表追加元素

## str

| 方法 | 作用 |
|------|------|
| `split()` / `split(",")` | 按空白或分隔符拆成列表 |
| `strip()` / `lstrip()` / `rstrip()` | 去两侧或单侧空白 |
| `join(iterable)` | 用当前字符串拼接 iterable 中的字符串 |
| `s[i:j]` | 切片；字符串不可原地改 |

### 说明：`split()` 与 `split(",")`

- **无参 `split()`**：按**任意空白**切分，连续空白会被合并，首尾空白也会被忽略。
- **`split(",")`**：按**字面逗号**切分；连续分隔符会保留空串，段内空格也不会自动去掉。

### `split()` 与 `split(",")`

**输入代码**：

```python
s = "  a,b, c  \n"
"hello   world\nfoo".split()
"a,,b".split(",")
s.split(",")
```

**输出结果**：

```text
repr(s) = '  a,b, c  \n'
'hello   world\nfoo'.split() -> ['hello', 'world', 'foo']
'a,,b'.split(',') -> ['a', '', 'b']
s.split(',') -> ['  a', 'b', ' c  \n']
```

### `strip()` / `lstrip()` / `rstrip()`

- `strip()` / `lstrip()` / `rstrip()` 只处理**两端**空白，不处理中间内容。

**输入代码**：

```python
s.strip()
"  a  b  \n".strip()
"  abc\n".lstrip()
"abc  \n".rstrip()
```

**输出结果**：

```text
s.strip() -> 'a,b, c'
'  a  b  \n'.strip() -> 'a  b'
'  abc\n'.lstrip() -> 'abc\n'
'abc  \n'.rstrip() -> 'abc'
```

### `join(iterable)` 与 `s[i:j]`

- `join(iterable)` 要求 iterable 里的元素都是字符串；混入整数等其他类型会报 `TypeError`。
- 字符串切片也是**左闭右开**，并且返回**新字符串**。

**输入代码**：

```python
"--".join(["x", "y", "z"])
"--".join(["x", 1])
"hello"[1:4]
```

**输出结果**：

```text
'--'.join(['x', 'y', 'z']) -> x--y--z
'--'.join(['x', 1]) -> TypeError: sequence item 1: expected str instance, int found
'hello'[1:4]（左闭右开）-> ell
```

## set

| 操作 | 作用 |
|------|------|
| `add` / `remove` / `discard` | 增删；`discard` 无元素不报错 |
| `&` `\|` `-` | 交、并、差 |
| `s.update(other)` | 批量并入元素 |
| `s.union(other)` / `s.intersection(other)` / `s.difference(other)` | 集合运算（返回新集合） |
| `s.copy()` | 浅拷贝 |
| `s.clear()` | 清空集合 |

### `remove` 与 `discard`

- `remove(x)`：`x` 不在集合中报 **`KeyError`**。
- `discard(x)`：不存在时**静默成功**，适合“可能没有”的场景。

### `add` / `remove` / `discard`

**输入代码**：

```python
S = {1}
S.add(2)
S.remove(2)
S.remove(99)
S.discard(99)
```

**输出结果**：

```text
add(2) 后 sorted(S) -> [1, 2]
remove(2) 后 sorted(S) -> [1]
remove(不存在的元素) -> KeyError
discard(99)（不存在也不报错）后 sorted(S) -> [1]
```

### `&` / `|` / `-`

- `&` / `|` / `-` 都会返回**新集合**，不会改动原集合。

**输入代码**：

```python
A = {1, 2, 3}
B = {2, 3, 4}
sorted(A & B)
sorted(A | B)
sorted(A - B)
```

**输出结果**：

```text
A = {1, 2, 3}  B = {2, 3, 4}
sorted(A & B) -> [2, 3]
sorted(A | B) -> [1, 2, 3, 4]
sorted(A - B) -> [1]
```

### `update` / `union` / `intersection` / `difference`

- `update(other)` 会把元素并入**原集合**。
- `union()` / `intersection()` / `difference()` 返回**新集合**，原集合不变。

**输入代码**：

```python
S2 = {1}
S2.update({2, 3})
sorted(A.union(B))
sorted(A.intersection(B))
sorted(A.difference(B))
```

**输出结果**：

```text
update({2, 3}) 后 sorted(S2) -> [1, 2, 3]
sorted(A.union(B)) -> [1, 2, 3, 4]  原 A 仍为 [1, 2, 3]
sorted(A.intersection(B)) -> [2, 3]  原 A 仍为 [1, 2, 3]
sorted(A.difference(B)) -> [1]  原 A 仍为 [1, 2, 3]
```

### `copy()` 与 `clear()`

**输入代码**：

```python
copy_s = A.copy()
copy_s.clear()
```

**输出结果**：

```text
copy() -> [1, 2, 3]
clear() 后 sorted(copy_s) -> []
```

## 官方文档

- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
