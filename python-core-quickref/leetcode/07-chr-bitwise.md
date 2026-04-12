# 07 · ord/chr 与位运算

完整演示：[scripts/07_chr_bitwise.py](scripts/07_chr_bitwise.py)  
运行：`python3 07_chr_bitwise.py`

下文各「输入代码 / 输出结果」与脚本逐段对应；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## 字符与码位

| 函数 | 作用 |
|------|------|
| `ord(c)` | 单字符 -> Unicode 码点整数 |
| `chr(n)` | 整数 -> 单字符 |
| `str.isdigit()` / `isalpha()` 等 | 字符类判断（刷题小工具） |

### `ord` / `chr` 与字符类判断

- `ord(c)` 只接受**单个字符**；传更长字符串会报错。
- `chr(n)` 是码点到字符的反向映射，和 `ord` 正好相反。

**输入代码**：

```python
ord("A"), chr(65)
ord("你")
"9".isdigit(), "a".isalpha()
```

**输出结果**：

```text
ord('A') = 65  chr(65) = A
ord('你') = 20320
'9'.isdigit() = True   'a'.isalpha() = True
```

## 位运算（整数）

假定 `a`、`b` 为非负整数示意：

| 运算符 | 含义 |
|--------|------|
| `a & b` | 按位与 |
| `a \| b` | 按位或 |
| `a ^ b` | 按位异或（相同为 0，不同为 1） |
| `~a` | 按位取反（结果按带符号、无限宽度语义解释） |
| `a << k` / `a >> k` | 左移 / 右移 |

### `&` / `|` / `^` / `~` / 移位

- `^` 常用于“相同抵消、不同保留”的场景，比如找只出现一次的数。
- `~a` 在 Python 里不是“固定宽度按位取反”，所以结果常表现为负数。

**输入代码**：

```python
a, b = 0b1100, 0b1010
a & b
a | b
a ^ b
~a
a << 1
a >> 1
```

**输出结果**：

```text
a=0b1100 b=0b1010
a&b = 0b1000 a|b = 0b1110 a^b = 0b0110
~a = -13
a << 1 = 24 0b11000  a >> 1 = 6 0b110
```

## 刷题常见技巧

- `x & (x - 1)`：去掉二进制最低位的 1。
- `x & -x`：`lowbit`，取最低位的 1 所代表的数。
- `1 << i`：第 `i` 位为 1 的掩码（从 0 计）。
- `bin(n).count("1")`：统计二进制中 1 的个数；高版本可用 `n.bit_count()`。

### `lowbit` 与去掉最低位 1

- `x & -x` 会只保留最低位的 1；树状数组里常把它叫 `lowbit`。
- `x & (x - 1)` 会把最低位的 1 消掉，常用于统计 1 的个数或做状态压缩。

**输入代码**：

```python
n = 0b1011000
n & -n
n & (n - 1)
```

**输出结果**：

```text
n=0b1011000 lowbit n&-n = 0b1000
n&(n-1) 去掉最低位1 -> 0b1010000
```

### 统计二进制中 1 的个数

- `bin(n).count("1")` 兼容性最好；`int.bit_count()` 在现代 Python 里更直接。

**输入代码**：

```python
x11 = 0b1011
bin(x11).count("1")
x11.bit_count()
```

**输出结果**：

```text
popcount(0b1011) = 3（写法: bin(n).count('1')） ；int.bit_count() = 3
```

### 子集枚举：掩码与下标

- `1 << len(items)` 表示一共有多少种选或不选的状态。
- `mask >> i & 1` 为 1 就表示“第 `i` 个元素被选中”。

**输入代码**：

```python
items = ["a", "b", "c"]
for mask in range(1 << len(items)):
    chosen = [items[i] for i in range(len(items)) if mask >> i & 1]
```

**输出结果**：

```text
mask=0b00 -> []
mask=0b01 -> ['a']
mask=0b10 -> ['b']
mask=0b11 -> ['a', 'b']
mask=0b100 -> ['c']
```

## 官方文档

- [Built-in types — int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
