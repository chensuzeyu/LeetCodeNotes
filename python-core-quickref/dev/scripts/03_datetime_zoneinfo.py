"""对应 03-datetime-zoneinfo.md：datetime、zoneinfo"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    utf8_stdout()
    section("datetime：date / time / datetime、now(UTC)、timedelta、fromisoformat")
    print("time(14, 30):", time(14, 30))
    print("datetime.now()（未带 tz，本地语义依环境）:", datetime.now())
    utc_now = datetime.now(timezone.utc)
    print("UTC now:", utc_now)
    print("加 2 天:", utc_now + timedelta(days=2))
    s = "2026-04-06T12:34:56+00:00"
    parsed = datetime.fromisoformat(s)
    print("fromisoformat:", parsed)

    section("zoneinfo：IANA 时区（无 tzdata 时可能失败）")
    try:
        from zoneinfo import ZoneInfo

        sh = ZoneInfo("Asia/Shanghai")
        localish = datetime(2026, 6, 1, 12, 0, 0, tzinfo=sh)
        print("Asia/Shanghai:", localish, "-> UTC:", localish.astimezone(timezone.utc))
    except Exception as exc:  # noqa: BLE001
        print("(跳过或降级)", type(exc).__name__, exc)
        print("提示：Windows 可 pip install tzdata 以提供 IANA 数据。")

    section("date 与 date.today()")
    print("today:", date.today())


if __name__ == "__main__":
    main()
