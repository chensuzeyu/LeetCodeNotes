# Python 3 速查 · 日常开发

**与刷题分离**：这里放写脚本、读配置、文本与路径处理等**工程向最低限** API；需要 `heapq` / `bisect` 等见 [leetcode](../leetcode/README.md)。

## 怎么用

```bash
cd python-core-quickref/dev/scripts
python run_all.py
```

或：`python 01_json_re_pathlib.py`

要求：**Python 3.9+**。Windows 终端乱码见 [上层 README](../README.md)。

## 文档索引

| 文档 | 演示脚本 | 内容 |
|------|----------|------|
| [01-json-re-pathlib.md](01-json-re-pathlib.md) | [scripts/01_json_re_pathlib.py](scripts/01_json_re_pathlib.py) | `json`、`re`、`pathlib` |

（后续可追加 `02-datetime-logging.md` 等，仍在本目录单独编号。）

## 维护

新增日常向主题：在本目录加 `0x-*.md` 与 `scripts/0x_*.py`，并更新 `scripts/run_all.py` 的 `demos`。
