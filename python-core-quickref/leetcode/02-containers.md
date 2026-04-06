# 02 · 容器常用方法（list / dict / str / set）

完整演示：`scripts/02_containers.py`  
运行：`python 02_containers.py`

## list

| 方法 / 写法 | 作用 |
|-------------|------|
| `append(x)` | 尾部加入一个元素 |
| `pop()` / `pop(i)` | 弹出末尾或下标 `i` |
| `insert(i, x)` | 在位置 `i` 插入 |
| `nums[i:j]` | 切片，**左闭右开** |
| `nums[::-1]` | 反转副本（新序列） |

## dict

| 方法 / 写法 | 作用 |
|-------------|------|
| `d[key]` | 读；键不存在会 `KeyError` |
| `d.get(key, default)` | 安全读取，带默认值 |
| `d.setdefault(key, default)` | 无则插入再返回 |
| `key in d` | 判断是否含有键 |
| `for k, v in d.items()` | 遍历键值 |

## str

| 方法 | 作用 |
|------|------|
| `split()` / `split(",")` | 按空白或分隔符拆成列表 |
| `strip()` / `lstrip()` / `rstrip()` | 去两侧或单侧空白 |
| `join(iterable)` | 用当前字符串拼接 iterable 中的字符串 |
| `s[i:j]` | 切片；字符串不可原地改 |

## set

| 操作 | 作用 |
|------|------|
| `add` / `remove` / `discard` | 增删；`discard` 无元素不报错 |
| `&` `\|` `-` | 交、并、差 |

## 官方文档

- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
