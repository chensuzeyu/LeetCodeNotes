# 10 · dataclasses / typing（结构化数据与类型标注）

完整演示：`scripts/10_dataclasses_typing.py`  
运行：`python 10_dataclasses_typing.py`（在 `dev/scripts` 目录下）

日常开发里用 **dataclass** 减少样板代码；**typing** 提升可读性并可配合编辑器/静态检查（`mypy` 等）。

## dataclasses

| 用法 | 说明 |
|------|------|
| `@dataclass` | 自动生成 `__init__`、`__repr__` 等 |
| `field(default=...)` / `field(default_factory=list)` | 可变默认值必须用 `default_factory` |
| `frozen=True` | 只读实例（可哈希的前置条件之一） |

## typing（常用子集）

| 符号 | 说明 |
|------|------|
| `Optional[T]` | 等价 `T \| None`（3.10+ 可直接写） |
| `list[int]` / `dict[str, float]` | 泛型容器（3.9+ 可用内置泛型） |
| `Callable[[int, str], bool]` | 函数类型粗略描述 |
| `Protocol` | 结构化子类型（duck typing 正规化） |

## 官方文档

- [dataclasses](https://docs.python.org/3/library/dataclasses.html)  
- [typing](https://docs.python.org/3/library/typing.html)
