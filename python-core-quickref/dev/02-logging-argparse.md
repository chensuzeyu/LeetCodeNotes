# 02 · logging / argparse（可观测与命令行入口）

完整演示：[scripts/02_logging_argparse.py](scripts/02_logging_argparse.py)  
运行：`python 02_logging_argparse.py`（在 `dev/scripts` 目录）

脚本从「能跑」到「能维护」，通常要先有**分级日志**与**规范 CLI**。  
下文「预期输出」与脚本一致；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## logging

| 用法 | 说明 |
|------|------|
| `logging.basicConfig(level=..., format=...)` | 进程级**一次性**基础配置；多次调用常只有第一次生效 |
| `logging.getLogger(__name__)` | 模块内 logger；比全局 `logging.info` 更易控制 |
| `logger.debug/info/warning/error/exception` | 级别；`exception` 会附带当前异常栈 |
| `FileHandler` / `StreamHandler` | 输出到文件或指定流 |

### 级别与格式

- **`level=DEBUG`**：低于该级别的日志不会输出；脚本演示里 `DEBUG`/`INFO`/`WARNING` 都会出现在 `stderr`。

**与 `print`**：`print` 难过滤级别、难统一格式；**库代码**优先用 `logging`，仅在极简一次性脚本可 `print`。

**预期输出摘录**：

```text
DEBUG __main__: 调试信息
INFO __main__: 普通信息
WARNING __main__: 告警
```

## argparse

| 用法 | 说明 |
|------|------|
| `ArgumentParser(description=...)` | 解析器 |
| `add_argument("--out", type=Path, default=...)` | 可选参数；`type=` 做转换 |
| `add_argument("inputs", nargs="*")` | 零个或多个位置参数，解析为**列表** |
| `add_argument("--verbose", action="store_true")` | 出现旗标则为 `True`，否则默认 `False` |
| `parser.parse_args(argv)` | 测试可传入**自定义** `argv`，不必依赖真实 `sys.argv` |

### 演示参数含义

- **`demo_argv`**：`--verbose`、`--out build/result.txt`、以及两个输入文件；`inputs` 收集剩余位置参数，`out` 为 `Path`（Windows 下打印可能是 `build\result.txt`）。

**预期输出摘录**：

```text
解析 demo argv: ['--verbose', '--out', 'build/result.txt', 'a.csv', 'b.csv']
  inputs = ['a.csv', 'b.csv']
  out    = build\result.txt
  verbose= True
```

## 官方文档

- [logging](https://docs.python.org/3/library/logging.html)  
- [argparse](https://docs.python.org/3/library/argparse.html)
