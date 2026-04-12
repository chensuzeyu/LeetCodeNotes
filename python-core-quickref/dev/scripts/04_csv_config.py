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
    section("csv：writer / reader（行列表；写磁盘时 open(..., newline='')）")
    buf_rw = io.StringIO()
    w0 = csv.writer(buf_rw)
    w0.writerow(["a", "b"])
    w0.writerow(["1", "2"])
    raw_rows = buf_rw.getvalue()
    print("writer -> repr:", repr(raw_rows))
    print("reader rows:", list(csv.reader(io.StringIO(raw_rows))))
    with tempfile.TemporaryDirectory() as td:
        csv_path = Path(td) / "rows.csv"
        with open(csv_path, "w", encoding="utf-8", newline="") as fh:
            w1 = csv.writer(fh)
            w1.writerow(["a", "b"])
            w1.writerow(["1", "2"])
        with open(csv_path, "r", encoding="utf-8", newline="") as fh:
            print("disk csv repr:", repr(fh.read()))

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

        a_ini = Path(td) / "base.ini"
        b_ini = Path(td) / "override.ini"
        a_ini.write_text("[app]\nport = 8080\n", encoding="utf-8")
        b_ini.write_text("[app]\nport = 9090\n", encoding="utf-8")
        cp3 = ConfigParser()
        cp3.read([a_ini, b_ini])
        print("read([base, override]) [app].port =", cp3.getint("app", "port"))

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
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "demo.toml"
            p.write_bytes(toml_b)
            with open(p, "rb") as fh:
                print("tomllib.load(rb) ->", tomllib.load(fh))
    else:
        print("当前 Python", sys.version.split()[0], "无 stdlib tomllib；可读 INI 或用第三方 tomli。")


if __name__ == "__main__":
    main()
