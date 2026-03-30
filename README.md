# DeerFlow Offline Skill Hub

企业离线场景的技能聚合与适配仓库。

## 数据范围

- 抓取时间: 2026-03-30
- GitHub 检索关键词: `claude code skills`、`filename:SKILL.md agent skills`、`cursor rules ai coding`、`roo code modes`、`codex skills` 等
- 聚合候选仓库: 180
- 可用短名单: 103
- 企业离线优先: 60

## 目录

- `data/catalog.json|csv`: 完整候选池
- `data/shortlist.json`: 可落地短名单
- `data/enterprise_offline_top60.json`: 企业离线优先清单
- `data/seed_repos_top20.txt`: 默认镜像源
- `scripts/mirror_repos.sh`: 批量镜像仓库
- `scripts/normalize_to_deerflow.py`: 转换为 DeerFlow `SKILL.md` 结构
- `scripts/pack_skill_archives.sh`: 打包 `.skill`

## 环境依赖

- 必需: `git`, `jq`, `python3`, `zip`
- 可选: `nodejs` (部分来源仓库自身脚本需要), `pip` (部分 Python 技能附带工具脚本)
- DeerFlow 端要求: 接收 `SKILL.md` frontmatter，建议字段 `name/description/version/author/compatibility`

## 一键流程

```bash
cd /root/deerflow-skill-hub-offline
bash scripts/mirror_repos.sh data/seed_repos_top20.txt
python3 scripts/normalize_to_deerflow.py --mirrors mirrors --out output/skills/custom
bash scripts/pack_skill_archives.sh output/skills/custom dist
```

把 `dist/*.skill` 通过 DeerFlow Gateway 安装即可。

## Top 30 (企业离线优先)

| # | Repo | Stars | DeerFlow兼容 | 离线可用 | 依赖 |
|---|---|---:|---|---|---|
| 2 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 54546 | medium | medium | Python |
| 4 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | 42584 | medium | medium | Node.js |
| 8 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | 20501 | medium | medium | Node.js |
| 9 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 18230 | high | high | None (Markdown/Config-only or unknown) |
| 10 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 17619 | high | high | Python |
| 11 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 17481 | high | medium | Node.js |
| 12 | [openai/skills](https://github.com/openai/skills) | 15714 | medium | medium | Python |
| 13 | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 15617 | medium | medium | None (Markdown/Config-only or unknown) |
| 16 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 13362 | high | medium | None (Markdown/Config-only or unknown) |
| 17 | [blader/humanizer](https://github.com/blader/humanizer) | 11598 | high | medium | None (Markdown/Config-only or unknown) |
| 19 | [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 10085 | medium | medium | None (Markdown/Config-only or unknown) |
| 20 | [diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) | 9373 | medium | medium | None (Markdown/Config-only or unknown) |
| 21 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 8222 | medium | medium | Python |
| 23 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 7470 | high | medium | Python |
| 24 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 7340 | medium | medium | None (Markdown/Config-only or unknown) |
| 25 | [refly-ai/refly](https://github.com/refly-ai/refly) | 7123 | high | high | Node.js |
| 26 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | 7050 | high | medium | Node.js |
| 27 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 5839 | high | medium | None (Markdown/Config-only or unknown) |
| 28 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 5830 | medium | medium | Node.js |
| 29 | [dontriskit/awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) | 5646 | medium | high | Node.js |
| 30 | [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | 5608 | medium | high | Node.js |
| 31 | [slavingia/skills](https://github.com/slavingia/skills) | 5534 | high | medium | None (Markdown/Config-only or unknown) |
| 32 | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 5302 | high | medium | None (Markdown/Config-only or unknown) |
| 33 | [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | 5279 | medium | medium | Python |
| 35 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | 4499 | medium | medium | Python |
| 36 | [vijaythecoder/awesome-claude-agents](https://github.com/vijaythecoder/awesome-claude-agents) | 4110 | medium | medium | None (Markdown/Config-only or unknown) |
| 37 | [trailofbits/skills](https://github.com/trailofbits/skills) | 4097 | high | medium | Python |
| 38 | [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) | 3904 | high | medium | None (Markdown/Config-only or unknown) |
| 40 | [zgsm-ai/costrict](https://github.com/zgsm-ai/costrict) | 3836 | medium | medium | Node.js |
| 44 | [twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill) | 3244 | medium | medium | None (Markdown/Config-only or unknown) |

## 说明

- `deerflow_compat=high`: 通常已是 skill/workflow 形态，改造成本低
- `deerflow_compat=medium`: 规则/提示词/工具集合，需要轻度包装
- `offline_readiness=high`: 以 markdown/rules 为主，脱网可直接运行
- `offline_readiness=medium`: 核心可离线，但部分能力可能依赖外部 API/MCP
