# 05 · os / sys / subprocess / shutil（环境、进程、文件批处理）

完整演示：`scripts/05_os_sys_subprocess_shutil.py`  
运行：`python 05_os_sys_subprocess_shutil.py`（在 `dev/scripts` 目录下）

与 `pathlib`（见 `01`）互补：`os`/`shutil` 偏传统 API；`subprocess` 是**调用外部命令**的正路。

## os

| 用法 | 说明 |
|------|------|
| `os.environ` | 环境变量映射；注意值为字符串 |
| `os.environ.get("PATH")` | 安全读取 |
| `os.getcwd()` / `chdir` | 当前目录 |

## sys

| 用法 | 说明 |
|------|------|
| `sys.argv` | 命令行参数（`argparse` 通常基于它） |
| `sys.exit(code)` | 以退出码结束进程 |
| `sys.path` | 模块搜索路径（脚本里临时 `insert` 常见于 demo） |

## subprocess

| 用法 | 说明 |
|------|------|
| `run([...], capture_output=True, text=True, check=True)` | 一次性执行；`check=True` 非 0 退出抛 `CalledProcessError` |
| 不要 `shell=True` | 除非必要；注入与安全风险更高 |

## shutil

| 用法 | 说明 |
|------|------|
| `shutil.copy2(src, dst)` | 复制并尽量保留元数据 |
| `shutil.move` / `rmtree` | 移动；递归删目录（**危险**，先确认路径） |

## 官方文档

- [os](https://docs.python.org/3/library/os.html)  
- [sys](https://docs.python.org/3/library/sys.html)  
- [subprocess](https://docs.python.org/3/library/subprocess.html)  
- [shutil](https://docs.python.org/3/library/shutil.html)
