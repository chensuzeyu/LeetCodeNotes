# 01 · json / re / pathlib（日常脚本最低限）

完整演示：[scripts/01_json_re_pathlib.py](scripts/01_json_re_pathlib.py)  
运行：`python 01_json_re_pathlib.py`（在 `dev/scripts` 目录）

偏**本地脚本、小工具、读配置**；与力扣 IDE 无直接关系，但日常开发极常用。  
下文各「输入输出示例」与脚本中的赋值及 `print` **一一对应**；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## json

| 用法 | 说明 |
|------|------|
| `json.loads(s)` | 字符串 → Python 对象 |
| `json.dumps(obj)` | Python 对象 → 字符串；常配 `ensure_ascii=False`（中文不转 `\uXXXX`）、`indent=2`（多行可读） |

### 参数说明

- **`ensure_ascii=False`**：`"你好"` 在 dumps 结果里仍是可读中文，否则会变成 `\u4f60\u597d` 形式。
- **`indent=2`**：美化缩进，便于肉眼 diff / 提交到仓库的配置样例。

**输入输出示例**

**输入**（`01_json_re_pathlib.py`）：

```python
raw = '{"x": 1, "msg": "你好"}'
obj = json.loads(raw)
out = json.dumps(obj, ensure_ascii=False, indent=2)
```

**输出**（`stdout`，与脚本 `print` 一致）：

```text
loads -> {'x': 1, 'msg': '你好'}
dumps(ensure_ascii=False, indent=2):
 {
  "x": 1,
  "msg": "你好"
}
```

## re（正则）

| 用法 | 说明 |
|------|------|
| `re.findall(pattern, s)` | 所有非重叠匹配 → 列表 |
| `re.search` / `re.match` | 找一处（任意位置）/ 从开头匹配；`search` 常配合 `m.group(n)` |
| `pattern = re.compile(...)` | 多次复用时略省开销 |
| 原始字符串 | 模式串用 `r"..."`，少写反斜杠转义 |

### `findall` 与 `search`

- **`findall`**：返回所有匹配串（或分组元组，视模式而定）。
- **`search`**：找到一个就停：`m.group(1)` 取**第一个捕获组**。

**输入输出示例**

**输入**（`01_json_re_pathlib.py`）：

```python
s = "abc 12 def 345"
re.findall(r"\d+", s)
re.search(r"def\s+(\d+)", s)
re.match(r"\d+", s)
re.match(r"abc", s)
re.compile(r"[a-z]+").findall(s)
```

**输出**（`stdout`）：

```text
digits: ['12', '345']
search 分组: 345
match 从开头（首字符非数字）: None
match abc: abc
compile.findall -> ['abc', 'def']
```

## pathlib.Path

| 用法 | 说明 |
|------|------|
| `Path("a/b")` / `Path.cwd()` | 路径对象 |
| `read_text(encoding="utf-8")` | 读整个文本文件 |
| `write_text(..., encoding="utf-8")` | 写文本 |
| `/` 拼接 | `base / "subdir" / "file.txt"`，跨平台 |

### 编码

- 与 [刷题分册 `open`](../leetcode/01-builtins.md) 同理：Windows 上**显式 `utf-8`** 更稳。

**输入输出示例**

**输入**（`01_json_re_pathlib.py`，在 `tempfile.TemporaryDirectory()` 内）：

```python
cfg = base / "conf" / "app.json"
cfg.write_text('{"ok": true}\n', encoding="utf-8")
cfg.read_text(encoding="utf-8")
Path.cwd()
```

**输出**（`stdout`；`写入:` 一行为临时目录，因本机路径不同而变化）：

```text
写入: C:\Users\...\AppData\Local\Temp\...\conf\app.json
read_text -> '{"ok": true}\n'
cwd = E:\develop\LeetCodeNotes\python-core-quickref\dev\scripts
```

（第三行 `cwd` 为运行时的当前工作目录；在 `dev/scripts` 下执行上式时即该目录。）

## 官方文档

- [json](https://docs.python.org/3/library/json.html)  
- [re](https://docs.python.org/3/library/re.html)  
- [pathlib](https://docs.python.org/3/library/pathlib.html)
