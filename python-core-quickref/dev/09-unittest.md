# 09 · unittest（标准库单元测试）

完整演示：[scripts/09_unittest.py](scripts/09_unittest.py)  
运行：`python 09_unittest.py` 或 `python -m unittest 09_unittest.py`（在 `dev/scripts` 目录）

工程里常用 **pytest**（第三方）；但标准库 **unittest** 无依赖、IDE/CI 兼容好，适合速查与最小项目。  
下文「输入输出示例」与脚本 **一一对应**（见 [../README.md](../README.md) 维护约定）。

## 要点

| 用法 | 说明 |
|------|------|
| `unittest.TestCase` | 子类里 `test_*` 方法 |
| `self.assertEqual` / `assertTrue` / `assertRaises` | 常用断言；`with self.assertRaises(Exc):` 校验异常 |
| `setUp` / `tearDown` | 每测试前后钩子 |
| `unittest.main()` | 直接运行当前文件测试 |
| `python -m unittest discover` | 发现包内测试 |
| `TextTestRunner(verbosity=2).run(suite)` | 与 `defaultTestLoader.loadTestsFromTestCase` 配合 |

### `assertRaises`

- 示例：`add(1, "x")` 应对 `TypeError`，在 `with` 块内调用被测函数。

**输入输出示例**

**输入**（`09_unittest.py`）：

```python
def add(a: int, b: int) -> int:
    return a + b

class TestAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.left = 2

    def tearDown(self) -> None:
        pass

    def test_add(self) -> None:
        self.assertEqual(add(self.left, 3), 5)

    def test_raises(self) -> None:
        with self.assertRaises(TypeError):
            add(1, "x")

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
result = runner.run(suite)
print("wasSuccessful:", result.wasSuccessful())
```

**输出**（`stdout`；`Ran 2 tests in ...s` 中耗时因机器略异）：

```text
============================================================
unittest：TextTestRunner 运行 Sample
============================================================
test_add (__main__.TestAdd) ... ok
test_raises (__main__.TestAdd) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
wasSuccessful: True
```

## 官方文档

- [unittest](https://docs.python.org/3/library/unittest.html)
