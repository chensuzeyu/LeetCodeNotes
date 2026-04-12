# 05 · os / sys / subprocess / shutil（环境、进程、文件批处理）

完整演示：[scripts/05_os_sys_subprocess_shutil.py](scripts/05_os_sys_subprocess_shutil.py)  
运行：`python3 05_os_sys_subprocess_shutil.py`（在 `dev/scripts` 目录）

与 `pathlib`（见 `01`）互补：`os` / `shutil` 偏传统 API；`subprocess` 是调用外部命令的正路。  
下文各「输入代码 / 输出结果」与脚本逐段对应；`PATH`、临时目录、`sys.argv`、解释器路径等动态片段使用 `<PATH_PREVIEW>`、`<TMP_PATH>`、`<ARGV0>`、`<PY_EXECUTABLE>`、`<CWD>` 占位。

## os

| 用法 | 说明 |
|------|------|
| `os.environ` | 环境变量映射；值为字符串 |
| `os.environ.get("PATH")` | 安全读取 |
| `os.getcwd()` / `os.chdir(...)` | 当前目录 / 切换目录 |

### `os.environ.get(...)` 与 `getcwd()` / `chdir()`

- `os.environ` 里的值都是字符串；即使你放进去的是数字语义，读出来也要自己再转型。

**输入代码**：

```python
path_preview = os.environ.get("PATH", "")
os.getcwd()

old_cwd = os.getcwd()
with tempfile.TemporaryDirectory() as td:
    os.chdir(td)
    os.getcwd()
```

**输出结果**（`stdout`）：

```text
PATH 前 80 字: <PATH_PREVIEW>
getcwd: <CWD>
chdir 临时目录后 getcwd: <TMP_PATH>
恢复后 getcwd: <CWD>
```

## sys

| 用法 | 说明 |
|------|------|
| `sys.argv` | 命令行参数 |
| `sys.path` | 模块搜索路径 |
| `sys.version` / `sys.executable` | 当前解释器版本与路径 |
| `sys.exit(code)` | 以退出码结束进程；本课在子进程中演示 |

### `argv` / `path` / `version` / `executable`

- `sys.path` 控制 import 搜索路径；临时插到最前面时，记得用完再恢复。

**输入代码**：

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

**输出结果**（`stdout`）：

```text
sys.argv: ['<ARGV0>']
len(sys.path): <N>
sys.path[0]（脚本目录，用于 import 搜索起点）: <SCRIPT_DIR>
insert(0, ...) 后 path[0]: <SCRIPT_DIR>/_demo_sys_path_insert
pop(0) 后恢复原 path[0]: <SCRIPT_DIR>
sys.version: <PY_VERSION>
sys.executable: <PY_EXECUTABLE>
```

## subprocess

| 用法 | 说明 |
|------|------|
| `run([...], capture_output=True, text=True, check=True)` | 一次性执行；非 0 退出时可抛 `CalledProcessError` |
| 避免 `shell=True` | 除非必要；安全风险更高 |

### `subprocess.run(...)`

- 传列表参数时通常比整串命令更稳，也更容易避开引号和转义问题。

**输入代码**：

```python
subprocess.run([sys.executable, "-c", "print('subprocess ok')"], ...)
subprocess.run([sys.executable, "-c", "import sys; sys.exit(7)"], ...)
subprocess.run([sys.executable, "-c", "import sys; sys.exit(1)"], check=True, ...)
```

**输出结果**（`stdout`）：

```text
stdout: subprocess ok
子进程 sys.exit(7) returncode: 7
check=True 捕获 CalledProcessError returncode: 1
```

## shutil

| 用法 | 说明 |
|------|------|
| `shutil.copy2(src, dst)` | 复制并尽量保留元数据 |
| `shutil.move` / `rmtree` | 移动；递归删目录（危险操作，先确认路径） |

### `copy2` / `move` / `rmtree`

- `rmtree` 是递归删除整棵目录树的危险操作；真实项目里一定先确认目标路径。

**输入代码**：

```python
src.write_text("hello", encoding="utf-8")
shutil.copy2(src, dst)
shutil.move(dst, moved)
shutil.rmtree(rm_dir)
```

**输出结果**（`stdout`）：

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
