# 项目基底评估与采用顺序

2026-10-23。依据上一轮调研，并重新读取重点仓库的 README、依赖清单、数据库定义、API 文档和 GitHub 元数据。未安装运行、未压测、未测论文理解正确率；以下分数是**针对本项目的选型判断**，不是产品客观排行榜或实测成绩。

## 结论先行

**主建议：以 Open Notebook 为完整应用基底，先保留原栈做小样本改造；另接专门组件，不合并多个完整应用。** 复用研究工作区、来源/笔记、模型配置、问答搜索、内容转换和已有后台作业。新增独立科研领域模块，负责 Zotero 身份映射、论文版本、证据、技术关系、审阅和报告快照；用清楚的内部 API 连接既有功能，不让技术图直接依赖聊天记录或向量库。

这意味着修订上一轮技术选择为 **Next.js/React + FastAPI + SurrealDB**，SQLite 可保留作上游现有 checkpoint 的实现。SQLite 是上一轮设计建议，不是用户硬性要求，不能因其已被写下便推导出必须自建。Open Notebook 的 API 文档及依赖表已经证明通用工作台能力与 Python 扩展点存在；因此先复用它，比现在自行开发全部工作台更有依据。不要在 fork 的同时替换数据库、前端和任务系统；正式领域对象通过独立 repository 接口和新增数据表/集合维护，具体事务/索引能力在试点验证。

| 比较 | Open Notebook 原栈扩展 | 自建 React + FastAPI + SQLite |
|---|---|---|
| 可以省掉的初期工作 | 已有工作区、资料上传、模型设置、搜索、笔记、转换、作业状态和部署界面 | 无完整应用可直接复用；可复用解析/编排等组件 |
| 两者都要新做 | Zotero同步、技术谱系、证据版本、确认、真实活动与周报 | 相同；自建不会自动让这些更可靠 |
| 长期代价 | SurrealDB运行、上游升级合并、科研模块与既有对象边界 | 更多界面与通用能力由本项目独自维护，初期交付较慢 |
| 当前判断 | **作为默认起点**，增加模块优于立即重写通用层 | 有条件备选，适合证明上游耦合或运行负担无法接受之后 |

这个维护总量判断尚未经实装计时。用约 20 篇论文做 **3–5 个工作日的技术试点时间盒**：完成 Zotero 条目到 source 映射、一个带版本定位的证据对象、一个可确认技术关系、失败后恢复、完整导出/备份恢复。必须保留现有来源、笔记、搜索、模型配置等主流程不重写；若无法隔离科研模块、为一个领域功能必须修改多个核心读写路径、证据定位/不可变快照无法可靠实现，或本机运行数据库与容器的负担用户不能接受，则停止扩大 fork，转为自有核心+组件方案。时间盒不保证这些测试都能通过；其目的是在重度改造前暴露成本。

## 完整应用排序

评分 1–5，越高越有利：实用性 P（25%）= 现在能直接完成多少相关任务；可迁移性 T（20%）= 接口、数据取回及代码复用难度；完整性 C（15%）= 部署、界面、文档和完整流程；适配性 F（30%）= 与科研需求、Python/React扩展及本地单用户的匹配；工程证据 E（10%）= 可见维护、发布、测试依据。总分 `0.25P + 0.20T + 0.15C + 0.30F + 0.10E`。不要求候选强行符合上一轮SQLite选择；相差 0.1 左右没有统计意义。许可证单独列出，不把宽松许可证等同质量。

| 顺序 / 项目 | P | T | C | F | E | 加权分 | 用途与主要代价 |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 [Open Notebook](https://github.com/lfnovo/open-notebook) | 4.5 | 4 | 4 | 4.5 | 4 | **4.28** | 长期 fork 候选第一。研究工作区、笔记、转换和引用问答贴近需求；技术谱系、Zotero 同步、确认/版本体系和 PPT 仍需新增 |
| 2 [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | 5 | 3.5 | 4.5 | 3 | 4.5 | **3.98** | 通用功能原型第一。模型、Agent、MCP、定时任务现成；长期扩展要深入 Node 后端并重建科研领域模型 |
| 3 [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | 4 | 3.5 | 4 | 3 | 4 | **3.60** | 研究报告与外部搜索流程较完整；以调研任务为中心，持久文献管理和技术谱系仍是新产品 |
| 4 [Kotaemon](https://github.com/Cinnamon/kotaemon) | 3.5 | 3.5 | 3.5 | 3.5 | 3 | **3.45** | PDF 高亮引用、混合检索和可调管线适合精读原型；Gradio 界面若改为现定 React，界面复用明显减少 |
| 5 [Khoj](https://github.com/khoj-ai/khoj) | 3.5 | 2.5 | 4 | 3 | 2.5 | **3.13** | 科研管家/周期简报参考；通用助手范围较大，Python 服务与既有数据库体系需适配，维护方向需继续观察 |
| 6 [Paper2Slides](https://github.com/HKUDS/Paper2Slides) | 2.5 | 3.5 | 3 | 2.5 | 2.5 | **2.78** | 只覆盖汇报子任务，阶段检查点值得复用；当前生成图片与 PDF，不能直接满足可编辑 PPTX |
| 7 [Paperlib](https://github.com/Future-Scholars/paperlib) | 3 | 2.5 | 4 | 2 | 2.5 | **2.70** | 成熟文献管理方向参考；本项目保留 Zotero，fork 它将重复建设文献库，并另加 AI、技术图和调度 |

AnythingLLM 的“原型第一”不等于“长期 fork 第一”。上述排名的适配性权重较高；若目标改成最快获得通用聊天和自动化、并接受 Node 主后端，AnythingLLM 可以排第一。Paper2Slides/Paperlib 排后是任务匹配问题，不表示它们在自己领域较差。

## 技术、接口和数据退出成本

| 项目 | 实际技术 / 许可证 | 可复用边界与数据迁出 | 工程证据及待验证项 |
|---|---|---|---|
| Open Notebook | FastAPI + Next.js/React + SurrealDB；MIT。依赖中已有 LangGraph 和 SQLite checkpoint，**checkpoint 不是领域数据库** | 官方 `/api` 覆盖 notebooks、sources、notes、search、transformations、jobs；可下载源文件，API 可用于取回对象。同机迁移有数据库与文件目录备份。异构迁移到 SQLite 仍需转换 ID、关系、查询和作业数据；未核验完整语义一键导出 | 10-20 推送；上一轮核验发布与前后端 CI。本轮确认 API 和部署文档。默认数据、任务机制均与 SurrealDB 有联系，不是换一行连接串即可迁移 |
| AnythingLLM | React/Vite + Node/Express + Prisma/SQLite，独立 collector；MIT | 完整开发 API 可管理、嵌入和问答工作区；可调用外部 FastAPI，但会形成两套后端。SQLite 不意味着能直接复用其业务表。聊天/资料对象与版本化证据、审阅图需要另建映射；未验证完整迁出保真 | 10-23 推送；已有发布及测试工作流。适合短期接口原型；别把同时运行两个应用当成长期“合并完成” |
| GPT Researcher | Python 服务/SDK + Web 前端；Apache-2.0 | 以研究请求和报告产物接入，保留研究流程或 SDK；本项目接管证据、报告快照和任务状态。避免把它自己的循环执行器再套成第二个总调度器 | 10-10 推送；既有 tests/evals 目录可作线索，不能推定本领域准确率 |
| Kotaemon | Python + Gradio；Apache-2.0 | `kotaemon` 管线与 `ktem` 应用分层；官方说明复制 `ktem_app_data` 可迁移安装。复制目录是应用备份，不等于通用科研数据导出；研究 API 契约和 React 界面要自建 | 07-14 推送；README明确部分图检索依赖冲突及旧版约束。Windows 原生安装与解析组合需实测 |
| Khoj | Python，依赖 FastAPI/Django；既有 PostgreSQL 使用路径；AGPL-3.0 | 可参考 API、搜索和自动化；不能直接当成 SQLite 应用。资料可重建不代表会话、计划和衍生状态能无损迁出；迁移路径未实测 | 08-02 推送；README推荐同团队 Pipali，这只是投入方向信号，不等于已停止维护。保留对应许可证并单独审查发布方案 |
| Paper2Slides | React/Vite + FastAPI；MIT | CLI/API 与阶段检查点清晰；取回大纲/中间结果，把最终阶段换成原生 PPTX 渲染；不采用整套应用作为科研数据中心 | 05-20 推送；README最终产物 `slides.pdf`，图片生成不保证文字公式可编辑 |
| Paperlib | Electron + Vue + Realm；GPL-3.0 | 可参考元数据抓取、RSS、扩展接口；文献导出不等于技术图/智能体状态迁出。与 Zotero 职能重复，整体迁移价值较低 | 04-01 推送；包清单存在 e2e 测试命令，不能因上一轮未见专用 CI 就说“没有测试”；Windows 安装签名仍需注意 |

上述七仓库本次均未归档；日期来自 GitHub `pushed_at`（UTC），可能只是文档或分支推送，不证明发布质量。许可证这里只记录仓库标识，不作组合分发的法律结论。

重点原始依据：[Open Notebook API](https://github.com/lfnovo/open-notebook/blob/main/docs/7-DEVELOPMENT/api-reference.md)、[其依赖](https://github.com/lfnovo/open-notebook/blob/main/pyproject.toml)、[备份说明](https://github.com/lfnovo/open-notebook/blob/main/docs/1-INSTALLATION/docker-compose.md)；[AnythingLLM API](https://docs.anythingllm.com/features/api)、[数据库定义](https://github.com/Mintplex-Labs/anything-llm/blob/master/server/prisma/schema.prisma)；[Paperlib 包清单](https://github.com/Future-Scholars/paperlib/blob/chore/official-sync/package.json)。其余技术/输出依据为各仓库 README 与依赖清单，历史发布和 CI 的详细来源见 [GitHub 原始调研](2026-10-22/github-projects.md)、[博客原始调研](2026-10-22/blog-practices.md)。

## 专门组件：按接入先后排序，不与完整应用比较总分

| 优先级 | 项目 / 建议 | 接入本系统的边界 | 采用前关键验证 |
|---|---|---|---|
| 1 | Zotero 官方 API；[kujenga/zotero-mcp](https://github.com/kujenga/zotero-mcp) 作可选工具接口（MIT） | 官方 API 完成条目同步；MCP 供 Agent 搜索/读元数据与全文。MCP 本身不负责增量游标、批注同步、冲突解决 | 用户库能导入、按稳定 key 去重，附件版本可识别；不改 Zotero 原库 |
| 2 | [Docling](https://github.com/docling-project/docling)（代码 MIT，模型另核） | 独立解析适配器，输出结构化文档/来源定位；保存 lossless JSON，Markdown 用于阅读 | 双栏、扫描、表格、公式和页码定位；保留失败与低质量页 |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph)（MIT，上游已有） | 在已有任务机制内增加科研工作流，不额外部署第二个总调度器；预算、幂等和领域提交由科研模块明确约束 | 中断恢复不重复提交、取消生效、旧任务不能覆盖新结果 |
| 4 | [PptxGenJS](https://github.com/gitbrent/PptxGenJS)（MIT） | Node 子进程消费统一 SlidePlan，输出可编辑 PPTX | 在目标 PowerPoint/WPS 打开、渲染、抽样编辑，检查公式/字体/溢出 |
| 5 | [PaperQA2](https://github.com/Future-House/paper-qa)（Apache-2.0） | 可替换 EvidenceRetriever；比较基础混合检索后决定，不拥有正式知识库 | 用同一批论文比较支持率、漏检、成本；公开版和内部实验版有差异，锁版本 |
| 6 | GPT Researcher 研究流程、Kotaemon 阅读交互 | 仅在其解决具体缺口时选取模块或接口，不同时部署两套完整问答系统 | 新增价值是否超过依赖、任务和数据重复成本 |
| 暂缓 | Microsoft GraphRAG；ArxRec；Paper2Slides | 前者只作图检索对照；ArxRec 仅借鉴反馈思路；Paper2Slides 借鉴计划与检查点 | 通用图不等于技术继承；ArxRec 未核验明确许可证；图片/PDF 不等于可编辑幻灯片 |

组合方式为：`Zotero → Open Notebook 中独立的 Paper/Evidence/Claim/Relation 领域模块 → 已有任务机制与受控工作流 → 日报与 SlidePlan → PPTX`。先试现有解析器，Docling作为可替换引擎；PptxGenJS通过Node子进程输出；PaperQA2作为对照通过后才接入的证据检索适配器。解析、检索和模型输出先形成候选结果，确认接口才修改正式知识。保留一个正式领域写入口，并补充带 schema_version 的 JSON/Markdown 导出，不能把数据库备份冒充跨产品迁移。完整应用只选 Open Notebook，AnythingLLM/GPT Researcher/Kotaemon不再并排常驻；不把多个仓库平铺拷贝合并。

## 博客阅读顺序

按本项目落地价值排序：① [FutureHouse 科学问答工程实践](https://www.futurehouse.org/research/engineering-blog-journey-to-superhuman-performance-on-scientific-tasks)（证据与评测，4.6/5）→ ② [Aaron Taylor 的 Zotero MCP 实践](https://ataylor.io/blog/zotero-mcp/)（窄接口接入，4.4）→ ③ [Assaf Elovic 多 Agent 协作](https://www.langchain.com/blog/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration)（流程参考，4.0）→ ④ [Haoxiang 的 arXiv 推荐实践](https://blog.haoxiang.org/2024/02/personalized-arxiv-recommendation-service/)（轻量反馈闭环，3.6）→ ⑤ [Paper2Slides 第三方分析](https://hysenlabs.com/projects/hkuds-paper2slides)（仅发现线索，3.0）。这是文章参考价值和阅读顺序，不是可部署代码排名；五维等权定义和风险详见 [博客实践评估](blog-practice-ranking.md)。

本轮没有 fork、安装或把任何上游代码合入主仓库。下一次实际选型以 20 篇论文的集成小试为依据；公开文档不能代替用户研究领域中的准确性、成本和恢复测试。
