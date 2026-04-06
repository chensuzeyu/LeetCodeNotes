# 05 · os / sys / subprocess / shutil（环境、进程、文件批处理）

完整演示：[scripts/05_os_sys_subprocess_shutil.py](scripts/05_os_sys_subprocess_shutil.py)  
运行：`python 05_os_sys_subprocess_shutil.py`（在 `dev/scripts` 目录）

与 `pathlib`（见 `01`）互补：`os`/`shutil` 偏传统 API；`subprocess` 是**调用外部命令**的正路。  
下文各「输入输出示例」与脚本 **一一对应**；`PATH`、`临时目录路径`、`sys.argv[0]` 因本机环境而异（见 [../README.md](../README.md) 维护约定）。

## os

| 用法 | 说明 |
|------|------|
| `os.environ` | 环境变量映射；注意值为字符串 |
| `os.environ.get("PATH")` | 安全读取 |
| `os.getcwd()` / `chdir` | 当前目录 |

**输入输出示例**

**输入**（`05_os_sys_subprocess_shutil.py`）：

```python
path_preview = os.environ.get("PATH", "")
# 打印: (path_preview[:80] + "…") if len(path_preview) > 80 else path_preview
os.getcwd()
with tempfile.TemporaryDirectory() as td:
    os.chdir(td)  # 退出 with 前在 finally 中 chdir(old_cwd)，见脚本
```

**输出**（`stdout`；`PATH 前 80 字` 为当前机器 PATH 的前 80 字符，过长则加 `…`；临时目录为系统 Temp 下唯一目录）：

```text
PATH 前 80 字: E:\anaconda3;E:\anaconda3\Library\mingw-w64\bin;E:\anaconda3\Library\usr\bin;E:\…
getcwd: E:\develop\LeetCodeNotes\python-core-quickref\dev\scripts
chdir 临时目录后 getcwd: C:\Users\Lenovo\AppData\Local\Temp\tmprk1y3eb2
恢复后 getcwd: E:\develop\LeetCodeNotes\python-core-quickref\dev\scripts
```

（第三行目录名每次运行不同；`getcwd` 第三、五行为在 `dev/scripts` 下执行时的结果。）

## sys

| 用法 | 说明 |
|------|------|
| `sys.argv` | 命令行参数（`argparse` 通常基于它） |
| `sys.exit(code)` | 以退出码结束进程；本课用子进程演示（见 **subprocess**） |
| `sys.path` | 模块搜索路径；`path[0]` 常为脚本所在目录；临时 `insert`/`pop` 见脚本 |

**输入输出示例**

**输入**（`05_os_sys_subprocess_shutil.py`）：

```python
sys.argv
len(sys.path)
sys.path[0]
fake = str(Path(__file__).resolve().parent / "_demo_sys_path_insert")
sys.path.insert(0, fake)
sys.path.pop(0)
sys.version.split()[0]
sys.executable
```

**输出**（`stdout`；单独运行本文件时 `sys.argv[0]` 为 `05_os_sys_subprocess_shutil.py`；由 `run_all` 调用时为 `run_all.py`；`len(sys.path)` 因环境略异）：

```text
sys.argv: ['05_os_sys_subprocess_shutil.py']
len(sys.path): 9
sys.path[0]（脚本目录，用于 import 搜索起点）: E:\develop\LeetCodeNotes\python-core-quickref\dev\scripts
insert(0, ...) 后 path[0]: E:\develop\LeetCodeNotes\python-core-quickref\dev\scripts\_demo_sys_path_insert
pop(0) 后恢复原 path[0]: E:\develop\LeetCodeNotes\python-core-quickref\dev\scripts
sys.version: 3.9.13
sys.executable: E:\anaconda3\python.exe
```

## subprocess

| 用法 | 说明 |
|------|------|
| `run([...], capture_output=True, text=True, check=True)` | 一次性执行；`check=True` 非 0 退出抛 `CalledProcessError` |
| 不要 `shell=True` | 除非必要；注入与安全风险更高 |

**输入输出示例**

**输入**（`05_os_sys_subprocess_shutil.py`）：

```python
subprocess.run([sys.executable, "-c", "print('subprocess ok')"], capture_output=True, text=True, check=True)
subprocess.run([sys.executable, "-c", "import sys; sys.exit(7)"], capture_output=True, text=True)
subprocess.run([sys.executable, "-c", "import sys; sys.exit(1)"], capture_output=True, text=True, check=True)  # 捕获异常
```

**输出**（`stdout`）：

```text
stdout: subprocess ok
子进程 sys.exit(7) returncode: 7
check=True 捕获 CalledProcessError returncode: 1
```

## shutil

| 用法 | 说明 |
|------|------|
| `shutil.copy2(src, dst)` | 复制并尽量保留元数据 |
| `shutil.move` / `rmtree` | 移动；递归删目录（**危险**，先确认路径） |

**输入输出示例**

**输入**（`05_os_sys_subprocess_shutil.py`，在 `tempfile.TemporaryDirectory()` 内）：

```python
src.write_text("hello", encoding="utf-8")
shutil.copy2(src, dst)
shutil.move(dst, moved)
# rm_dir = base / "rm_me"; (rm_dir / "x.txt").write_text("x", encoding="utf-8")
shutil.rmtree(rm_dir)
```

**输出**（`stdout`）：

```text
copy2 后 exists: True 内容: 'hello'
move 后: hello
rmtree 后 rm_dir.exists(): False
```

## 官方文档

- [os](https://docs.python.org/3/library/os.html)  
- [sys](https://docs.python.org/3/library/sys.html)  
- [subprocess](https://docs.python.org/3/library/subprocess.html)  
- [shutil](https://docs.python.org/3/library/shutil.html)
