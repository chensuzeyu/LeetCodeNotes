# 09 · unittest（标准库单元测试）

完整演示：[scripts/09_unittest.py](scripts/09_unittest.py)  
运行：`python 09_unittest.py` 或 `python -m unittest 09_unittest.py`（在 `dev/scripts` 目录）

工程里常用 **pytest**（第三方）；但标准库 **unittest** 无依赖、IDE/CI 兼容好，适合速查与最小项目。  
下文「预期输出」与脚本一致（见 [../README.md](../README.md) 维护约定）。

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

**预期输出摘录**（含分隔线与 `wasSuccessful`）：

```text
============================================================
unittest：TextTestRunner 运行 Sample
============================================================
test_add (__main__.TestAdd) ... ok
test_raises (__main__.TestAdd) ... ok
----------------------------------------------------------------------
Ran 2 tests in ...s
OK
wasSuccessful: True
```

## 官方文档

- [unittest](https://docs.python.org/3/library/unittest.html)
