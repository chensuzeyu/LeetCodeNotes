# 09 · unittest（标准库单元测试）

完整演示：`scripts/09_unittest.py`  
运行：`python 09_unittest.py` 或 `python -m unittest 09_unittest.py`（在 `dev/scripts` 目录下）

工程里常用 **pytest**（第三方）；但标准库 **unittest** 无依赖、IDE/CI 兼容好，适合速查与最小项目。

## 要点

| 用法 | 说明 |
|------|------|
| `unittest.TestCase` | 子类里 `test_*` 方法 |
| `self.assertEqual` / `assertTrue` / `assertRaises` | 常用断言 |
| `setUp` / `tearDown` | 每测试前后钩子 |
| `unittest.main()` | 直接运行当前文件测试 |
| `python -m unittest discover` | 发现包内测试 |

## 官方文档

- [unittest](https://docs.python.org/3/library/unittest.html)
