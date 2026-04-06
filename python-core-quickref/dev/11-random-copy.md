# 11 · random / copy（实验复现与结构拷贝）

完整演示：`scripts/11_random_copy.py`  
运行：`python 11_random_copy.py`（在 `dev/scripts` 目录下）

写评测脚本、造数据、对拍时离不开 **随机**；调试图/嵌套结构时常要用 **浅拷贝 / 深拷贝**。

## random

| 用法 | 说明 |
|------|------|
| `random.seed(a)` | 固定种子，便于**复现**（协作与 CI 很有用） |
| `random.random()` | `[0, 1)` 均匀 float |
| `random.randint(a, b)` | 闭区间 `[a, b]` 整数 |
| `random.randrange(stop)` / `randrange(start, stop[, step])` | 半开区间直觉与 `range` 一致 |
| `random.choice(seq)` | 单元素 |
| `random.choices(seq, k=n)` | **可重复**抽 `n` 个 |
| `random.sample(seq, k)` | **不重复**抽 `k` 个（`k` 不能超过可区分元素个数） |
| `random.shuffle(x)` | **原地**打乱列表，返回 `None` |

**安全随机**（令牌、密码学）：用 **`secrets`**，不要用 `random`。

## copy

| 用法 | 说明 |
|------|------|
| `copy.copy(x)` | **浅拷贝**：一层新容器，内层对象仍共享引用 |
| `copy.deepcopy(x)` | **深拷贝**：递归复制；内层可变对象互不影响（注意循环引用与开销） |

## 官方文档

- [random](https://docs.python.org/3/library/random.html)  
- [copy](https://docs.python.org/3/library/copy.html)  
- [secrets](https://docs.python.org/3/library/secrets.html)
