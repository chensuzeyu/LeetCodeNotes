# 02 · logging / argparse（可观测与命令行入口）

完整演示：[scripts/02_logging_argparse.py](scripts/02_logging_argparse.py)  
运行：`python3 02_logging_argparse.py`（在 `dev/scripts` 目录）

脚本从「能跑」到「能维护」，通常要先有**分级日志**与**规范 CLI**。  
下文各「输入代码 / 输出结果」与脚本 **一一对应**；`logging` 默认写 `stderr`，`section()` 与 `print` 写 `stdout`（见 [../README.md](../README.md) 维护约定）。

## logging

| 用法 | 说明 |
|------|------|
| `logging.basicConfig(level=..., format=...)` | 进程级**一次性**基础配置；多次调用常只有第一次生效 |
| `logging.getLogger(__name__)` | 模块内 logger；比全局 `logging.info` 更易控制 |
| `logger.debug/info/warning/error/exception` | 级别；`exception` 会附带当前异常栈 |
| `FileHandler` / `StreamHandler` | 输出到文件或指定流 |

### 级别与格式

- **`level=DEBUG`**：低于该级别的日志不会输出；脚本演示里 `DEBUG`/`INFO`/`WARNING` 都会出现在 `stderr`。
- `basicConfig(...)` 通常只应在程序入口集中配一次；库代码里一般不自己反复配 root logger。

**与 `print`**：`print` 难过滤级别、难统一格式；**库代码**优先用 `logging`，仅在极简一次性脚本可 `print`。

**输入代码**（`02_logging_argparse.py`）：

```python
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)
log.debug("调试信息")
log.info("普通信息")
log.warning("告警")
```

**输出结果**（`stderr`；直接运行本文件时 `name` 为 `__main__`；由 `run_all` 动态加载时为 `02_logging_argparse`）：

```text
DEBUG __main__: 调试信息
INFO __main__: 普通信息
WARNING __main__: 告警
```

**输入代码**（`02_logging_argparse.py`）：

```python
root = logging.getLogger()
# 临时文件路径由 NamedTemporaryFile(delete=False, suffix=".log") 生成
fh = logging.FileHandler(log_path, encoding="utf-8")
root.addHandler(fh)
logging.error("仅写入文件的一条")
# 随后读文件取末行打印
```

**输出结果**（`stdout`；同时 root logger 仍会往 `stderr` 打出一行 `ERROR root: 仅写入文件的一条`）：

```text
FileHandler 末行: ERROR 仅写入文件的一条
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

- **`demo_argv`**：`--verbose`、`--out build/result.txt`、以及两个输入文件；`inputs` 收集剩余位置参数，`out` 为 `Path`（Windows 下 `print(args.out)` 为 `build\result.txt`）。
- `parse_args(argv)` 这种写法对教学和测试都很友好，因为它不依赖真实命令行环境。

**输入代码**（`02_logging_argparse.py`）：

```python
demo_argv = ["--verbose", "--out", "build/result.txt", "a.csv", "b.csv"]
args = parser.parse_args(demo_argv)
```

**输出结果**（`stdout`）：

```text
解析 demo argv: ['--verbose', '--out', 'build/result.txt', 'a.csv', 'b.csv']
  inputs = ['a.csv', 'b.csv']
  out    = build\result.txt
  verbose= True
```

**输入代码**：无额外解析；脚本打印 `sys.argv` 前若干项。

**输出结果**（`stdout`，单独运行本文件时首参为当前脚本路径；由 `run_all` 调用时首参来自上层）：

```text
由 run_all 调用时，真实 sys.argv 来自上层；此处已用 demo_argv 固定演示。
单独运行本文件时 sys.argv = ['<ARGV0>']
```

## 官方文档

- [logging](https://docs.python.org/3/library/logging.html)  
- [argparse](https://docs.python.org/3/library/argparse.html)
