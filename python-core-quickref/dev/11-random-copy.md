# 11 · random / copy（实验复现与结构拷贝）

完整演示：[scripts/11_random_copy.py](scripts/11_random_copy.py)  
运行：`python 11_random_copy.py`（在 `dev/scripts` 目录）

写评测脚本、造数据、对拍时离不开 **随机**；调试图/嵌套结构时常要用 **浅拷贝 / 深拷贝**。  
下文数字与 `secrets` 一行**除 `token_hex` 外**在固定 `seed(42)` 下与脚本一致；`token_hex` 每次不同（见 [../README.md](../README.md) 维护约定）。

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

**预期输出摘录**（`seed(42)` 后）：

```text
seed(42) 后 random() 两次: 0.639427 0.025011
randint(1, 6) 三次: [3, 2, 2]
choice(['a', 'b', 'c']): a
shuffle 后: [4, 2, 3, 5, 1]
sample(不重复): [0, 9, 1, 7]
```

```text
token_hex(8) = <每次不同>
```

## copy

| 用法 | 说明 |
|------|------|
| `copy.copy(x)` | **浅拷贝**：外层 dict 是新对象，**内层**仍与源共享引用 |
| `copy.deepcopy(x)` | **深拷贝**：递归复制；内层列表互不影响（注意循环引用与开销） |

**预期输出摘录**：

```text
改 nested 内层列表后 shallow["outer"]["x"] = [1, 2, 99]
深拷贝不受影响 deep["outer"]["x"] = [1, 2]
```

## 官方文档

- [random](https://docs.python.org/3/library/random.html)  
- [copy](https://docs.python.org/3/library/copy.html)  
- [secrets](https://docs.python.org/3/library/secrets.html)
