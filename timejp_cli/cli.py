from __future__ import annotations
from datetime import datetime
from zoneinfo import ZoneInfo
import argparse

def run():
    parser = argparse.ArgumentParser(
        description="日本時刻とロンドン時刻を表示します（DST対応）"
    )
    parser.add_argument(
        "-f", "--format",
        default="%Y-%m-%d %H:%M:%S %Z%z",
        help="日時フォーマット（デフォルト: %(default)s）"
    )
    args = parser.parse_args()

    now_utc = datetime.now(tz=ZoneInfo("UTC"))
    tokyo = now_utc.astimezone(ZoneInfo("Asia/Tokyo"))
    london = now_utc.astimezone(ZoneInfo("Europe/London"))

    print("Tokyo :", tokyo.strftime(args.format))
    print("London:", london.strftime(args.format))
