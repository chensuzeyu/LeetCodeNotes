# 04 · csv / configparser / tomllib（表格与配置）

完整演示：[scripts/04_csv_config.py](scripts/04_csv_config.py)  
运行：`python3 04_csv_config.py`（在 `dev/scripts` 目录）

**ETL 小工具、批处理、服务读本地配置**三类场景极常见。  
下文各「输入代码 / 输出结果」与脚本 **一一对应**；改脚本时请同步更新本文（见 [../README.md](../README.md) 维护约定）。

## csv

| 用法 | 说明 |
|------|------|
| `csv.reader(f)` / `csv.writer(f)` | 行迭代写行；**写磁盘**时 `open(..., newline="")` 避免多余 `\r\r\n` |
| `csv.DictReader` / `DictWriter` | 表头 ↔ 字典，`fieldnames` 与表头行一致 |

### `DictReader` 读回的值

- **单元格一律是字符串**；需要整数要自己 `int(row["score"])`。
- 写磁盘文件时常配 `open(..., newline="")`，这样 `csv.writer` 才不会在某些平台写出多余空行。

**输入代码**（`04_csv_config.py`）：

```python
buf_rw = io.StringIO()
w0 = csv.writer(buf_rw)
w0.writerow(["a", "b"])
w0.writerow(["1", "2"])
raw_rows = buf_rw.getvalue()
list(csv.reader(io.StringIO(raw_rows)))
with open(csv_path, "w", encoding="utf-8", newline="") as fh:
    ...
```

**输出结果**（`stdout`；Windows 下 `writer` 默认 `\r\n` 行尾）：

```text
writer -> repr: 'a,b\r\n1,2\r\n'
reader rows: [['a', 'b'], ['1', '2']]
disk csv repr: 'a,b\r\n1,2\r\n'
```

**输入代码**（`04_csv_config.py`）：

```python
rows = [{"name": "Ann", "score": "92"}, {"name": "Bob", "score": "88"}]
# DictWriter(buf, fieldnames=["name", "score"]); writeheader; writerows
# DictReader(io.StringIO(text))
```

**输出结果**（`stdout`；`print(text.strip())` 含表头与两行数据）：

```text
name,score
Ann,92
Bob,88
read back: [{'name': 'Ann', 'score': '92'}, {'name': 'Bob', 'score': '88'}]
```

## configparser（INI）

| 用法 | 说明 |
|------|------|
| `ConfigParser()` | 解析 `key=value` 分段 INI |
| `read(["a.ini", "b.ini"])` | 多文件后者可覆盖前者（按设计） |
| `get(section, key)` / `getint` / `getboolean` | 带类型转换 |

- `getboolean` / `getint` 这类方法很适合把配置值直接转成业务需要的类型。

**输入代码**（`04_csv_config.py`）：

```python
ini = """\
[app]
debug = yes
port = 8080

[db]
url = sqlite:///./app.db
"""
cp.read_string(ini)
# 另：Path(td)/"local.ini" 写入同上字符串后 cp2.read(p)
# 多文件：a.ini port=8080，override.ini port=9090，cp3.read([a_ini, b_ini])
```

**输出结果**（`stdout`）：

```text
getboolean(app, debug) = True
getint(app, port)      = 8080
read file [db].url = sqlite:///./app.db
read([base, override]) [app].port = 9090
```

## tomllib（标准库 TOML，Python 3.11+）

| 用法 | 说明 |
|------|------|
| `tomllib.loads(s)` / `tomllib.load(f)` | **只读**；`load` 时 `f` 须**二进制**打开 `rb` |
| 3.9–3.10 | 标准库无 `tomllib`；常用第三方 `tomli`（只读）或 `toml` |

- `tomllib` 是标准库里的“读 TOML”方案，但**不负责写回**。

**输入代码**（Python 3.11+，`04_csv_config.py`）：

```python
toml_b = b'''
title = "demo"
[nested]
count = 3
'''
tomllib.loads(toml_b.decode())
with open(p, "rb") as fh:
    tomllib.load(fh)
```

**输出结果**（`stdout`）：

```text
tomllib.loads -> {'title': 'demo', 'nested': {'count': 3}}
tomllib.load(rb) -> {'title': 'demo', 'nested': {'count': 3}}
```

**输入代码**：`sys.version_info < (3, 11)` 分支。

**输出结果**（`stdout`）：

```text
当前 Python <PY_VERSION> 无 stdlib tomllib；可读 INI 或用第三方 tomli。
```

## 官方文档

- [csv](https://docs.python.org/3/library/csv.html)  
- [configparser](https://docs.python.org/3/library/configparser.html)  
- [tomllib](https://docs.python.org/3/library/tomllib.html)
