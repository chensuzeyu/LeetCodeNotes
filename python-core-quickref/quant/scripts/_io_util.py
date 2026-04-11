"""演示脚本公用：在 Windows 等环境下尽量让标准输出使用 UTF-8。"""

from __future__ import annotations

import sys


def utf8_stdout() -> None:
    """尽量让标准输出与标准错误使用 UTF-8（logging 默认常写到 stderr）。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass
