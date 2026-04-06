"""对应 06-urllib.md：urllib.parse、urllib.request"""

from __future__ import annotations

from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("urllib.parse：urlparse / parse_qs / urlencode")
    u = urlparse("https://example.com/path?q=hello&tag=py&lang=zh")
    print("scheme", u.scheme, "netloc", u.netloc, "path", u.path)
    print("query ->", parse_qs(u.query))
    q = urlencode([("q", "space value"), ("page", 2)])
    print("urlencode ->", q)

    section("urllib.request：可选联网演示（失败则跳过）")
    req = Request(
        "https://example.com/",
        headers={"User-Agent": "python-core-quickref-demo/0.1"},
        method="GET",
    )
    try:
        with urlopen(req, timeout=5) as resp:
            snippet = resp.read(200)
            print("status", getattr(resp, "status", "?"), "前 200 字节:", snippet[:80], "...")
    except HTTPError as e:
        print("HTTPError:", e)
    except URLError as e:
        print("(离线或网络不可用，跳过 urlopen )", type(e).__name__, e)

    section("urllib.request：HTTPError（非 2xx，需单独捕获）")
    req404 = Request(
        "https://httpbin.org/status/404",
        headers={"User-Agent": "python-core-quickref-demo/0.1"},
        method="GET",
    )
    try:
        with urlopen(req404, timeout=8) as resp:
            print("status 404 演示意外成功:", getattr(resp, "status", "?"))
    except HTTPError as e:
        print("HTTPError.code:", e.code)
    except URLError as e:
        print("(无法访问 httpbin，跳过 HTTPError 演示)", type(e).__name__, e)


if __name__ == "__main__":
    main()
