# 01 · json / re / pathlib（日常脚本最低限）

完整演示：`scripts/01_json_re_pathlib.py`  
运行：`python 01_json_re_pathlib.py`（在 `dev/scripts` 目录下）

偏**本地脚本、小工具、读配置**；与力扣 IDE 无直接关系，但日常开发极常用。

## json

| 用法 | 说明 |
|------|------|
| `json.loads(s)` | 字符串 → Python 对象 |
| `json.dumps(obj)` | Python 对象 → 字符串；常配 `ensure_ascii=False` 中文可读、`indent=2` 排版 |

## re（正则）

| 用法 | 说明 |
|------|------|
| `re.findall(pattern, s)` | 所有非重叠匹配 → 列表 |
| `re.search` / `re.match` | 找一处 / 从开头匹配 |
| `pattern = re.compile(...)` | 多次复用时略省开销 |
| 原始字符串 | 模式串用 `r"..."`，少写反斜杠转义 |

## pathlib.Path

| 用法 | 说明 |
|------|------|
| `Path("a/b")` / `Path.cwd()` | 路径对象 |
| `read_text(encoding="utf-8")` | 读整个文本文件 |
| `write_text(..., encoding="utf-8")` | 写文本 |
| `/` 拼接 | `base / "subdir" / "file.txt"` |

## 官方文档

- [json](https://docs.python.org/3/library/json.html)  
- [re](https://docs.python.org/3/library/re.html)  
- [pathlib](https://docs.python.org/3/library/pathlib.html)
