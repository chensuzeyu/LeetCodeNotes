# 11 · random / copy（实验复现与结构拷贝）

完整演示：[scripts/11_random_copy.py](scripts/11_random_copy.py)  
运行：`python3 11_random_copy.py`（在 `dev/scripts` 目录）

评测脚本、造数据、对拍常用 `random`；嵌套结构调试时常要区分浅拷贝与深拷贝。  
下文各「输入代码 / 输出结果」与脚本逐段对应；`secrets.token_hex(...)` 的结果每次不同，用 `<TOKEN_HEX_16>` 占位。

## random

| 用法 | 说明 |
|------|------|
| `random.seed(a)` | 固定种子，便于复现 |
| `random.random()` | `[0, 1)` 均匀 float |
| `random.randint(a, b)` | 闭区间 `[a, b]` 整数 |
| `random.randrange(...)` | 半开区间直觉与 `range` 一致 |
| `random.choice(seq)` | 抽一个元素 |
| `random.choices(seq, k=n)` | 可重复抽样 |
| `random.sample(seq, k)` | 不重复抽样 |
| `random.shuffle(x)` | 原地打乱，返回 `None` |

### `seed` / `random` / `randint` / `randrange` / `choices` / `choice` / `shuffle` / `sample`

**输入代码**：

```python
random.seed(42)
round(random.random(), 6), round(random.random(), 6)
[random.randint(1, 6) for _ in range(3)]
[random.randrange(0, 10, 2) for _ in range(2)]
random.choices(["a", "b", "c"], k=5)
random.choice(["a", "b", "c"])
xs = [1, 2, 3, 4, 5]
random.shuffle(xs)
random.sample(range(10), k=4)
```

**输出结果**（`stdout`）：

```text
seed(42) 后 random() 两次: 0.639427 0.025011
randint(1, 6) 三次: [3, 2, 2]
randrange(0, 10, 2) 两次: [2, 0]
choices 可重复 5 次: ['c', 'c', 'a', 'b', 'a']
choice(['a', 'b', 'c']): a
shuffle 后: [5, 4, 3, 1, 2]
sample(不重复): [8, 6, 3, 7]
```

### `secrets`（安全随机）

- 令牌、密码学相关用途请用 `secrets`，不要用 `random`。

**输入代码**：

```python
secrets.token_hex(8)
```

**输出结果**（`stdout`）：

```text
token_hex(8) = <TOKEN_HEX_16>
```

## copy

| 用法 | 说明 |
|------|------|
| `copy.copy(x)` | 浅拷贝：外层是新对象，内层引用仍共享 |
| `copy.deepcopy(x)` | 深拷贝：递归复制，内层对象也独立 |

### `copy.copy(...)` 与 `copy.deepcopy(...)`

**输入代码**：

```python
nested = {"outer": {"x": [1, 2]}}
shallow = copy.copy(nested)
deep = copy.deepcopy(nested)
nested["outer"]["x"].append(99)
```

**输出结果**（`stdout`）：

```text
改 nested 内层列表后 shallow["outer"]["x"] = [1, 2, 99]
深拷贝不受影响 deep["outer"]["x"] = [1, 2]
```

## 官方文档

- [random](https://docs.python.org/3/library/random.html)  
- [copy](https://docs.python.org/3/library/copy.html)  
- [secrets](https://docs.python.org/3/library/secrets.html)
