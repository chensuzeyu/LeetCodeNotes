# 07 · ord/chr 与位运算

完整演示：`scripts/07_chr_bitwise.py`  
运行：`python 07_chr_bitwise.py`

## 字符与码位

| 函数 | 作用 |
|------|------|
| `ord(c)` | 单字符 → Unicode 码点整数 |
| `chr(n)` | 整数 → 单字符 |
| `str.isdigit()` / `isalpha()` 等 | 字符类判断（刷题小工具） |

## 位运算（整数）

假定 `a,b` 为非负整数示意：

| 运算符 | 含义 |
|--------|------|
| `a & b` | 按位与 |
| `a \| b` | 按位或 |
| `a ^ b` | 按位异或（相同为 0，不同为 1） |
| `~a` | 按位取反（注意结果是**带符号**解释下的无限宽度语义，日常刷题多在无符号/掩码下理解） |
| `a << k` / `a >> k` | 左移 / 右移（等价于乘以 / 除以 2^k 的截断） |

## 刷题常见技巧（索引）

- `x & (x - 1)`：去掉二进制最低位的 1（常配合数 1 的个数、位枚举）  
- `x & -x`：**lowbit**（最低位的 1 所代表的数）  
- `1 << i`：第 `i` 位为 1 的掩码（从 0 计）  
- `bin(n).count("1")`：统计二进制中 1 的个数（各版本可用）；**新版** Python 亦可 `int.bit_count()`（视构建而定）  

## 官方文档

- [Built-in types — int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
