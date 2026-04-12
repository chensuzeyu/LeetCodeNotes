# 06 · urllib.parse / urllib.request（URL 与简单 HTTP）

完整演示：[scripts/06_urllib.py](scripts/06_urllib.py)  
运行：`python3 06_urllib.py`（在 `dev/scripts` 目录）

小工具拉接口、拼查询串时用标准库即可；复杂客户端再考虑 `httpx` / `requests`（第三方）。  
下文各「输入代码 / 输出结果」与脚本逐段对应；联网结果可能受网络、DNS、TLS 影响，动态异常片段统一写作 `<NETWORK_ERROR>`。

## urllib.parse

| 用法 | 说明 |
|------|------|
| `urlparse(url)` | 拆 `scheme`、`netloc`、`path`、`query` 等 |
| `parse_qs` | query -> 字典，值为列表 |
| `urlencode` | 字典 / 键值列表 -> 查询串；空格常编码为 `+` |

### `urlparse` / `parse_qs` / `urlencode`

- `parse_qs` 返回的是“键 -> 值列表”，因为同一个查询参数本来就可能出现多次。
- `urlencode` 默认会把空格编码成 `+`；这在 query string 里很常见。

**输入代码**：

```python
u = urlparse("https://example.com/path?q=hello&tag=py&lang=zh")
parse_qs(u.query)
urlencode([("q", "space value"), ("page", 2)])
```

**输出结果**（`stdout`）：

```text
scheme https netloc example.com path /path
query -> {'q': ['hello'], 'tag': ['py'], 'lang': ['zh']}
urlencode -> q=space+value&page=2
```

## urllib.request

| 用法 | 说明 |
|------|------|
| `Request(url, headers={...})` | 可带 UA 等请求头 |
| `urlopen(req, timeout=10)` | 读响应；可能抛 `URLError` / `HTTPError` |

### `urlopen(...)`

- `urlopen` 读到的是字节流；真实项目里通常还会再按响应头或约定编码去 `.decode(...)`。
- 即使是 GET，请求失败也不一定是 HTTP 状态码，网络、DNS、TLS 问题都可能先抛 `URLError`。

**输入代码**：

```python
req = Request(
    "https://example.com/",
    headers={"User-Agent": "python-core-quickref-demo/0.1"},
    method="GET",
)
with urlopen(req, timeout=5) as resp:
    resp.read(200)
```

**输出结果**（成功时）：

```text
status 200 前 200 字节: <BYTES_PREVIEW> ...
```

**输出结果**（离线或网络不可用时）：

```text
(离线或网络不可用，跳过 urlopen ) URLError <NETWORK_ERROR>
```

### `HTTPError`

- `HTTPError` 是 `URLError` 的子类之一，表示“已经连到服务端，但服务端返回了 4xx/5xx 之类的 HTTP 错误”。

**输入代码**：

```python
req404 = Request(
    "https://httpbin.org/status/404",
    headers={"User-Agent": "python-core-quickref-demo/0.1"},
    method="GET",
)
urlopen(req404, timeout=8)
```

**输出结果**（成功连上 httpbin 时）：

```text
HTTPError.code: 404
```

**输出结果**（无法访问时）：

```text
(无法访问 httpbin，跳过 HTTPError 演示) URLError <NETWORK_ERROR>
```

## 官方文档

- [urllib](https://docs.python.org/3/library/urllib.html)
