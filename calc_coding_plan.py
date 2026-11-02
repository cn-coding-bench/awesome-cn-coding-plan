#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Awesome CN Coding Plan - 国内主流 AI 编程套餐月度/年度成本对比计算器
零第三方依赖，直接在终端中输出不同强度下的真实算账对比与避坑推荐。
"""

import argparse
import sys

def format_row(cols, widths, aligns):
    parts = []
    for val, w, align in zip(cols, widths, aligns):
        s = str(val)
        actual_len = sum(2 if ord(c) > 127 else 1 for c in s)
        padding = max(0, w - actual_len)
        if align == '<':
            parts.append(s + ' ' * padding)
        elif align == '>':
            parts.append(' ' * padding + s)
        else:
            left = padding // 2
            right = padding - left
            parts.append(' ' * left + s + ' ' * right)
    return " | ".join(parts)

def run_calc(hours=4.0, mode='agent', team=1):
    mode_multiplier = {
        'completion': (0.5, '日常轻度代码补全 (0.5M Tokens/h)'),
        'refactor': (1.5, '中度多文件重构 / Cline (1.5M Tokens/h)'),
        'agent': (3.0, '全自动 Agent 挂机 / Claude Code (3.0M Tokens/h)')
    }
    mult, mode_name = mode_multiplier.get(mode, (1.5, '中度多文件重构'))
    monthly_tokens_m = hours * 22 * mult * team
    annual_tokens_m = monthly_tokens_m * 12

    plans = [
        {
            'name': '字节火山方舟 Coding Plan',
            'first_month': 9.41,
            'renewal': 40.0,
            'annual': (9.41 + 40.0 * 11) * team,
            'models': 'DeepSeek-V4.1 / GLM-5.3 / Doubao / Kimi',
            'pros': '免抢购 / 首月 ¥9.4 / 4大模型自由切 / 支持 Auto 路由',
            'url': 'https://coding.mybskm.top/go/volcengine-coding'
        },
        {
            'name': '阿里云百炼 Coding Plan Pro',
            'first_month': 39.9,
            'renewal': 200.0,
            'annual': (39.9 + 200.0 * 11) * team,
            'models': '通义千问 Qwen3.8-Max / Qwen3.8-Coder',
            'pros': '国内直连极低延迟 / 工具调用稳定 (热门档需早09:30蹲点)',
            'url': 'https://coding.mybskm.top/go/aliyun-coding'
        },
        {
            'name': '腾讯云通用 Token Plan Lite',
            'first_month': 28.0,
            'renewal': 39.0,
            'annual': (28.0 + 39.0 * 11) * team,
            'models': '腾讯混元 Turbo/T1 / DeepSeek / GLM',
            'pros': '积分池按需扣减 / 配合 WorkBuddy 编程助手',
            'url': 'https://coding.mybskm.top/go/tencent-workbuddy'
        },
        {
            'name': '智谱 GLM Coding Plan Lite',
            'first_month': 0.0,
            'renewal': 94.4,
            'annual': (0.0 + 94.4 * 11) * team,
            'models': '智谱 GLM-5.3 / GLM-5.3-Flash',
            'pros': '实名可领 2000万免额 Tokens / 长文本学术利器 (拼好模已下线)',
            'url': 'https://coding.mybskm.top/go/zhipu-glm'
        },
        {
            'name': '海外 Cursor Pro 对照组 ($20/月)',
            'first_month': 145.0,
            'renewal': 145.0,
            'annual': (145.0 * 12) * team,
            'models': 'Claude 3.5 Sonnet / GPT-4o',
            'pros': '原生 IDE 补全体验强 (需外币卡、网络风控与代付溢价)',
            'url': 'https://cursor.com'
        },
        {
            'name': '海外 Claude Pro 对照组 ($20/月)',
            'first_month': 145.0,
            'renewal': 145.0,
            'annual': (145.0 * 12) * team,
            'models': 'Claude 3.5 Sonnet / Haiku 3.5',
            'pros': '网页端与官方 CLI (高频重构易触碰 5h 频率墙)',
            'url': 'https://claude.com'
        }
    ]

    print("=" * 88)
    print(" 🚀 Awesome CN Coding Plan · 国内 AI 编程算力套餐月度/年度成本对比计算器")
    print("=" * 88)
    print(f"设定参数: 每天高频使用 {hours} 小时 | 模式: {mode_name} | 团队人数: {team} 人")
    print(f"预估工作量: 月度约 {monthly_tokens_m:.1f} M Tokens | 年度约 {annual_tokens_m:.1f} M Tokens\n")

    widths = [28, 12, 12, 12, 20]
    aligns = ['<', '>', '>', '>', '<']
    headers = ['套餐名称', '首月支出(¥)', '次月续费(¥)', '年总预算(¥)', '核心特征与选型避坑']

    print(format_row(headers, widths, aligns))
    print("-" * 92)

    for p in plans:
        row = [
            p['name'],
            f"¥{p['first_month']:.1f}",
            f"¥{p['renewal']:.1f}",
            f"¥{p['annual']:.1f}",
            p['pros']
        ]
        print(format_row(row, widths, aligns))

    print("-" * 92)
    cursor_annual = (145.0 * 12) * team
    volc_annual = (9.41 + 40.0 * 11) * team
    saved_volc = cursor_annual - volc_annual
    print(f"\n💡 算账结论：")
    print(f"  1. 相比海外 Cursor Pro (年费 ¥{cursor_annual:.0f})，改选火山方舟国内套餐 (年费 ¥{volc_annual:.0f})，")
    print(f"     每年立省 ¥{saved_volc:.0f} (节约约 {saved_volc/cursor_annual*100:.1f}%)！")
    print(f"  2. 全天候 Agent 挂机推荐：腾讯云双11特惠轻量服务器 (4核4G，¥38/年) + 火山方舟/阿里百炼组合。")
    print(f"\n👉 在线完整比价大表、活动下线实时日志与交互式账单计算器：")
    print(f"   https://coding.mybskm.top/")
    print("=" * 88)
    return 0

def main():
    parser = argparse.ArgumentParser(description="国内 AI 编程套餐真实算账对比工具")
    parser.add_argument('--hours', type=float, default=4.0, help="每天开发使用时长（小时），默认 4.0")
    parser.add_argument('--mode', choices=['completion', 'refactor', 'agent'], default='agent', help="使用模式：completion(轻度补全) / refactor(重度重构) / agent(全天候Agent)")
    parser.add_argument('--team', type=int, default=1, help="团队开发者人数，默认 1")
    args = parser.parse_args()
    return run_calc(args.hours, args.mode, args.team)

if __name__ == '__main__':
    sys.exit(main())
