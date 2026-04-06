"""对应 02-logging-argparse.md：logging、argparse"""

from __future__ import annotations

import argparse
import logging
import sys
import tempfile
from pathlib import Path

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)
    sys.stdout.flush()


def main() -> None:
    utf8_stdout()
    section("logging：basicConfig、命名 logger、级别")
    # 在 utf8_stdout() 之后配置，以便 StreamHandler 面向已设为 UTF-8 的 stderr
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s %(name)s: %(message)s",
    )
    log = logging.getLogger(__name__)
    log.debug("调试信息")
    log.info("普通信息")
    log.warning("告警")
    sys.stderr.flush()

    section("logging：FileHandler（追加到根 logger，演示完移除）")
    root = logging.getLogger()
    with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", delete=False, suffix=".log") as tf:
        log_path = Path(tf.name)
    try:
        fh = logging.FileHandler(log_path, encoding="utf-8")
        fh.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
        root.addHandler(fh)
        logging.error("仅写入文件的一条")
        root.removeHandler(fh)
        fh.close()
        lines = log_path.read_text(encoding="utf-8").strip().splitlines()
        print("FileHandler 末行:", lines[-1] if lines else "")
    finally:
        log_path.unlink(missing_ok=True)

    section("argparse：parse_args（演示用固定参数，避免依赖 sys.argv）")
    parser = argparse.ArgumentParser(description="演示 argparse")
    parser.add_argument("inputs", nargs="*", help="输入路径，可变个")
    parser.add_argument("--out", type=Path, default=Path("out.txt"), help="输出路径")
    parser.add_argument("--verbose", action="store_true", help="详细输出")
    demo_argv = ["--verbose", "--out", "build/result.txt", "a.csv", "b.csv"]
    args = parser.parse_args(demo_argv)
    print("解析 demo argv:", demo_argv)
    print("  inputs =", args.inputs)
    print("  out    =", args.out)
    print("  verbose=", args.verbose)

    section("与 run_all 共存")
    print("由 run_all 调用时，真实 sys.argv 来自上层；此处已用 demo_argv 固定演示。")
    print("单独运行本文件时 sys.argv =", sys.argv[:3], "..." if len(sys.argv) > 3 else "")


if __name__ == "__main__":
    main()
