# Open Notebook 基底上的功能复用清单

更新：2026-10-23。状态：规划；尚未引入、安装或集成这些项目。依据为本轮已核验的 [项目评估](../research/base-project-ranking.md)及 [博客实践](../research/blog-practice-ranking.md)，不代表所有组件都必须引入。

## 复用边界

只选择 Open Notebook 作为完整应用基底；其他项目优先借鉴交互和流程，明确缺口时才接入库或窄接口。“易于借鉴”不等于源码可直接复制；模型、数据格式、许可证和依赖仍需逐项验证。越依赖原项目数据库与任务系统的功能，越适合借鉴设计后在本基底实现。

| 项目 | 值得迁移的内容 | 最合理的形式 | 边界与接入顺序 |
|---|---|---|---|
| [Open Notebook](https://github.com/lfnovo/open-notebook) | 工作区、资料/笔记、模型配置、搜索问答、内容转换、任务界面与 API | **保留原栈改造** | 第一阶段基底；Next.js/FastAPI/SurrealDB 保留，科研身份、证据和技术图不是现成能力 |
| [Zotero / Zotero MCP](https://github.com/kujenga/zotero-mcp) | 读取现有文献元数据、全文及搜索的窄工具接口；继续使用 Zotero 阅读 | **官方 API 适配；MCP 可选** | 首先只读接入；MCP 不替代同步游标、稳定身份、附件版本和去重逻辑 |
| [Docling](https://github.com/docling-project/docling) | 结构化文档解析、版面与来源定位信息 | **解析库/适配器** | 先试基底解析器，有明确缺口再引入；保留结构化产物，公式/扫描件质量需实测 |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 分阶段工作流、运行状态和中断恢复结构 | **扩展上游已有依赖** | 沿用一个作业入口，不另装第二套总调度器；恢复不自动保证领域提交幂等 |
| [PptxGenJS](https://github.com/gitbrent/PptxGenJS) | 可编辑文本、图表、图片的 PPTX 生成 | **独立渲染适配器** | 后期消费统一 SlidePlan；公式、字体、版面和编辑能力须在目标软件验收 |
| [PaperQA2](https://github.com/Future-House/paper-qa) | 证据检索、重排、带来源回答和评测方法 | **先借鉴方法，后评估可替换检索组件** | 与基础检索在同一批论文上比较后决定；不接管正式知识库，不承诺推导正确 |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | 问题拆解 → 搜索 → 筛选 → 汇总 → 审阅的研究流程 | **流程为主，必要时窄 API/SDK** | 用于专题调研与日报发现；不直接搬入完整多 Agent 运行体系 |
| [Kotaemon](https://github.com/Cinnamon/kotaemon) | 回答与原文高亮联动、证据侧栏、混合检索管线思路 | **交互与管线设计** | 在 Open Notebook 界面重现适用部分；Gradio 界面不直接拼入 Next.js |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | 模型/工具配置、连接器管理、工作区权限和任务反馈的组织方式 | **产品结构与交互借鉴** | 只采用确有缺口的体验；不搬 Node 后端、数据库或重复的模型设置系统 |
| [Khoj](https://github.com/khoj-ai/khoj) | 个人助手中的搜索、周期任务和简报入口组织 | **产品流程借鉴** | 帮助设计科研管家；本项目仍需实现科研进度语义，移植代码前另核依赖与许可 |
| [ArxRec](https://github.com/pppoe/ArxRec) | 兴趣方向 → 每日短名单 → 已读/忽略反馈 → 调整推荐 | **思想与独立实现** | 原仓库未核验明确许可证，不复制源码；来源与排序按用户学科调整 |
| [Paper2Slides](https://github.com/HKUDS/Paper2Slides) | 解析 → 摘要 → 大纲 → 生成的阶段划分、检查点 | **流程与中间产物设计** | 大纲先审阅，再交自己的 PPTX 渲染器；图片/PDF 输出不等于可编辑 PPT |
| [Paperlib](https://github.com/Future-Scholars/paperlib) | 元数据补全、RSS、集合/标签与扩展入口的组织思路 | **局部体验借鉴** | Zotero 已承担文献库，不迁入 Paperlib 整套存储或阅读器 |
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | 图辅助组织和检索大批材料的思路 | **后期检索对照，暂不接入** | 通用实体图不自动表示方法继承；不能直接拿来充当技术谱系 |

## 组合后能形成什么能力

以下是目标能力，不是本轮已经实现的功能。

1. **读与找**：保留 Zotero 阅读，工作台按研究问题组织文献，搜索、问答并回看证据。
2. **记与连**：生成简短记忆卡，把论文放入可审阅的技术关系网络，按主题显示主干与分支。
3. **深度理解**：用声明式 Skill 分别执行精读、数学推导和方法思路重建，记录材料范围与未解决问题。
4. **持续跟进**：增量发现论文，结合已读/忽略反馈形成短名单；基于真实活动生成日报与待办。
5. **汇报输出**：把指定时间段的活动和确认知识固定为快照，生成可编辑、可查来源的周报 PPT。

其中工作区、模型配置、通用检索和解析/渲染基础较易复用；**论文身份与版本、证据支持关系、技术谱系、确认与修订保护、真实科研进度和不可变报告快照仍须自建并验证**。数学正确性与技术继承真实性不能靠组合项目自动获得。

采用顺序遵循 [基底试点 ADR](../decisions/0002-open-notebook-base.md)：先 Zotero → 证据 → 简介/关系 → 确认/快照，再增加精读、每日发现与 PPT；每次只有明确缺口才引入新的运行依赖。当前架构的唯一权威入口仍是 [当前架构](current-architecture.md)。
