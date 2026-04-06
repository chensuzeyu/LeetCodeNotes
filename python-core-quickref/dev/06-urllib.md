# 06 · urllib.parse / urllib.request（URL 与简单 HTTP）

完整演示：[scripts/06_urllib.py](scripts/06_urllib.py)  
运行：`python 06_urllib.py`（在 `dev/scripts` 目录）

小工具拉接口、拼查询串时用标准库即可；**复杂客户端**再考虑 `httpx` / `requests`（第三方）。  
联网演示可能因 TLS/超时失败，以终端为准（见 [../README.md](../README.md) 维护约定）。

## urllib.parse

| 用法 | 说明 |
|------|------|
| `urlparse(url)` | 拆 `scheme`、`netloc`、`path`、`query` 等 |
| `parse_qs` | query → **字典，值为列表**（同一键可出现多次） |
| `urlencode` | 字典/键值列表 → `application/x-www-form-urlencoded` 字符串，`空格` 常编码为 `+` |

### `parse_qs` 的值为何是列表？

- 规范允许 `?q=1&q=2`；故 `parse_qs` 默认 `{'q': ['1', '2']}`。

**输入输出示例**

**输入**（`06_urllib.py`）：

```python
u = urlparse("https://example.com/path?q=hello&tag=py&lang=zh")
parse_qs(u.query)
urlencode([("q", "space value"), ("page", 2)])
```

**输出**（`stdout`）：

```text
scheme https netloc example.com path /path
query -> {'q': ['hello'], 'tag': ['py'], 'lang': ['zh']}
urlencode -> q=space+value&page=2
```

## urllib.request

| 用法 | 说明 |
|------|------|
| `Request(url, headers={...})` | 可带 UA 等头 |
| `urlopen(req, timeout=10)` | 读响应；超时抛 `URLError`；HTTP 错误码可抛 `HTTPError` |

**异常**：`URLError`、`HTTPError`（后者亦为 `URLError` 子类）。

**输入输出示例（urlopen example.com）**

**输入**（`06_urllib.py`）：

```python
req = Request(
    "https://example.com/",
    headers={"User-Agent": "python-core-quickref-demo/0.1"},
    method="GET",
)
with urlopen(req, timeout=5) as resp:
    resp.read(200)
```

**输出**（`stdout`，成功时；`snippet[:80]` 随 example.com 页面字节变化，下列为一次真实抓取）：

```text
status 200 前 200 字节: b'<!doctype html><html lang="en"><head><title>Example Domain</title><meta name="vi' ...
```

**输出**（`stdout`，TLS/超时/离线时）：

```text
(离线或网络不可用，跳过 urlopen ) URLError <urlopen error _ssl.c:1112: The handshake operation timed out>
```

**输入输出示例（HTTPError 404）**

**输入**（`06_urllib.py`）：

```python
req404 = Request(
    "https://httpbin.org/status/404",
    headers={"User-Agent": "python-core-quickref-demo/0.1"},
    method="GET",
)
urlopen(req404, timeout=8)
```

**输出**（`stdout`，成功连上 httpbin 时）：

```text
HTTPError.code: 404
```

**输出**（`stdout`，无法访问 httpbin 时）：

```text
(无法访问 httpbin，跳过 HTTPError 演示) URLError <urlopen error ...>
```

## 官方文档

- [urllib](https://docs.python.org/3/library/urllib.html)
