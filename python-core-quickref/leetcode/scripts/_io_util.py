"""演示脚本公用：在 Windows 等环境下尽量让标准输出使用 UTF-8。"""

from __future__ import annotations

import sys


def utf8_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
