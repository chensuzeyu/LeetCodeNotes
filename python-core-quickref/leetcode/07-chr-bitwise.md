# 07 · ord/chr 与位运算

完整演示：[scripts/07_chr_bitwise.py](scripts/07_chr_bitwise.py)  
运行：`python 07_chr_bitwise.py`

下文「预期输出」与脚本一致；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## 字符与码位

| 函数 | 作用 |
|------|------|
| `ord(c)` | 单字符 → Unicode 码点整数 |
| `chr(n)` | 整数 → 单字符 |
| `str.isdigit()` / `isalpha()` 等 | 字符类判断（刷题小工具） |

**预期输出摘录**：

```text
ord('A') = 65  chr(65) = A
ord('你') = 20320
'9'.isdigit() = True   'a'.isalpha() = True
```

## 位运算（整数）

假定 `a,b` 为非负整数示意：

| 运算符 | 含义 |
|--------|------|
| `a & b` | 按位与 |
| `a \| b` | 按位或 |
| `a ^ b` | 按位异或（相同为 0，不同为 1） |
| `~a` | 按位取反（注意结果是**带符号**解释下的无限宽度语义，日常刷题多在无符号/掩码下理解） |
| `a << k` / `a >> k` | 左移 / 右移（等价于乘以 / 除以 2^k 的截断） |

**预期输出摘录**：

```text
a=0b1100 b=0b1010
a&b = 0b1000 a|b = 0b1110 a^b = 0b0110
a << 1 = 24 0b11000  a >> 1 = 6 0b110
```

### 刷题常见技巧（与输出对照）

- **`x & (x - 1)`**：去掉二进制最低位的 1（常配合数 1 的个数、位枚举）。
- **`x & -x`**：**lowbit**（最低位的 1 所代表的数）。
- **`1 << i`**：第 `i` 位为 1 的掩码（从 0 计）。
- **`bin(n).count("1")`**：统计二进制中 1 的个数；Python 3.8+ 亦可用 **`n.bit_count()`**（若解释器支持）。

**预期输出摘录**：

```text
n=0b1011000 lowbit n&-n = 0b1000
n&(n-1) 去掉最低位1 -> 0b1010000
popcount(0b1011) = 3（写法: bin(n).count('1')） ；int.bit_count() = 3
```

若解释器无 `int.bit_count`（极少见），脚本在同一行末尾输出「（高版本 Python 也可用 int.bit_count()）」而非分号句；数字与 `bin(n).count('1')` 说明不变。

### 子集枚举：掩码与下标

```text
mask=0b00 -> []
mask=0b01 -> ['a']
mask=0b10 -> ['b']
mask=0b11 -> ['a', 'b']
mask=0b100 -> ['c']
```

## 官方文档

- [Built-in types — int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
