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
- 可选: `nodejs` (部分来源仓库脚本需要), `pip` (部分 Python 技能附带工具脚本)
- DeerFlow 端要求: 接收 `SKILL.md` frontmatter，建议字段 `name/description/version/author/compatibility`

## 一键流程

```bash
cd /root/deerflow-skill-hub-offline
bash scripts/mirror_repos.sh data/seed_repos_top20.txt
python3 scripts/normalize_to_deerflow.py --mirrors mirrors --out output/skills/custom
bash scripts/pack_skill_archives.sh output/skills/custom dist
```

把 `dist/*.skill` 通过 DeerFlow Gateway 安装即可。

## Top 60 逐项作用与测试清单

| # | Repo | 具体作用 | 你要测试什么 | 依赖 | 兼容/离线 |
|---|---|---|---|---|---|
| 2 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 界面/体验设计类技能或模板。 | 给一个产品需求，验证是否输出可执行的页面/组件设计规范。 | Python | medium/medium |
| 4 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | 通用技能仓库：cherry-studio。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/medium |
| 8 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | 面向 Codex/通用 coding agent 的技能包。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/medium |
| 9 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Obsidian 工作流技能，增强文档与知识管理。 | 对示例 vault 执行结构化任务，验证 Markdown/Canvas 操作链路。 | None (Markdown/Config-only or unknown) | high/high |
| 10 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 界面/体验设计类技能或模板。 | 给一个产品需求，验证是否输出可执行的页面/组件设计规范。 | Python | high/high |
| 11 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | SEO/GEO 审计与内容优化技能集。 | 输入一个站点 URL，检查是否产出结构化 SEO 诊断与修复建议。 | Node.js | high/medium |
| 12 | [openai/skills](https://github.com/openai/skills) | 面向 Codex/通用 coding agent 的技能包。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Python | medium/medium |
| 13 | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 多代理/子代理编排技能集合。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | medium/medium |
| 16 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 面向 Codex/通用 coding agent 的技能包。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/medium |
| 17 | [blader/humanizer](https://github.com/blader/humanizer) | 通用技能仓库：humanizer。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/medium |
| 19 | [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 技能索引仓库，用于选型和批量引入。 | 随机抽取 3 个条目镜像并转换，验证可被 DeerFlow 识别加载。 | None (Markdown/Config-only or unknown) | medium/medium |
| 20 | [diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) | 通用技能仓库：claude-code-infrastructure-showcase。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | medium/medium |
| 21 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 界面/体验设计类技能或模板。 | 给一个产品需求，验证是否输出可执行的页面/组件设计规范。 | Python | medium/medium |
| 23 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 通用技能仓库：claude-skills。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Python | high/medium |
| 24 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 游戏开发流程代理与技能编排。 | 输入游戏需求，验证是否拆出角色分工与阶段性交付。 | None (Markdown/Config-only or unknown) | medium/medium |
| 25 | [refly-ai/refly](https://github.com/refly-ai/refly) | 界面/体验设计类技能或模板。 | 给一个产品需求，验证是否输出可执行的页面/组件设计规范。 | Node.js | high/high |
| 26 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | 面向 Codex/通用 coding agent 的技能包。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | high/medium |
| 27 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 研究型工作流技能（检索-分析-汇总）。 | 输入研究问题，验证是否产出多步骤检索与证据汇总模板。 | None (Markdown/Config-only or unknown) | high/medium |
| 28 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 通用技能仓库：ai-website-cloner-template。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/medium |
| 29 | [dontriskit/awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) | 界面/体验设计类技能或模板。 | 给一个产品需求，验证是否输出可执行的页面/组件设计规范。 | Node.js | medium/high |
| 30 | [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | 流程化执行与计划管理技能。 | 输入复杂任务，验证是否先生成阶段计划再执行。 | Node.js | medium/high |
| 31 | [slavingia/skills](https://github.com/slavingia/skills) | 通用技能仓库：skills。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/medium |
| 32 | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 通用技能仓库：Humanizer-zh。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/medium |
| 33 | [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | NotebookLM 集成技能，用于知识库问答。 | 连接测试知识库后提问，验证回答是否引用知识源。 | Python | medium/medium |
| 35 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | SEO/GEO 审计与内容优化技能集。 | 输入一个站点 URL，检查是否产出结构化 SEO 诊断与修复建议。 | Python | medium/medium |
| 36 | [vijaythecoder/awesome-claude-agents](https://github.com/vijaythecoder/awesome-claude-agents) | 通用技能仓库：awesome-claude-agents。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | medium/medium |
| 37 | [trailofbits/skills](https://github.com/trailofbits/skills) | 安全审计与漏洞研究技能集。 | 用示例代码仓触发审计任务，验证是否给出可复现风险与修复建议。 | Python | high/medium |
| 38 | [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) | 界面/体验设计类技能或模板。 | 给一个产品需求，验证是否输出可执行的页面/组件设计规范。 | None (Markdown/Config-only or unknown) | high/medium |
| 40 | [zgsm-ai/costrict](https://github.com/zgsm-ai/costrict) | 通用技能仓库：costrict。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/medium |
| 44 | [twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill) | 界面/体验设计类技能或模板。 | 给一个产品需求，验证是否输出可执行的页面/组件设计规范。 | None (Markdown/Config-only or unknown) | medium/medium |
| 47 | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | 界面/体验设计类技能或模板。 | 给一个产品需求，验证是否输出可执行的页面/组件设计规范。 | Python | medium/medium |
| 48 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | 研究型工作流技能（检索-分析-汇总）。 | 输入研究问题，验证是否产出多步骤检索与证据汇总模板。 | None (Markdown/Config-only or unknown) | medium/medium |
| 50 | [intellectronica/ruler](https://github.com/intellectronica/ruler) | 通用技能仓库：ruler。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/high |
| 51 | [Dimillian/Skills](https://github.com/Dimillian/Skills) | 面向 Codex/通用 coding agent 的技能包。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/medium |
| 52 | [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | 通用技能仓库：codebase-to-course。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/medium |
| 53 | [eze-is/web-access](https://github.com/eze-is/web-access) | 通用技能仓库：web-access。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/medium |
| 54 | [htdt/godogen](https://github.com/htdt/godogen) | 界面/体验设计类技能或模板。 | 给一个产品需求，验证是否输出可执行的页面/组件设计规范。 | Python | high/medium |
| 55 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | 面向 Codex/通用 coding agent 的技能包。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Python | medium/medium |
| 58 | [axtonliu/axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills) | Obsidian 工作流技能，增强文档与知识管理。 | 对示例 vault 执行结构化任务，验证 Markdown/Canvas 操作链路。 | None (Markdown/Config-only or unknown) | medium/medium |
| 59 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | 通用技能仓库：dbskill。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/medium |
| 60 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | 通用技能仓库：agent-skills。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/medium |
| 63 | [glittercowboy/taches-cc-resources](https://github.com/glittercowboy/taches-cc-resources) | 通用技能仓库：taches-cc-resources。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | medium/high |
| 65 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 研究型工作流技能（检索-分析-汇总）。 | 输入研究问题，验证是否产出多步骤检索与证据汇总模板。 | Python | high/high |
| 66 | [coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill) | 通用技能仓库：excalidraw-diagram-skill。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Python | medium/medium |
| 68 | [tanweai/wooyun-legacy](https://github.com/tanweai/wooyun-legacy) | 通用技能仓库：wooyun-legacy。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | medium/medium |
| 69 | [gadievron/raptor](https://github.com/gadievron/raptor) | 安全审计与漏洞研究技能集。 | 用示例代码仓触发审计任务，验证是否给出可复现风险与修复建议。 | Python | medium/high |
| 70 | [nexu-io/nexu](https://github.com/nexu-io/nexu) | 面向 Codex/通用 coding agent 的技能包。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/high |
| 71 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | 安全审计与漏洞研究技能集。 | 用示例代码仓触发审计任务，验证是否给出可复现风险与修复建议。 | Python | medium/medium |
| 72 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | 通用技能仓库：android-reverse-engineering-skill。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/medium |
| 73 | [YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill](https://github.com/YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill) | 多媒体生成/处理技能。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/high |
| 75 | [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) | 多代理/子代理编排技能集合。 | 随机抽取 3 个条目镜像并转换，验证可被 DeerFlow 识别加载。 | Python | high/medium |
| 76 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | 通用技能仓库：videocut-skills。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | high/medium |
| 80 | [skills-directory/skill-codex](https://github.com/skills-directory/skill-codex) | 面向 Codex/通用 coding agent 的技能包。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/high |
| 81 | [itsmostafa/aws-agent-skills](https://github.com/itsmostafa/aws-agent-skills) | 通用技能仓库：aws-agent-skills。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Python | high/medium |
| 82 | [Prat011/awesome-llm-skills](https://github.com/Prat011/awesome-llm-skills) | 技能索引仓库，用于选型和批量引入。 | 随机抽取 3 个条目镜像并转换，验证可被 DeerFlow 识别加载。 | Python | high/medium |
| 83 | [instructa/ai-prompts](https://github.com/instructa/ai-prompts) | 技能索引仓库，用于选型和批量引入。 | 随机抽取 3 个条目镜像并转换，验证可被 DeerFlow 识别加载。 | Node.js | medium/high |
| 84 | [rohunvora/x-research-skill](https://github.com/rohunvora/x-research-skill) | 研究型工作流技能（检索-分析-汇总）。 | 输入研究问题，验证是否产出多步骤检索与证据汇总模板。 | Node.js | medium/medium |
| 85 | [Shpigford/chops](https://github.com/Shpigford/chops) | 面向 Codex/通用 coding agent 的技能包。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | None (Markdown/Config-only or unknown) | high/medium |
| 86 | [jarrodwatts/claude-code-config](https://github.com/jarrodwatts/claude-code-config) | 通用技能仓库：claude-code-config。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Node.js | medium/high |
| 87 | [wuji-labs/nopua](https://github.com/wuji-labs/nopua) | 通用技能仓库：nopua。 | 执行一次最小任务样例，确认能被转换并在 DeerFlow 中启用。 | Python | medium/high |

## 说明

- `deerflow_compat=high`: 通常已是 skill/workflow 形态，改造成本低。
- `deerflow_compat=medium`: 规则/提示词/工具集合，需要轻度包装。
- `offline_readiness=high`: 以 markdown/rules 为主，脱网可直接运行。
- `offline_readiness=medium`: 核心可离线，但部分能力可能依赖外部 API/MCP。
