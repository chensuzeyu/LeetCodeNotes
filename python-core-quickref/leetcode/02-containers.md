# 02 · 容器常用方法（list / dict / str / set）

完整演示：[scripts/02_containers.py](scripts/02_containers.py)  
运行：`python 02_containers.py`（在 `leetcode/scripts` 目录）

下文「预期输出」与脚本一致；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## list

| 方法 / 写法 | 作用 |
|-------------|------|
| `append(x)` | 尾部加入一个元素 |
| `pop()` / `pop(i)` | 弹出末尾或下标 `i` |
| `insert(i, x)` | 在位置 `i` 插入 |
| `nums[i:j]` | 切片，**左闭右开** |
| `nums[::-1]` | 反转副本（新序列） |

### 切片与复制反转

- **`nums[i:j]`**：含 `i`，**不含** `j`；省略端点表示从头到尾。
- **`nums[::-1]`**：得到反转后的**新**序列，**原列表不变**。

**预期输出摘录**：

```text
nums[1:3]（左闭右开）-> [2, 3]
nums[::-1]（新序列，原列表不变）-> [3, 2, 9]  nums 仍为 [9, 2, 3]
```

## dict

| 方法 / 写法 | 作用 |
|-------------|------|
| `d[key]` | 读；键不存在会 `KeyError` |
| `d.get(key, default)` | 安全读取，带默认值 |
| `d.setdefault(key, default)` | 无则插入再返回 |
| `key in d` | 判断是否含有键 |
| `for k, v in d.items()` | 遍历键值 |

### `[]` 与 `get` / `setdefault`

- **`d[k]`**：键不存在时抛 **`KeyError`**，适合「键必定存在」的路径。
- **`d.get(k, default)`**：缺失时返回 `default`，不修改字典。
- **`setdefault(k, default)`**：缺失时写入 `default` 再返回（一次访问完成「若没有则建」）。

**预期输出摘录**：

```text
d['missing'] -> KeyError: 'missing'
d.get('b', 0) = 0
setdefault('b', 2) 后 d = {'a': 1, 'b': 2}
```

## str

| 方法 | 作用 |
|------|------|
| `split()` / `split(",")` | 按空白或分隔符拆成列表 |
| `strip()` / `lstrip()` / `rstrip()` | 去两侧或单侧空白 |
| `join(iterable)` | 用当前字符串拼接 iterable 中的字符串 |
| `s[i:j]` | 切片；字符串不可原地改 |

### `split()` 与 `split(",")`

- **无参 `split()`**：按**任意空白**切分，且丢弃首尾空白段。
- **`split(",")`**：按**字面逗号**切分，**不会**自动去掉段内空格。

**预期输出摘录**：

```text
split()（任意空白）-> ['hello', 'world', 'foo']
split(',') -> ['  a', 'b', ' c  \n']
strip() -> repr: 'a,b, c'
'hello'[1:4]（左闭右开）-> ell
```

## set

| 操作 | 作用 |
|------|------|
| `add` / `remove` / `discard` | 增删；`discard` 无元素不报错 |
| `&` `\|` `-` | 交、并、差 |

### `remove` 与 `discard`

- **`remove(x)`**：`x` 不在集合中报 **`KeyError`**。
- **`discard(x)`**：不存在时**静默**成功，适合「可能没有」的场景。

**预期输出摘录**：

```text
remove(不存在的元素) -> KeyError
discard(99)（不存在也不报错）-> {1}
A & B = {2, 3}
```

## 官方文档

- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
