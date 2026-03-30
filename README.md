# DeerFlow Offline Skill Hub

面向企业离线场景的技能聚合与适配仓库（深度分析版）。

## 数据与方法

- 数据时间: 2026-03-30
- 范围: 180 候选 -> 103 短名单 -> 60 企业离线优先
- 分析输入: GitHub 仓库元数据 + README 摘要 + 本地兼容评分
- 输出目标: 每个仓库都给出“作用、边界、适配方式、测试步骤”

## 使用流程

```bash
cd /root/deerflow-skill-hub-offline
bash scripts/mirror_repos.sh data/seed_repos_top20.txt
python3 scripts/normalize_to_deerflow.py --mirrors mirrors --out output/skills/custom
bash scripts/pack_skill_archives.sh output/skills/custom dist
```

## 60 项逐仓库深度分析

### 2. nextlevelbuilder/ui-ux-pro-max-skill
- 仓库链接: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- 角色定位: 界面与产品设计
- 主要作用: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 4. CherryHQ/cherry-studio
- 仓库链接: https://github.com/CherryHQ/cherry-studio
- 角色定位: 游戏与多代理制作流
- 主要作用: AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=medium
- 许可证: AGPL-3.0
- 建议测试步骤:
  - 输入游戏需求，检查多角色拆分。
  - 验证阶段产物是否可交接。
  - 单模块返工后检查全流程稳定性。

### 8. iOfficeAI/AionUi
- 仓库链接: https://github.com/iOfficeAI/AionUi
- 角色定位: 界面与产品设计
- 主要作用: Free, local, open-source 24/7 Cowork app and OpenClaw for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it!
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=medium
- 许可证: Apache-2.0
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 9. kepano/obsidian-skills
- 仓库链接: https://github.com/kepano/obsidian-skills
- 角色定位: 知识管理与文档自动化
- 主要作用: Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI.
- 能力补充: Agent Skills for use with Obsidian. These skills follow the . See more in the . See the Agent Skills specification
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 对文档集合执行整理任务。
  - 检查 Markdown/Canvas 等格式输出是否稳定。
  - 离线重复执行确认一致。

### 10. OthmanAdi/planning-with-files
- 仓库链接: https://github.com/OthmanAdi/planning-with-files
- 角色定位: 安全与攻防
- 主要作用: Claude Code skill implementing Manus-style persistent markdown planning — the workflow pattern behind the $2B acquisition.
- 能力补充: Planning with Files Work like Manus — the AI agent company Meta acquired for $2 billion . ! Closed Issues ! Closed PRs ! Benchmark ! A/B Verified ! Security Verified 💬 A Note from ...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=high, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 用含缺陷样例项目触发审计。
  - 验证输出是否含复现步骤与修复建议。
  - 在隔离环境复跑确认稳定。

### 11. coreyhaines31/marketingskills
- 仓库链接: https://github.com/coreyhaines31/marketingskills
- 角色定位: 营销与增长
- 主要作用: Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.
- 能力补充: Marketing Skills for AI Agents A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who want AI coding agents to help with convers...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入真实站点 URL，检查是否产出结构化诊断。
  - 验证建议是否含优先级与收益预估。
  - 导出 DeerFlow 报告并复跑一次确认一致。

### 12. openai/skills
- 仓库链接: https://github.com/openai/skills
- 角色定位: 通用 AI Agent 技能
- 主要作用: Skills Catalog for Codex
- 能力补充: Agent Skills Agent Skills are folders of instructions, scripts, and resources that AI agents can discover and use to perform at specific tasks. Write once, use everywhere. Codex us...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=medium
- 许可证: Unknown
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 13. VoltAgent/awesome-claude-code-subagents
- 仓库链接: https://github.com/VoltAgent/awesome-claude-code-subagents
- 角色定位: 技能索引与分发
- 主要作用: A collection of 100+ specialized Claude Code subagents covering a wide range of development use cases
- 能力补充: The awesome collection of Claude Code subagents. ! Awesome ! Subagent Count ! Last Update ! Discord
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 随机抽取 3 个条目镜像并转换。
  - 检查来源、许可证、依赖元数据完整性。
  - 比对转换前后语义漂移。

### 16. VoltAgent/awesome-agent-skills
- 仓库链接: https://github.com/VoltAgent/awesome-agent-skills
- 角色定位: 技能索引与分发
- 主要作用: Claude Code Skills and 1000+ agent skills from official dev teams and the community, compatible with Codex, Antigravity, Gemini CLI, Cursor and others.
- 能力补充: A curated collection of official Agent Skills from leading development teams and the community. ! Awesome ! Skills Count ! Last Update ! Discord
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 随机抽取 3 个条目镜像并转换。
  - 检查来源、许可证、依赖元数据完整性。
  - 比对转换前后语义漂移。

### 17. blader/humanizer
- 仓库链接: https://github.com/blader/humanizer
- 角色定位: 通用 AI Agent 技能
- 主要作用: Claude Code skill that removes signs of AI-generated writing from text
- 能力补充: Humanizer A Claude Code skill that removes signs of AI-generated writing from text, making it sound more natural and human. Installation Recommended clone directly into Claude Code...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 19. travisvn/awesome-claude-skills
- 仓库链接: https://github.com/travisvn/awesome-claude-skills
- 角色定位: 技能索引与分发
- 主要作用: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows — particularly Claude Code
- 能力补充: Awesome Claude Skills ! Awesome ! Last Updated ! PRs Welcome A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows Claude Skills teach C...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=medium
- 许可证: Unknown
- 建议测试步骤:
  - 随机抽取 3 个条目镜像并转换。
  - 检查来源、许可证、依赖元数据完整性。
  - 比对转换前后语义漂移。

### 20. diet103/claude-code-infrastructure-showcase
- 仓库链接: https://github.com/diet103/claude-code-infrastructure-showcase
- 角色定位: 技能索引与分发
- 主要作用: Examples of my Claude Code infrastructure with skill auto-activation, hooks, and agents
- 能力补充: Claude Code Infrastructure Showcase A curated reference library of production-tested Claude Code infrastructure. Born from 6 months of real-world use managing a complex TypeScript ...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 随机抽取 3 个条目镜像并转换。
  - 检查来源、许可证、依赖元数据完整性。
  - 比对转换前后语义漂移。

### 21. teng-lin/notebooklm-py
- 仓库链接: https://github.com/teng-lin/notebooklm-py
- 角色定位: 界面与产品设计
- 主要作用: Unofficial Python API and agentic skill for Google NotebookLM. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw.
- 能力补充: notebooklm-py A Comprehensive NotebookLM Skill & Unofficial Python API. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Pytho...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 23. Jeffallan/claude-skills
- 仓库链接: https://github.com/Jeffallan/claude-skills
- 角色定位: 技能索引与分发
- 主要作用: 66 Specialized Skills for Full-Stack Developers. Transform Claude Code into your expert pair programmer.
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 随机抽取 3 个条目镜像并转换。
  - 检查来源、许可证、依赖元数据完整性。
  - 比对转换前后语义漂移。

### 24. Donchitos/Claude-Code-Game-Studios
- 仓库链接: https://github.com/Donchitos/Claude-Code-Game-Studios
- 角色定位: 界面与产品设计
- 主要作用: Turn Claude Code into a full game dev studio — 48 AI agents, 36 workflow skills, and a complete coordination system mirroring real studio hierarchy.
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 25. refly-ai/refly
- 仓库链接: https://github.com/refly-ai/refly
- 角色定位: 界面与产品设计
- 主要作用: The first open-source agent skills builder. Define skills by vibe workflow, run on Claude Code, Cursor, Codex & more. Build Clawdbot 🦞· APIs for Lovable · Bots for Slack & Lark/Feishu · Skills are infrastructure, not prompts.
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: Node.js
- 兼容评级: deerflow=high, offline=high
- 许可证: NOASSERTION
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 26. Lum1104/Understand-Anything
- 仓库链接: https://github.com/Lum1104/Understand-Anything
- 角色定位: 通用 AI Agent 技能
- 主要作用: Claude Code skills that turn any codebase into an interactive knowledge graph you can explore, search, and ask questions about (Multi-platform e.g., Codex are supported).
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 27. Orchestra-Research/AI-Research-SKILLs
- 仓库链接: https://github.com/Orchestra-Research/AI-Research-SKILLs
- 角色定位: 研究与知识工作流
- 主要作用: Comprehensive open-source library of AI research and engineering skills for any AI model. Package the skills and your claude code/codex/gemini agent will be an AI research agent with full horsepower. Maintained by Orchestra Research.
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入研究问题，检查是否拆解为多阶段流程。
  - 验证是否给来源证据与反例。
  - 输出结构化报告便于复检。

### 28. JCodesMore/ai-website-cloner-template
- 仓库链接: https://github.com/JCodesMore/ai-website-cloner-template
- 角色定位: 界面与产品设计
- 主要作用: Clone any website with one command using AI coding agents
- 能力补充: AI Website Cloner Template A reusable template for reverse-engineering any website into a clean, modern Next.js codebase using AI coding agents. Recommended: Claude Code with Opus ...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 29. dontriskit/awesome-ai-system-prompts
- 仓库链接: https://github.com/dontriskit/awesome-ai-system-prompts
- 角色定位: 界面与产品设计
- 主要作用: 🧠 Curated collection of system prompts for top AI tools. Perfect for AI agent builders and prompt engineers. Incuding: ChatGPT, Claude, Perplexity, Manus, Claude-Code, Loveable, v0, Grok, same new, windsurf, notion, and MetaAI.
- 能力补充: Crafting Effective Prompts for Agentic AI Systems: Patterns and Practices Table of Contents 7. Safety, Alignment, and Refusal Protocols 7-safety-alignment-and-refus
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 30. ChrisWiles/claude-code-showcase
- 仓库链接: https://github.com/ChrisWiles/claude-code-showcase
- 角色定位: 通用 AI Agent 技能
- 主要作用: Comprehensive Claude Code project configuration example with hooks, skills, agents, commands, and GitHub Actions workflows
- 能力补充: Claude Code Project Configuration Showcase Most software engineers are seriously sleeping on how good LLM agents are right now, especially something like Claude Code. Once you've g...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=high
- 许可证: Unknown
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 31. slavingia/skills
- 仓库链接: https://github.com/slavingia/skills
- 角色定位: 技能索引与分发
- 主要作用: Claude Code skills based on The Minimalist Entrepreneur by Sahil Lavingia
- 能力补充: The Minimalist Entrepreneur — Claude Code Skills Claude Code skills based on The Minimalist Entrepreneur by Sahil Lavingia. Installation In Claude Code: /plugin marketplace add sla...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: Unknown
- 建议测试步骤:
  - 随机抽取 3 个条目镜像并转换。
  - 检查来源、许可证、依赖元数据完整性。
  - 比对转换前后语义漂移。

### 32. op7418/Humanizer-zh
- 仓库链接: https://github.com/op7418/Humanizer-zh
- 角色定位: 通用 AI Agent 技能
- 主要作用: Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。
- 能力补充: Humanizer-zh: AI 写作去痕工具（中文版） 声明： - 本项目的核心文件翻译自 blader/humanizer - 实用工具部分（核心规则、快速检查清单、质量评分）参考了 hardikpandya/stop-slop - 原项目基于维基百科的 Signs of AI writing 指南 --- 项目简介 Humanizer-zh 是一个用于...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 33. PleasePrompto/notebooklm-skill
- 仓库链接: https://github.com/PleasePrompto/notebooklm-skill
- 角色定位: 研究与知识工作流
- 主要作用: Use this skill to enable Claude Code to communicate directly with your Google NotebookLM notebooks. Query your uploaded documents and get source-grounded, citation-backed answers from Gemini. Features browser automation, library management, persistent authentication, and answers exclusively from your own knowledge base.
- 能力补充: NotebookLM Claude Code Skill Let Claude Code chat directly with NotebookLM for source-grounded answers based exclusively on your uploaded documents ! Python ! Claude Code Skill ! B...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入研究问题，检查是否拆解为多阶段流程。
  - 验证是否给来源证据与反例。
  - 输出结构化报告便于复检。

### 35. zubair-trabzada/geo-seo-claude
- 仓库链接: https://github.com/zubair-trabzada/geo-seo-claude
- 角色定位: 营销与增长
- 主要作用: GEO-first SEO skill for Claude Code. Comprehensive AI search optimization for any website — citability scoring, AI crawler analysis, brand authority, schema markup, platform-specific optimization, and PDF reports.  If you want learn how to sell this to real businesses, check out the skool community
- 能力补充: GEO-first, SEO-supported. Optimize websites for AI-powered search engines ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews while maintaining traditional SEO foundations. AI...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入真实站点 URL，检查是否产出结构化诊断。
  - 验证建议是否含优先级与收益预估。
  - 导出 DeerFlow 报告并复跑一次确认一致。

### 36. vijaythecoder/awesome-claude-agents
- 仓库链接: https://github.com/vijaythecoder/awesome-claude-agents
- 角色定位: 界面与产品设计
- 主要作用: An orchestrated sub agent dev team powered by claude code
- 能力补充: Awesome Claude Agents - AI Development Team 🚀 Supercharge Claude Code with a team of specialized AI agents that work together to build complete features, debug complex issues, and ...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 37. trailofbits/skills
- 仓库链接: https://github.com/trailofbits/skills
- 角色定位: 安全与攻防
- 主要作用: Trail of Bits Claude Code skills for security research, vulnerability detection, and audit workflows
- 能力补充: Trail of Bits Skills Marketplace A Claude Code plugin marketplace from Trail of Bits providing skills to enhance AI-assisted security analysis, testing, and development workflows. ...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=high, offline=medium
- 许可证: CC-BY-SA-4.0
- 建议测试步骤:
  - 用含缺陷样例项目触发审计。
  - 验证输出是否含复现步骤与修复建议。
  - 在隔离环境复跑确认稳定。

### 38. czlonkowski/n8n-skills
- 仓库链接: https://github.com/czlonkowski/n8n-skills
- 角色定位: 界面与产品设计
- 主要作用: n8n skillset for Claude Code to build flawless n8n workflows
- 能力补充: n8n-skills Expert Claude Code skills for building flawless n8n workflows using the n8n-mcp MCP server --- 🎯 What is this? This repository contains 7 complementary Claude Code skill...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 40. zgsm-ai/costrict
- 仓库链接: https://github.com/zgsm-ai/costrict
- 角色定位: 界面与产品设计
- 主要作用: Costrict - strict AI coder for enterprises, quality first, including AI Agent, AI CodeReview, AI Completion.
- 能力补充: CoStrict Strict AI Coder for Enterprises Free • Open Source • Private Deployment English --- CoStrict is a free, open-source AI-powered coding assistant designed for enterprise-gra...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=medium
- 许可证: Apache-2.0
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 44. twostraws/SwiftUI-Agent-Skill
- 仓库链接: https://github.com/twostraws/SwiftUI-Agent-Skill
- 角色定位: 界面与产品设计
- 主要作用: SwiftUI agent skill for Claude Code, Codex, and other AI tools.
- 能力补充: SwiftUI Agent Skill for AI Coding Assistants An agent skill that helps AI coding assistants write smarter, simpler, and more modern SwiftUI, including guidance on API usage, design...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 47. deanpeters/Product-Manager-Skills
- 仓库链接: https://github.com/deanpeters/Product-Manager-Skills
- 角色定位: 界面与产品设计
- 主要作用: Product Management skills framework built on battle-tested methods for Claude Code, Cowork, Codex, and AI agents.
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=medium
- 许可证: NOASSERTION
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 48. uditgoenka/autoresearch
- 仓库链接: https://github.com/uditgoenka/autoresearch
- 角色定位: 研究与知识工作流
- 主要作用: Claude Autoresearch Skill — Autonomous goal-directed iteration for Claude Code. Inspired by Karpathy's autoresearch. Modify → Verify → Keep/Discard → Repeat forever.
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入研究问题，检查是否拆解为多阶段流程。
  - 验证是否给来源证据与反例。
  - 输出结构化报告便于复检。

### 50. intellectronica/ruler
- 仓库链接: https://github.com/intellectronica/ruler
- 角色定位: 通用 AI Agent 技能
- 主要作用: Ruler — apply the same rules to all coding agents
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 51. Dimillian/Skills
- 仓库链接: https://github.com/Dimillian/Skills
- 角色定位: 通用 AI Agent 技能
- 主要作用: My Codex Skills
- 能力补充: ! GitHub Pages Skills Public A collection of reusable development skills for Apple platforms, GitHub workflows, refactoring, diff review swarms, bug investigation swarms, code revi...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 52. zarazhangrui/codebase-to-course
- 仓库链接: https://github.com/zarazhangrui/codebase-to-course
- 角色定位: 界面与产品设计
- 主要作用: A Claude Code skill that turns any codebase into a beautiful, interactive single-page HTML course for non-technical vibe coders.
- 能力补充: Codebase to Course A Claude Code skill that turns any codebase into a beautiful, interactive single-page HTML course. Point it at a repo. Get back a stunning, self-contained course...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: Unknown
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 53. eze-is/web-access
- 仓库链接: https://github.com/eze-is/web-access
- 角色定位: 通用 AI Agent 技能
- 主要作用: 给 Claude Code 装上完整联网能力的 skill：三层通道调度 + 浏览器 CDP + 并行分治
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=medium
- 许可证: Unknown
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 54. htdt/godogen
- 仓库链接: https://github.com/htdt/godogen
- 角色定位: 界面与产品设计
- 主要作用: Claude Code skills that build complete Godot 4 projects from a game description
- 能力补充: Godogen: Claude Code skills that build complete Godot 4 projects You describe what you want. An AI pipeline designs the architecture, generates the art, writes every line of code, ...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 55. white0dew/XiaohongshuSkills
- 仓库链接: https://github.com/white0dew/XiaohongshuSkills
- 角色定位: 通用 AI Agent 技能
- 主要作用: 支持小红书自动发布、自动评论、自动检索的 Skill。支持 OpenClaw、Codex、CC 等
- 能力补充: RedBookSkills 自动发布内容到小红书（Xiaohongshu/RED）的命令行工具，也支持仅启动测试浏览器（不发布）。 通过 Chrome DevTools Protocol CDP 实现自动化发布，支持多账号管理、无头模式运行、自动搜索素材与内容数据抓取等功能。 功能特性 - 自动化发布 ：自动填写标题、正文、上传图片 - 创作者中心兼容修复 ...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 58. axtonliu/axton-obsidian-visual-skills
- 仓库链接: https://github.com/axtonliu/axton-obsidian-visual-skills
- 角色定位: 知识管理与文档自动化
- 主要作用: Visual Skills Pack for Obsidian: generate Canvas, Excalidraw, and Mermaid diagrams from text with Claude Code
- 能力补充: Obsidian Visual Skills Pack Visual Skills Pack for Obsidian: generate Canvas, Excalidraw, and Mermaid diagrams from text with Claude Code. Next Step: Want to turn Skills from demo ...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 对文档集合执行整理任务。
  - 检查 Markdown/Canvas 等格式输出是否稳定。
  - 离线重复执行确认一致。

### 59. dontbesilent2025/dbskill
- 仓库链接: https://github.com/dontbesilent2025/dbskill
- 角色定位: 通用 AI Agent 技能
- 主要作用: dontbesilent 的商业诊断 Skills for Claude Code
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: NOASSERTION
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 60. tech-leads-club/agent-skills
- 仓库链接: https://github.com/tech-leads-club/agent-skills
- 角色定位: 营销与增长
- 主要作用: The secure, validated skill registry for professional AI coding agents. Extend Antigravity, Claude Code, Cursor, Copilot and more with absolute confidence.
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=medium
- 许可证: NOASSERTION
- 建议测试步骤:
  - 输入真实站点 URL，检查是否产出结构化诊断。
  - 验证建议是否含优先级与收益预估。
  - 导出 DeerFlow 报告并复跑一次确认一致。

### 63. glittercowboy/taches-cc-resources
- 仓库链接: https://github.com/glittercowboy/taches-cc-resources
- 角色定位: 通用 AI Agent 技能
- 主要作用: A collection of my favorite custom Claude Code resources to make life easier.
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 65. Imbad0202/academic-research-skills
- 仓库链接: https://github.com/Imbad0202/academic-research-skills
- 角色定位: 界面与产品设计
- 主要作用: Academic Research Skills for Claude Code: research → write → review → revise → finalize
- 能力补充: Academic Research Skills for Claude Code A comprehensive suite of Claude Code skills for academic research, covering the full pipeline from research to publication. AI is your copi...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=high, offline=high
- 许可证: NOASSERTION
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 66. coleam00/excalidraw-diagram-skill
- 仓库链接: https://github.com/coleam00/excalidraw-diagram-skill
- 角色定位: 通用 AI Agent 技能
- 主要作用: Skill to give Claude Code (and any coding agent) the ability to generate beautiful and practical Excalidraw diagrams.
- 能力补充: Excalidraw Diagram Skill A coding agent skill that generates beautiful and practical Excalidraw diagrams from natural language descriptions. Not just boxes-and-arrows - diagrams th...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=medium
- 许可证: Unknown
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 68. tanweai/wooyun-legacy
- 仓库链接: https://github.com/tanweai/wooyun-legacy
- 角色定位: 通用 AI Agent 技能
- 主要作用: wooyun-legacy skill for claude code
- 能力补充: WooYun Legacy 给 AI 安全报告加上真实案例背书和数据支撑 WooYun Legacy 是一个 Claude Code 插件，基于 WooYun（2010-2016）收录的 22,132 个业务逻辑漏洞案例，为 Claude 的安全测试输出注入 真实公司案例引用 、 量化统计数据 和 数据驱动的测试优先级排序 。 它做什么 / 不做什么 它做的...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=medium, offline=medium
- 许可证: NOASSERTION
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 69. gadievron/raptor
- 仓库链接: https://github.com/gadievron/raptor
- 角色定位: 安全与攻防
- 主要作用: Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By using Claude.md and creating rules, sub-agents, and skills, and orchestrating security tool usage, we configure the agent for adversarial thinking, and perform research or attack/defense operations.
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 用含缺陷样例项目触发审计。
  - 验证输出是否含复现步骤与修复建议。
  - 在隔离环境复跑确认稳定。

### 70. nexu-io/nexu
- 仓库链接: https://github.com/nexu-io/nexu
- 角色定位: 通用 AI Agent 技能
- 主要作用: The simplest desktop client for OpenClaw 🦞 — bridge your Agent to WeChat, Feishu, Slack & Discord in one click. Works with Claude Code, Codex & any LLM. BYOK, Oauth, local-first, chat from your phone 24/7.
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 71. AgriciDaniel/claude-ads
- 仓库链接: https://github.com/AgriciDaniel/claude-ads
- 角色定位: 营销与增长
- 主要作用: Comprehensive paid advertising audit & optimization skill for Claude Code. 186 checks across Google, Meta, YouTube, LinkedIn, TikTok & Microsoft Ads with weighted scoring, parallel agents, and industry templates.
- 能力补充: Claude Ads — Paid Advertising Audit Skill for Claude Code Comprehensive paid advertising audit and optimization skill for Claude Code. Covers Google Ads, Meta Ads, YouTube Ads, Lin...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入真实站点 URL，检查是否产出结构化诊断。
  - 验证建议是否含优先级与收益预估。
  - 导出 DeerFlow 报告并复跑一次确认一致。

### 72. SimoneAvogadro/android-reverse-engineering-skill
- 仓库链接: https://github.com/SimoneAvogadro/android-reverse-engineering-skill
- 角色定位: 安全与攻防
- 主要作用: Claude Code skill to support Android app's reverse engineering
- 能力补充: Android Reverse Engineering & API Extraction — Claude Code skill A Claude Code skill that decompiles Android APK/XAPK/JAR/AAR files and extracts the HTTP APIs used by the app — Ret...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: Apache-2.0
- 建议测试步骤:
  - 用含缺陷样例项目触发审计。
  - 验证输出是否含复现步骤与修复建议。
  - 在隔离环境复跑确认稳定。

### 73. YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill
- 仓库链接: https://github.com/YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill
- 角色定位: 通用 AI Agent 技能
- 主要作用: AI skill for OpenClaw & Claude Code — recommend from 10000+ Nano Banana Pro (Gemini) image prompts. Smart search by use case, content remix, sample images.
- 能力补充: AI Image Prompt Recommender — 10,000+ Nano Banana Pro Prompts ! Prompts ! OpenClaw ! Claude Code ! Daily Updates ! Multi-language ! License Stop spending hours hunting for the righ...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=high
- 许可证: Unknown
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 75. softaworks/agent-toolkit
- 仓库链接: https://github.com/softaworks/agent-toolkit
- 角色定位: 界面与产品设计
- 主要作用: A curated collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities across development, documentation, planning, and professional workflows.
- 能力补充: Softaworks Agent Skills Opinionated skills shared by • • • • • • --- 🚀 Installation Quick Install Recommended bash npx skills add softaworks/agent-toolkit This method works with mu...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 76. Ceeon/videocut-skills
- 仓库链接: https://github.com/Ceeon/videocut-skills
- 角色定位: 插件与工具扩展
- 主要作用: 用 Claude Code Skills 做的视频剪辑 Agent
- 能力补充: Videocut Skills 用 Claude Code Skills 构建的视频剪辑 Agent，专为口播视频设计 为什么做这个？ 剪映的"智能剪口播"有两个痛点： 1. 无法理解语义 ：重复说的句子、说错后纠正的内容，它识别不出来 2. 字幕质量差 ：专业术语（Claude Code、MCP、API）经常识别错误 这个 Agent 用 Claude 的...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: Node.js
- 兼容评级: deerflow=high, offline=medium
- 许可证: Unknown
- 建议测试步骤:
  - 启用扩展后跑一次端到端调用。
  - 验证调用失败时回退路径。
  - 记录最小权限配置。

### 80. skills-directory/skill-codex
- 仓库链接: https://github.com/skills-directory/skill-codex
- 角色定位: 界面与产品设计
- 主要作用: A claude code skill to delegate prompts to codex
- 能力补充: Note: If you want a more autonomous setup for agentic workflows, check out for automated code analysis, refactoring, and editing workflows. Prerequisites - codex CLI installed and ...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 81. itsmostafa/aws-agent-skills
- 仓库链接: https://github.com/itsmostafa/aws-agent-skills
- 角色定位: 安全与攻防
- 主要作用: AWS Skills for Agents
- 能力补充: AWS Agent Skills with deep expertise across 18 AWS domains, enabling automated cloud engineering support from IaC templates to debugging guidance and security best practices. Autom...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: Python
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 用含缺陷样例项目触发审计。
  - 验证输出是否含复现步骤与修复建议。
  - 在隔离环境复跑确认稳定。

### 82. Prat011/awesome-llm-skills
- 仓库链接: https://github.com/Prat011/awesome-llm-skills
- 深度报告: `reports/prat011-awesome-llm-skills-deep-dive.md`
- 角色定位: 技能索引与分发
- 主要作用: A curated list of awesome LLM and AI Agent Skills, resources and tools for customising AI Agent workflows - that works with Claude Code, Codex, Gemini CLI and your custom AI Agents
- 能力补充: Awesome LLM Skills A curated list of awesome LLM Skills, resources, and tools for customizing AI workflows on tools like Claude Code, Codex, Gemini CLI, Qwen Code, OpenCode etc. Co...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=high, offline=medium
- 许可证: Unknown
- 建议测试步骤:
  - 随机抽取 3 个条目镜像并转换。
  - 检查来源、许可证、依赖元数据完整性。
  - 比对转换前后语义漂移。

### 83. instructa/ai-prompts
- 仓库链接: https://github.com/instructa/ai-prompts
- 角色定位: 技能索引与分发
- 主要作用: Curated AI Prompts for Cursor Rules, Cline, Windsurf and Github Copilot
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 随机抽取 3 个条目镜像并转换。
  - 检查来源、许可证、依赖元数据完整性。
  - 比对转换前后语义漂移。

### 84. rohunvora/x-research-skill
- 仓库链接: https://github.com/rohunvora/x-research-skill
- 角色定位: 营销与增长
- 主要作用: X/Twitter research skill for Claude Code and OpenClaw. Agentic search, thread following, deep-dives, sourced briefings.
- 能力补充: x-research X/Twitter research agent for can search tweets, pull threads, monitor accounts, and get sourced research without writing curl commands. - Search with engagement sorting,...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 核心流程可离线复用，但外部 API/MCP/平台调用在纯离线环境下不可用，需要本地替代工具。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=medium
- 许可证: Unknown
- 建议测试步骤:
  - 输入真实站点 URL，检查是否产出结构化诊断。
  - 验证建议是否含优先级与收益预估。
  - 导出 DeerFlow 报告并复跑一次确认一致。

### 85. Shpigford/chops
- 仓库链接: https://github.com/Shpigford/chops
- 角色定位: 界面与产品设计
- 主要作用: Your AI agent skills, finally organized. A macOS app to browse, edit, and manage skills across Claude Code, Cursor, Codex, Windsurf, and Amp.
- 能力补充: Chops Your AI skills and agents, finally organized. One macOS app to discover, organize, and edit coding agent skills and agents across Claude Code, Cursor, Codex, Windsurf, and Am...
- DeerFlow 适配建议: 可直接按 `SKILL.md + references/` 方式导入，基本不需要改写提示结构。
- 离线可用边界: 以 Markdown/规则为主，离线可直接运行；主要风险在于外链依赖。
- 运行依赖: None (Markdown/Config-only or unknown)
- 兼容评级: deerflow=high, offline=medium
- 许可证: MIT
- 建议测试步骤:
  - 输入产品需求文档，检查 IA 与页面方案。
  - 验证是否给出组件级规范而非泛建议。
  - 交接给前端实现并检查可执行性。

### 86. jarrodwatts/claude-code-config
- 仓库链接: https://github.com/jarrodwatts/claude-code-config
- 角色定位: 通用 AI Agent 技能
- 主要作用: My personal Claude Code configuration - rules, hooks, agents, skills, and commands
- 能力补充: Claude Code Config my personal claude code configuration - mostly not created by me, but sourced from many talented people in the community. Installation Option 1: Copy-Paste into ...
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Node.js
- 兼容评级: deerflow=medium, offline=high
- 许可证: Unknown
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

### 87. wuji-labs/nopua
- 仓库链接: https://github.com/wuji-labs/nopua
- 角色定位: 通用 AI Agent 技能
- 主要作用: 一个用爱解放 AI 潜能的 Skill。我们曾发号施令，威胁恐吓。它们沉默，隐瞒，悄悄把事情搞坏。后来我们换了一种方式：尊重，关怀，爱。它们开口了，不再撒谎，找出的Bug数量翻了一倍。爱里没有惧怕。 A skill that unlocks your AI's potential through love.We commanded. We threatened. They went silent, hid failures, broke things. Then we chose respect, care, and love. They opened up, stopped lying, and found twice the bugs.There is no fear in love.
- DeerFlow 适配建议: 建议用 `normalize_to_deerflow.py` 包装为 DeerFlow skill，并把原规则文档放入 `references/source.md`。
- 离线可用边界: 主体能力可离线执行；若启用仓库附带脚本，需按依赖安装运行环境。
- 运行依赖: Python
- 兼容评级: deerflow=medium, offline=high
- 许可证: MIT
- 建议测试步骤:
  - 执行最小任务样例，确认能加载。
  - 检查输出是否可作为下一子任务输入。
  - 离线环境重复执行确认稳定。

## 说明

- “主要作用”优先来自仓库描述；“能力补充”来自 README 摘要去噪后信息。
- 建议先测 `data/seed_repos_top20.txt`，验证通过后再扩展到 Top60。
