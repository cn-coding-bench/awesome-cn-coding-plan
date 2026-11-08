# Awesome CN Coding Plan · 国内主流 AI 编程套餐（Coding Plan / Token Plan）实测额度与避坑对比

> 🚀 **专为国内 Claude Code / Cursor / Cline / Roo Code / OpenCode 开发者整理的 AI 编程套餐（Coding Plan / Token Plan）实测排雷、限流对比与月度成本计算工具！**
>
> 📅 **最后全网人工核验：2026-10-30** | 📊 **在线交互式账单计算器：[coding.mybskm.top](https://coding.mybskm.top/)** | 📜 **开源协议：MIT**
>
> 💡 **利益相关与合规说明**：本开源比价仓由独立开发者维护，包含部分云厂商推广/CPS返利链接（点击购买不会增加您的任何支出，所获佣金用于维护基准测试与服务器带宽）。价格与活动以各云厂商官方最新页面为准，动态浮动档位已显式注明。

---

## ⚡ 10月底/11月最新排雷预警（真人老手吐槽，一针见血）

国内大厂的 AI 编程套餐近期变动极快，不少看似便宜的活动已经悄悄下线或大改规则，购买前务必看清避坑：

1. **腾讯云原 Coding Plan 页面已正式下线（旧短链直接 302 跳转失效页）**：
   - ⚠️ 原本的独立 Coding Plan 页面已停运，现已拆分为 **通用 Token Plan（¥28/月起，支持混元/DeepSeek/GLM 积分池）** 与 **WorkBuddy AI 编程助手**。别再找旧入口了！
   - 💡 **高性价比组合**：如果要挂 24 小时全自动编程 Agent 或自建远程开发环境，推荐走双 11 轻量云特惠通道（**4核4G 8M 仅 ¥38/年**），成本几乎可以忽略不计。
2. **智谱 GLM「拼好模」特惠活动已终止**：
   - ⚠️ 曾经风靡一时的拼好模已关闭，`/glm-coding` 官方常规 Lite 连续包月价格为 **¥94.4/月**，且在晚间高峰期偶尔出现并发排队。
   - 💡 **避坑策略**：中轻度开发者千万别一上来就无脑充月包！建议先走**官方实名拉新入口免费领取 2,000 万免费 Tokens 资源包**，测清自己在 Claude Code / OpenCode 中的真实消耗再作决定。
3. **阿里云百炼 Coding Plan（千问代码模型口碑稳，但热门档位需蹲点）**：
   - ⚠️ 百炼的通义千问 Qwen3.8-Max / Coder 在代码多文件重构与工具调用上极其扎实、国内直连延迟极低，但入门级和超低折扣档位经常库存紧张，往往需要早上 09:30 准点抢购。
4. **字节火山方舟 Coding Plan（当前免抢购首月性价比王者）**：
   - 💡 **实测推荐**：同时整合了 DeepSeek-V4.1-Flash、GLM-5.3、Doubao-Seed-Evolving 与 Kimi-K3.1-Pro，支持自由切换与 Auto 智能路由；首月活动叠加推荐 9.5 折后仅 **¥9.4/月**（次月续费 ¥40/月），**关键是不用卡点抢购，现开现用**！

---

## 📊 核心横向对比大表（TL;DR 价格、可用模型、限流槽点与直达入口）

| 服务商与套餐 | 真实费用 (首月/续费) | 包含主力模型 | 限流机制与主要槽点 | 最佳适用场景 | 官方直达入口 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **字节火山方舟 Coding Plan** | **首月 ¥9.4**<br>次月续费 ¥40/月 | DeepSeek-V4.1-Flash<br>GLM-5.3 / Doubao-Seed<br>Kimi-K3.1-Pro | 极高并发下个别模型轻度抖动；支持 Auto 路由故障自愈 | **首推王者**：不想卡点抢购、想一次体验 4 大主流国产模型的重度开发者 | [火山方舟 9.5折直达](https://coding.mybskm.top/go/volcengine-coding?src=gh_repo_cn_coding_plan) |
| **阿里云百炼 Coding Plan** | **首月 ¥39.9**<br>原价 ¥200/月 (Pro) | 通义千问 Qwen3.8-Max<br>Qwen3.8-Coder | 低价/特惠档位常缺货，需早 09:30 蹲点抢购；按 5 小时周期配额 | 追求国内直连超低延迟、重度依赖千问工具调用稳定性的开发者 | [阿里云百炼直达](https://coding.mybskm.top/go/aliyun-coding?src=gh_repo_cn_coding_plan) |
| **腾讯云通用 Token Plan** | **首月 ¥28 起**<br>日常 ¥39/月 (Lite) | 腾讯混元 Turbo/T1<br>DeepSeek / GLM | 原 Coding Plan 下线；积分池消耗模式，算力并非固定 Token 额度 | 腾讯云现有开发栈、搭配 WorkBuddy 插件或微信小程序生态开发者 | [腾讯云 TokenPlan 直达](https://coding.mybskm.top/go/tencent-workbuddy?src=gh_repo_cn_coding_plan) |
| **智谱 GLM Coding Plan** | **首月免费领 2000万**<br>连续包月 ¥94.4/月 | 智谱 GLM-5.3<br>GLM-5.3-Flash | 拼好模已下线；晚高峰偶有并发排队；直接买月包单价偏高 | 长文本上下文重构、学术/技术写作、智谱原生工具链重度用户 | [领 2000万Tokens](https://coding.mybskm.top/go/zhipu-glm?src=gh_repo_cn_coding_plan) |
| **腾讯云双11特惠轻量云** | **特惠 ¥38/年**<br>(4核4G 8M带宽) | Linux / Docker / 环境 | 仅限新客首年特惠；需搭配模型 API 使用 | **24 小时挂机神器**：云端部署自动化 Agent、Cline、OpenCode 环境 | [双11大促专区](https://coding.mybskm.top/go/tencent-double11?src=gh_repo_cn_coding_plan) / [轻量专区](https://coding.mybskm.top/go/tencent-lighthouse?src=gh_repo_cn_coding_plan) |
| **阿里云 ECS / GPU 算力** | **云大使活动专享特惠** | e-实例 / 开发者 GPU 容器 | 实例到期前需留意续费策略；需自备开源模型部署调试经验 | 自建开源大模型、DeepSeek 满血版私有化推理与量化部署 | [云大使直达](https://coding.mybskm.top/go/aliyun-dashi?src=gh_repo_cn_coding_plan) / [GPU算力专区](https://coding.mybskm.top/go/aliyun-gpu?src=gh_repo_cn_coding_plan) |
| **雨云免备案开发机** | **¥15/月 起** | KVM VPS / 高防节点 | 适合轻量级环境调试与开发环境代理 | 免备案需求、跨境网络环境优化、辅助开发环境搭建 | [雨云专区直达](https://coding.mybskm.top/go/rainyun?src=gh_repo_cn_coding_plan) |
| **海外 Cursor Pro (对照组)** | **$20/月 (约 ¥145)**<br>无首月折扣 | Claude 3.5 Sonnet<br>GPT-4o | 需海外信用卡与高额代付溢价；存在网络风控与封号风险 | 原生 IDE 深度依赖者、预算充足且具备可靠外币支付手段的用户 | [官网自理](https://cursor.com) |
| **海外 Claude Pro (对照组)** | **$20/月 (约 ¥145)**<br>无首月折扣 | Claude 3.5 Sonnet<br>Haiku 3.5 | 严格的 5 小时高频调用次数墙；严查 IP 代理导致误封号 | 必须使用 Claude 官方 Web 端或官方原生 CLI 的团队 | [官网自理](https://claude.com) |

---

## 💰 3 种典型开发强度的月度/年度真实算例（算清账本）

### 算例 1：轻度日常代码补全（每天约 2 小时，月消耗 ~1,500 万 Tokens）
- **海外方案（Cursor Pro）**：$20/月 ≈ ¥145/月，年成本 **¥1,740**。
- **国内方案**：智谱实名先领 2,000 万免费 Tokens（首月 ¥0） + 字节火山方舟首月（¥9.4） + 次月起火山方舟（¥40/月），年总成本约 **¥449**。
- 💵 **每年立省**：`¥1,740 - ¥449 =` **¥1,291（节约 74%）**！

### 算例 2：中重度 Claude Code / Cline 多文件重构（每天 4–6 小时，月消耗 ~6,000 万–1 亿 Tokens）
- **海外方案（Claude Pro + Cursor 双开）**：$40/月 ≈ ¥290/月，年成本 **¥3,480**。
- **国内方案**：火山方舟 Auto 模式（¥40/月）多模型轮询轮换 + 阿里百炼千问主力兜底，年总成本约 **¥480 ～ ¥960**。
- 💵 **每年立省**：`¥3,480 - ¥720 ≈` **¥2,760（节约 79%）**！

### 算例 3：全天候全自动 Agent 挂机 / 团队自动化流水线（24 小时不间断运行）
- **海外方案（AWS 云主机 + Claude Max 配额）**：$130+/月 ≈ ¥940+/月，年成本 **¥11,280+**。
- **国内方案**：腾讯云双 11 特惠轻量服务器 4核4G（**¥38/年**）作为 24h 挂机宿主 + 火山方舟/阿里百炼 API，年总成本仅约 **¥518 ～ ¥1,238**。
- 💵 **每年立省**：**¥10,000+**！

---

## 🛠️ 本地 CLI 算账工具使用说明

本仓库提供零依赖的 Python 算账命令行工具，既支持 PyPI 官方包免克隆直接安装运行，也支持克隆后直接运行：

```bash
# 方式 A：通过 PyPI 官方包一键安装运行（推荐）
pip install -U cn-coding-plan
cn-coding-plan --hours 4 --mode refactor --team 1

# 方式 B：本地直接运行脚本
python3 calc_coding_plan.py --hours 6 --mode refactor --team 3
```

---

## 🌐 深度避坑专题与在线计算器入口

如果需要更详尽的配置教程、活动下线历史或在线实时计算，欢迎访问我们维护的专题知识库：

- 🧮 **[在线交互式月度账单计算器](https://coding.mybskm.top/)**：动态拖拽工时、即时出具个性化推荐。
- 📜 **[各厂商活动下线与改版实时日志](https://coding.mybskm.top/changelog.html)**：第一时间掌握官方暗改与套餐下线动态。
- 🤖 **[Claude Code 国内直连百炼/火山/智谱配置与成本实测](https://coding.mybskm.top/claude-code-cn.html)**：手把手教你免代理流畅接入。
- ⚖️ **[Cursor Pro $20/月太贵？国内平替方案全方位对比](https://coding.mybskm.top/cursor-alternative.html)**：深度拆解替代可行性。
- 🔍 **[腾讯云 Coding Plan 下线后 Token Plan 与 WorkBuddy 实测](https://coding.mybskm.top/tencent-token-plan-workbuddy.html)**：解构新版积分规则。
- 🧪 **[智谱拼好模下线后 GLM-5.3 免费 Token 与套餐选型指南](https://coding.mybskm.top/zhipu-glm-coding-plan.html)**：不花冤枉钱的领券姿势。
- 🖥️ **[24 小时挂机跑 Claude Code / OpenCode Agent 的基础设施账单](https://coding.mybskm.top/claude-code-24h-agent-vps-isp-guide.html)**：双 ISP 原生住宅 VPS / CN2 GIA / 轻量云三方案拆账。
- 🔒 **[百炼 Coding Plan 晚高峰限流降速与额度抢购排雷指南](https://coding.mybskm.top/aliyun-bailian-coding-plan-quota-throttling.html)**：官方三层配额机制与双开分流避坑，双开月费不到 Cursor Pro 四分之一，附 `pipx run cn-coding-plan` 算账命令。

---

---

## 💳 海外订阅与出海开发生态推荐

如果你仍需要订阅 Cursor Pro / Claude 官方服务，或需要搭建低延迟、防风控的开发/跨境运行环境：

| 产品 | 特点与适用场景 | 官方入口 |
| :--- | :--- | :--- |
| **海外订阅防封与免外卡平替** | 丽萨双 ISP 原生住宅 IP 防封底座与国内百炼/GLM 免外卡直连方案对比 | [防封总账单](https://coding.mybskm.top/cursor-claude-pro-virtual-card-and-isp-ip.html) |
| **丽萨主机 LisaHost** | 美区/港区双 ISP 原生家宽纯净住宅 IP VPS，支持支付宝付款，海外开发与 API 访问成本测算 | [丽萨主机官网](https://coding.mybskm.top/go/lisahost?src=gh_repo_cn_coding_plan) |
| **搬瓦工 BWH** | 顶级 CN2 GIA / 软银高速回国线路 VPS，超低延迟与大带宽，海外 API 转发与常驻主机枢纽 | [搬瓦工高速方案](https://coding.mybskm.top/go/bwh?src=gh_repo_cn_coding_plan) |
| **跨境防关联 BOM 计算器** | 出海多店铺 / TikTok 真机云手机 vs 指纹浏览器 + 双 ISP 原生住宅 IP 月度成本在线测算（支持 `pipx run cbcost-calc`） | [在线成本计算器](https://cbcost.mybskm.top/) |

## 🤝 贡献与开源许可

- 本项目数据每周持续核验更新。如发现厂商价格或限流规则变动，欢迎提交 Issue 或 PR。
- 遵循 [MIT License](LICENSE) 开源协议。

## 四仓互链：网络环境防风控与成本测算

| 仓库 | 用途 |
| --- | --- |
| [awesome-cn-coding-plan](https://github.com/cn-coding-bench/awesome-cn-coding-plan) | 编程订阅对比 |
| [crossborder-multi-shop-bom-calculator](https://github.com/cn-coding-bench/crossborder-multi-shop-bom-calculator) | 多店铺 BOM |
| [claude-code-cn-setup-and-vps-guide](https://github.com/cn-coding-bench/claude-code-cn-setup-and-vps-guide) | 开发环境与 VPS |
| [tiktok-cloudphone-vs-residential-isp-proxy](https://github.com/cn-coding-bench/tiktok-cloudphone-vs-residential-isp-proxy) | 云手机与住宅 IP |

基准算例：$20 订阅按 7.25 折算约 ¥145 + 丽萨双 ISP 原生住宅 VPS ¥68 + 虚拟卡开卡/充值汇损按约 ¥7–15 估算，月均测算基准约 ¥220（区间 ¥220–228）。费用为预算假设，不是实时套餐报价；开卡费与充值汇损需拆开填写，避免重复计费。

| 预算项 | 首月实付现金（测算） | 稳态月均摊销成本 |
| --- | --- | --- |
| 按月订阅 + VPS + 每月汇损 ¥7 | ¥220 + 实际开卡费 | ¥220 |
| 年付 VPS（假设同价 ¥816/年） | ¥968 + 实际开卡费 | ¥220 |

一次性开卡费仅进入首月现金；首年摊销另加开卡费 ÷ 12，续年不重复计入。
