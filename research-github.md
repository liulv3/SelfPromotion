# GitHub 项目检索报告

核验日期：2026-10-22。检索使用 agent-reach 的 GitHub 流程，实际通过已连接的 GitHub 工具读取公开仓库 README、LICENSE、release、workflow 和部分运行记录。没有安装、运行或做论文质量实测。下表“功能”来自官方 README／文档；“适用性、优缺点、评级”是本次判断；发布日期、许可证、CI 文件和运行结果属于已核验事实。Stars 不作为可靠性证据。

## 建议

**快速验证：AnythingLLM 作为可替换的原型外壳，Zotero 继续作为文献和批注入口。** 它已有文档问答、Agent、定时任务，最容易验证“读论文—研究日报—周报素材”闭环。技术谱系及证据数据必须放在自有领域服务中，通过接口接入，避免原型数据库变成长期约束。

**长期实现：自有科研领域层 + 可替换组件。** 核心资产是 Paper、Claim、EvidenceSpan、Method、TypedRelation、ReviewDecision、SkillRun；Zotero 负责原件与阅读，LangGraph 负责可恢复工作流，解析/检索/演示文稿使用专门组件。通用 GraphRAG 图不是技术继承树：引用、相似、改进、依赖、反驳要分类型存储；用户选择主干，界面投影成树，底层保留多父节点和交叉边。

## 8 个候选

| 项目 / 许可证 | 官方描述的功能；可以复用在哪里 | 优点与局限 | 可靠性证据与判断 |
|---|---|---|---|
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) / [MIT](https://github.com/Mintplex-Labs/anything-llm/blob/master/LICENSE) | 文档问答、来源引用、自定义 Agent、无代码流程、Scheduled Tasks、多模型和向量库；可作功能原型外壳与科研日报入口 | 优：现成工作区和自动化覆盖面广。缺：通用知识助手，未核验到论文技术继承树、严格数学推导验证或 Zotero 原生领域模型；存在可关闭遥测，需按本地部署目标配置 | [v1.18.0，2026-10-13](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.18.0)；[后端测试工作流](https://github.com/Mintplex-Labs/anything-llm/blob/master/.github/workflows/run-tests.yaml)读取到 yarn test，PR触发。近期抽样PR运行需维护者批准，不能当作通过。**原型优先；工程可信度中上，科研答案正确率未知** |
| [Open Notebook](https://github.com/lfnovo/open-notebook) / [MIT](https://github.com/lfnovo/open-notebook/blob/main/LICENSE) | 研究 notebook、多模态来源、全文/向量搜索、来源引用、自定义转换、REST API；可复用论文工作区和摘要/问答 | 优：研究内容组织贴近用户、API边界清晰、可自托管。缺：SurrealDB等既有架构需适配；[VISION](https://github.com/lfnovo/open-notebook/blob/main/VISION.md)明确当前单用户，PPT产物和MCP agents仍属无日期愿景，不能写成已经提供 | [v1.15.0，2026-10-04](https://github.com/lfnovo/open-notebook/releases/tag/v1.15.0)；[CI](https://github.com/lfnovo/open-notebook/blob/main/.github/workflows/test.yml)含后端pytest/coverage、前端测试、lint、typecheck、构建。发行说明声称做过全新安装、升级、API/UI端到端验证，这属于维护者报告。**研究界面首选备选底座；中上** |
| [Kotaemon](https://github.com/Cinnamon/kotaemon) / [Apache-2.0](https://github.com/Cinnamon/kotaemon/blob/main/LICENSE.txt) | 混合检索+重排、PDF高亮引用、低相关提醒、问题分解、ReAct/ReWOO、多种GraphRAG实验；可复用可追溯精读与RAG试验台 | 优：证据定位UI比普通聊天更贴近论文阅读；检索管线可扩展。缺：Gradio界面可能需要重做；README提示nano-graphrag依赖冲突，MS GraphRAG示例限制旧版本；通用图不等于技术谱系 | [v0.12.0，2026-05-31](https://github.com/Cinnamon/kotaemon/releases/tag/v0.12.0)；[单测CI](https://github.com/Cinnamon/kotaemon/blob/main/.github/workflows/unit-test.yaml)运行Ubuntu/Python3.10、3.11，Windows矩阵被注释。**证据阅读组件中等，Windows整包稳定性需试装** |
| [Paperlib](https://github.com/Future-Scholars/paperlib) / [GPL-3.0](https://github.com/Future-Scholars/paperlib/blob/chore/official-sync/LICENSE) | 论文管理、元数据抓取、RSS、引用复制、扩展生态（AI摘要/聊天等）；可借鉴无DOI会议论文元数据整理、RSS入口与扩展设计 | 优：科研场景集中，尤其计算机会议论文。缺：替代已有Zotero会增加迁移负担；不是技术谱系或智能体调度底座；README说明Windows安装包无签名；GPL需纳入分发方案评估 | [3.1.12，2025-09-28](https://github.com/Future-Scholars/paperlib/releases/tag/release-electron-3.1.12)涉及从云数据库迁到本地及Windows修复；[发布CI](https://github.com/Future-Scholars/paperlib/blob/chore/official-sync/.github/workflows/release.yml)有多平台构建，但该目录只见beta/release，无专门单测流程证据。**参考/可选替代品，中等偏保守** |
| [Khoj](https://github.com/khoj-ai/khoj) / [AGPL-3.0](https://github.com/khoj-ai/khoj/blob/master/LICENSE) | 私人知识搜索、文档/互联网问答、自定义agents、自动研究和简报；可借鉴个人科研管家与周期任务 | 优：助手及个人知识场景契合；含检索评测工作流。缺：通用个人助手、非学术数据模型；AGPL需提前评估；README已推荐维护团队新产品Pipali，需确认长期投入 | [2.0.0-beta.28，2026-03-26](https://github.com/khoj-ai/khoj/releases/tag/2.0.0-beta.28)；[CI](https://github.com/khoj-ai/khoj/blob/master/.github/workflows/test.yml)覆盖Python3.10—3.12/Postgres；抽查默认分支最近push测试在[2026-08-02失败](https://github.com/khoj-ai/khoj/actions/runs/30727919093)，此前同日成功。**有工程基础，但当前采用需先修复/复验，中等偏保守** |
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) / [MIT](https://github.com/microsoft/graphrag/blob/main/LICENSE) | 文本实体、关系、社区摘要和基于图的问答；可作为跨论文发现关系的候选生成器或比较基线 | 优：有研究方法、文档和测试。缺：README明确进入维护模式，不接新功能/新PR；不是正式受支持的Microsoft产品，索引成本高；生成关系不能直接视为技术继承事实 | [v3.3.0，2026-10-08](https://github.com/microsoft/graphrag/releases/tag/v3.3.0)；[测试目录](https://github.com/microsoft/graphrag/tree/main/.github/workflows)含单元、集成、smoke测试。**适合研究基线，不建议成为技术谱系核心依赖** |
| [LangGraph](https://github.com/langchain-ai/langgraph) / [MIT](https://github.com/langchain-ai/langgraph/blob/main/LICENSE) | 有状态Agent编排、持久化执行、人审中断、记忆；可实现精读/推导/反推作者思想等版本化Skill工作流 | 优：恢复、中断、重试状态可以明确设计；可独立使用，不要求完整LangChain。缺：是框架，不提供论文质量；Skills规范、权限边界、成本限制、验证器仍需自己做。注意开源框架与商业部署/观测产品边界 | [多包发布记录](https://github.com/langchain-ai/langgraph/releases)及[CI](https://github.com/langchain-ai/langgraph/tree/main/.github/workflows)持续存在，仓库未归档；latest release返回的是CLI 0.4.37，不能误写为LangGraph核心版本。**长期编排组件优先，中上** |
| [PptxGenJS](https://github.com/gitbrent/PptxGenJS) / [MIT](https://github.com/gitbrent/PptxGenJS/blob/master/LICENSE) | 从JS生成原生文本、表格、图形、图表、图片和母版的pptx；可作为PPT Skill最终可编辑文件输出层 | 优：结构化对象方便统一模板、批量周报；无需本地PowerPoint生成。缺：不负责论文理解、故事线与审美；公式/字体/溢出、软件间渲染差异需要模板与实测 | [v4.0.1，2025-06-26](https://github.com/gitbrent/PptxGenJS/releases/tag/v4.0.1)修复过表格分页超链接导致文件修复提示；[TESTING](https://github.com/gitbrent/PptxGenJS/blob/master/TESTING.md)主要是人工跨环境测试指南，不能等同本次生成文件已通过测试。**成熟输出组件，中等偏高；固定版本+渲染验收** |

## 可核查的仓库状态

下面是 GitHub API 的 `pushed_at`，表示仓库最近推送，**不等于默认分支最后功能提交，也不等于质量保证**。八个仓库在本次API读取中均未归档。

| 仓库 | pushed_at（UTC） |
|---|---|
| [Open Notebook API](https://api.github.com/repos/lfnovo/open-notebook) | 2026-10-20 10:52:09 |
| [Kotaemon API](https://api.github.com/repos/Cinnamon/kotaemon) | 2026-07-14 16:53:59 |
| [Paperlib API](https://api.github.com/repos/Future-Scholars/paperlib) | 2026-04-01 23:01:59 |
| [Khoj API](https://api.github.com/repos/khoj-ai/khoj) | 2026-08-02 01:55:40 |
| [AnythingLLM API](https://api.github.com/repos/Mintplex-Labs/anything-llm) | 2026-10-22 06:26:35 |
| [GraphRAG API](https://api.github.com/repos/microsoft/graphrag) | 2026-10-20 15:24:08 |
| [LangGraph API](https://api.github.com/repos/langchain-ai/langgraph) | 2026-10-22 13:34:18 |
| [PptxGenJS API](https://api.github.com/repos/gitbrent/PptxGenJS) | 2025-11-28 20:17:14 |

## 复用前最小验收

1. 用同一批约20篇真实论文测试：双栏、扫描、复杂公式、跨页表格、附录、撤稿/版本重复；记录解析失败而非悄悄生成答案。
2. 每个摘要事实、关系和PPT结论能回到具体论文版本及页/段；抽样人工核查引用是否真正支持结论。没找到原文就标为推测或未知。
3. 用固定查询比较普通混合RAG与图增强是否真的增加正确答案，再决定是否承担图索引成本。
4. 定时任务验证断网重试、同日重复运行去重、预算截止、失败可见；外部工具故障不应损坏Zotero原库。
5. PPT需真实导出和渲染检查，文本/图表可编辑，参考文献可回溯；预览通过再记为成功。

这些是建议实施时的验收，不是本轮已经完成的安装测试。PaperQA2、GPT Researcher、Zotero MCP、Paper2Slides和每日arXiv流程由博客检索智能体另行核验，可与本报告组合，避免把全部开源应用同时堆进系统。
