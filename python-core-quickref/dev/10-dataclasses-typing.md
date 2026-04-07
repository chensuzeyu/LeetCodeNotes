# 10 · dataclasses / typing（结构化数据与类型标注）

完整演示：[scripts/10_dataclasses_typing.py](scripts/10_dataclasses_typing.py)  
运行：`python3 10_dataclasses_typing.py`（在 `dev/scripts` 目录）

日常开发里用 **dataclass** 减少样板代码；**typing** 提升可读性并可配合编辑器/静态检查（`mypy` 等）。  
下文各「输入代码 / 输出结果」与脚本 **一一对应**（见 [../README.md](../README.md) 维护约定）。

## dataclasses

| 用法 | 说明 |
|------|------|
| `@dataclass` | 自动生成 `__init__`、`__repr__` 等 |
| `field(default=...)` / `field(default_factory=list)` | **可变默认值**（`list`/`dict`）必须用 `default_factory`，否则多实例共享同一对象 |
| `frozen=True` | 只读实例（可哈希的前置条件之一） |

### `default_factory` 示例

```python
@dataclass
class User:
    name: str
    tags: list[str] = field(default_factory=list)
    score: Optional[float] = None
```

**输入代码**（`10_dataclasses_typing.py`；`Point` / `Square` / `HasArea` / `total_area` 定义见脚本）：

```python
u = User("Ann", tags=["dev", "py"], score=97.5)
v = User("Bob")
v.tags.append("new")
Point(3, 4)
total_area(Square(2))  # Square(2).area() -> 4.0
```

**输出结果**（`stdout`）：

```text
User(name='Ann', tags=['dev', 'py'], score=97.5)
User(name='Bob', tags=['new'], score=None)
frozen Point: Point(x=3, y=4)
Protocol total_area(Square(2)): 4
```

（`Bob` 仅 `append('new')`，因 `tags` 是每实例独立列表。）

## typing（常用子集）

| 符号 | 说明 |
|------|------|
| `Optional[T]` | 等价 `T \| None`（3.10+ 可直接写） |
| `list[int]` / `dict[str, float]` | 泛型容器（3.9+ 可用内置泛型） |
| `Callable[[int, str], bool]` | 函数类型粗略描述 |
| `Protocol` | 结构化子类型（duck typing 正规化） |

**输入代码**（`10_dataclasses_typing.py`）：

```python
twice: Callable[[int], int] = lambda x: x * 2
twice(21)
```

**输出结果**（`stdout`）：

```text
twice(21) = 42
```

## 官方文档

- [dataclasses](https://docs.python.org/3/library/dataclasses.html)  
- [typing](https://docs.python.org/3/library/typing.html)
