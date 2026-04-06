"""对应 04-csv-config.md：csv、configparser、tomllib（3.11+）"""

from __future__ import annotations

import csv
import io
import sys
import tempfile
from configparser import ConfigParser
from pathlib import Path

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("csv：DictWriter / DictReader（写磁盘时 open 建议 newline=''）")
    buf = io.StringIO()
    rows = [{"name": "Ann", "score": "92"}, {"name": "Bob", "score": "88"}]
    w = csv.DictWriter(buf, fieldnames=["name", "score"])
    w.writeheader()
    w.writerows(rows)
    text = buf.getvalue()
    print(text.strip())
    r = csv.DictReader(io.StringIO(text))
    print("read back:", list(r))

    section("configparser：INI")
    ini = """\
[app]
debug = yes
port = 8080

[db]
url = sqlite:///./app.db
"""
    cp = ConfigParser()
    cp.read_string(ini)
    print("getboolean(app, debug) =", cp.getboolean("app", "debug"))
    print("getint(app, port)      =", cp.getint("app", "port"))
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "local.ini"
        p.write_text(ini, encoding="utf-8")
        cp2 = ConfigParser()
        cp2.read(p)
        print("read file [db].url =", cp2.get("db", "url"))

    section("tomllib：仅 Python 3.11+ 标准库")
    if sys.version_info >= (3, 11):
        import tomllib

        toml_b = b"""
title = \"demo\"
[nested]
count = 3
"""
        obj = tomllib.loads(toml_b.decode())
        print("tomllib.loads ->", obj)
    else:
        print("当前 Python", sys.version.split()[0], "无 stdlib tomllib；可读 INI 或用第三方 tomli。")


if __name__ == "__main__":
    main()
