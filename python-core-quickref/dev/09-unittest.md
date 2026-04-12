# 09 · unittest（标准库单元测试）

完整演示：[scripts/09_unittest.py](scripts/09_unittest.py)  
运行：`python3 09_unittest.py` 或 `python3 -m unittest 09_unittest.py`（在 `dev/scripts` 目录）

工程里常用 `pytest`，但标准库 `unittest` 无依赖、CI 兼容好，适合速查与最小项目。  
下文各「输入代码 / 输出结果」与脚本逐段对应；测试耗时可写作 `<ELAPSED>`。

## 要点

| 用法 | 说明 |
|------|------|
| `unittest.TestCase` | 子类里编写 `test_*` 方法 |
| `self.assertEqual` / `assertRaises` | 常用断言 |
| `setUp` / `tearDown` | 每个测试前后的钩子 |
| `unittest.main()` | 直接运行当前文件测试 |
| `TextTestRunner(verbosity=2).run(suite)` | 以可读文本方式运行 suite |

### `assertRaises`、`setUp` 与 `TextTestRunner`

- `setUp()` 会在**每个测试方法之前**执行一次；不同测试之间不要指望共享它改过的状态。
- `assertRaises(...)` 让“预期抛异常”也能成为可验证测试，而不是靠人工看报错。
- `TextTestRunner(verbosity=2)` 会把每个 `test_*` 的名字和结果都打印出来，更适合教学和命令行观察。

**输入代码**：

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
```

**输出结果**（`stdout`）：

```text
============================================================
unittest：TextTestRunner 运行 Sample
============================================================
test_add (__main__.TestAdd) ... ok
test_raises (__main__.TestAdd) ... ok

----------------------------------------------------------------------
Ran 2 tests in <ELAPSED>s

OK
wasSuccessful: True
```

## 官方文档

- [unittest](https://docs.python.org/3/library/unittest.html)
