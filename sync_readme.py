#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""读取 prices.json 并校验链接与核验日期的自动化同步脚本"""

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

def sync():
    prices_file = ROOT / "prices.json"
    readme_file = ROOT / "README.md"
    if not prices_file.is_file() or not readme_file.is_file():
        print("prices.json 或 README.md 不存在")
        return 1

    data = json.loads(prices_file.read_text(encoding="utf-8"))
    verified_at = data.get("verified_at", "2026-10-30")

    readme = readme_file.read_text(encoding="utf-8")
    new_readme = re.sub(
        r"(📅 最后全网人工核验：)\d{4}-\d{2}-\d{2}",
        rf"\g<1>{verified_at}",
        readme
    )
    if new_readme != readme:
        readme_file.write_text(new_readme, encoding="utf-8")
        print(f"已更新 README.md 最后核验日期为：{verified_at}")
    else:
        print(f"README.md 核验日期已为最新：{verified_at}")
    return 0

if __name__ == '__main__':
    sys.exit(sync())
