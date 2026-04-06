# 06 · urllib.parse / urllib.request（URL 与简单 HTTP）

完整演示：`scripts/06_urllib.py`  
运行：`python 06_urllib.py`（在 `dev/scripts` 目录下）

小工具拉接口、拼查询串时用标准库即可；**复杂客户端**再考虑 `httpx` / `requests`（第三方）。

## urllib.parse

| 用法 | 说明 |
|------|------|
| `urlparse(url)` | 拆 scheme、netloc、path、query |
| `parse_qs` / `urlencode` | query 字典 ↔ 字符串 |

## urllib.request

| 用法 | 说明 |
|------|------|
| `Request(url, headers={...})` | 可带 UA 等头 |
| `urlopen(req, timeout=10)` | 上下文管理器读取响应；注意网络/证书/代理环境差异 |

**异常**：`URLError`、`HTTPError`（后者亦为 `URLError` 子类）。

## 官方文档

- [urllib](https://docs.python.org/3/library/urllib.html)
