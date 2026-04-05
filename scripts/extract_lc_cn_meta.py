#!/usr/bin/env python3
"""
从力扣中国区题目页 HTML 中提取 <meta name="description"> 里的中文题干摘要。

该片段通常包含：题目描述、示例、提示、进阶等，适合粘贴到笔记中的「原题」小节后再按需整理
（例如将提示里的上界改成页面显示用的上标形式）。

用法（控制台建议 UTF-8）：
  python scripts/extract_lc_cn_meta.py path/to/page.html
  python scripts/extract_lc_cn_meta.py path/to/page.html -o out.txt

获取 HTML 示例：
  curl.exe -L -o two-sum.html "https://leetcode.cn/problems/two-sum/description/"
"""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path


def extract_description(html_text: str) -> str:
    key = 'name="description" content="'
    i = html_text.find(key)
    if i < 0:
        raise ValueError("未找到 name=\"description\" 的 meta 标签（请确认是力扣题目描述页 HTML）")
    start = i + len(key)
    end = start
    while end < len(html_text):
        if html_text[end] == '"' and html_text[end - 1] != "\\":
            break
        end += 1
    else:
        raise ValueError("meta description 未正常闭合")
    s = html.unescape(html_text[start:end])
    return s.replace("\xa0", " ").replace("\u200b", "")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从力扣 CN 题目页 HTML 提取 meta description 正文",
    )
    parser.add_argument("html_file", type=Path, help="本地 HTML 文件路径")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="写入 UTF-8 文本文件；省略则打印到标准输出",
    )
    args = parser.parse_args()

    raw = args.html_file.read_text(encoding="utf-8", errors="replace")
    try:
        text = extract_description(raw)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1

    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8", newline="\n")
    else:
        try:
            sys.stdout.buffer.write((text + "\n").encode("utf-8"))
        except BrokenPipeError:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
