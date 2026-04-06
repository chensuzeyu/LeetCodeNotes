# 02 · logging / argparse（可观测与命令行入口）

完整演示：`scripts/02_logging_argparse.py`  
运行：`python 02_logging_argparse.py`（在 `dev/scripts` 目录下）

脚本从「能跑」到「能维护」，通常要先有**分级日志**与**规范 CLI**。

## logging

| 用法 | 说明 |
|------|------|
| `logging.basicConfig(level=..., format=...)` | 进程级**一次性**基础配置；多次调用常只有第一次生效 |
| `logging.getLogger(__name__)` | 模块内 logger；比全局 `logging.info` 更易控制 |
| `logger.debug/info/warning/error/exception` | 级别；`exception` 会附带当前异常栈 |
| `FileHandler` / `StreamHandler` | 输出到文件或指定流 |

**与 `print`**：`print` 难过滤级别、难统一格式；**库代码**优先用 `logging`，仅在极简一次性脚本可 `print`。

## argparse

| 用法 | 说明 |
|------|------|
| `ArgumentParser(description=...)` | 解析器 |
| `add_argument("--out", type=Path, default=...)` | 可选参数；`type=` 做转换 |
| `add_argument("path", nargs="?")` | 位置参数；`nargs="*"` 多个 |
| `add_argument("--verbose", action="store_true")` | 布尔开关 |
| `parser.parse_args()` | 得到 `Namespace`；测试可用 `parse_args([])` |

## 官方文档

- [logging](https://docs.python.org/3/library/logging.html)  
- [argparse](https://docs.python.org/3/library/argparse.html)
