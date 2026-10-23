# 博客检索智能体报告

核验日期：2026-10-22。使用 agent-reach 检索流程，由已连接的网页搜索与 GitHub 只读接口完成。以下是文档与仓库审阅，没有安装、运行或压测项目；“可靠性”指当前证据充分程度与集成风险，不等于实验准确率或生产认证。`pushed_at` 只表示仓库有推送，可能包含文档修改，不代表核心代码最近有改进。

## 结论

建议复用 **PaperQA2 的证据检索组件、GPT Researcher 的外部调研流程、轻量 Zotero MCP 的连接层**，把技术谱系、研究进度和确认后的知识做成自己的产品数据。每日发现可以借鉴 ArxRec 的反馈闭环，周报可借鉴 Paper2Slides 的分阶段流程；后两者不宜直接承担整个系统。

没有发现这些项目已经完整解决“主次分明且可以追溯证据的科研技术谱系”。引用、相似和技术继承是不同关系，必须明确边类型，并由使用者确认关键主干。

## 文章发现链条

| 具体文章 | 作者、日期与性质 | 发现的项目与可用经验 |
|---|---|---|
| [Engineering Blog: Journey to superhuman performance on scientific tasks](https://www.futurehouse.org/research/engineering-blog-journey-to-superhuman-performance-on-scientific-tasks) | FutureHouse 团队；页面列 Andrew White、Sam Rodriques，完整作者还有 Michael Skarlinski、Sam Cox、James Braza；2024-09-19。开发方工程文章，含消融实验，具有自身产品宣传立场。 | [PaperQA2](https://github.com/Future-House/paper-qa)。用检索、证据重排、按问题压缩证据、回答来拆解任务；用包含“信息不足”选项的问题集检验系统。文章实验结论限于其数据、模型和内部实现。 |
| [How to Build the Ultimate AI Automation with Multi-Agent Collaboration](https://www.langchain.com/blog/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration) | 2024-05-09；网页署名 LangChain Team，编者按明确正文作者 Assaf Elovic。维护者原创、框架厂商博客，含代码；不是独立评测。 | [GPT Researcher](https://github.com/assafelovic/gpt-researcher)。负责人、研究、审阅、修订、写作、发布分工；并发子任务使用各自状态，避免互相覆盖。正文展示的审阅循环依赖模型接受，产品必须另加轮次、时间、费用及“无新证据”终止条件。 |
| [Building an MCP Server for Zotero](https://ataylor.io/blog/zotero-mcp/) | Aaron Taylor 个人原创实践；2025-02-05，可核验署名与日期；无独立准确率评测。 | [kujenga/zotero-mcp](https://github.com/kujenga/zotero-mcp)。作者刻意保留搜索、元数据、全文三个工具；很适合把 Zotero 留在原位，再增加知识层。注意它不同于同名的 `54yyyu/zotero-mcp`。 |
| [Personalized arXiv Recommendation Service](https://blog.haoxiang.org/2024/02/personalized-arxiv-recommendation-service/) | Haoxiang Li；2024-02-16。个人自用实践，明确描述自己只使用数周；无独立质量实验。 | [ArxRec](https://github.com/pppoe/ArxRec)。每日离线推荐、静态网页、三档反馈，通过已读/忽略反馈更新兴趣。值得借鉴的是低成本反馈闭环；文章旧价格与运行费用不能作为今天预算。 |
| [Paper2Slides: turning a PDF paper into slides or a poster from the command line](https://hysenlabs.com/projects/hkuds-paper2slides) | 第三方 Hysen Labs 长文；页面称 Dawson 审阅于 2026-10-06、更新于 2026-09-24。主要依据 README 做编辑分析，没有可核验实际跑分；不是项目作者原创，作为补充线索。 | [Paper2Slides](https://github.com/HKUDS/Paper2Slides)。发现可恢复的“解析→提取→计划→生成”流程。技术和维护结论均回到官方仓库核验，没有采纳该文章“多久未更新便说明仍维护”等主观判断。 |

额外阅读：[Artur Magalhães 的 Zotero MCP 搭建文章](https://arturmagalhaes.com/tech/zotero_server/)，2025-06-29，包含配置和实现，适合理解接口；功能重叠，因此没有再增加一个 Zotero 基底候选。

## 项目评估

| 项目 | 适合复用的部分 | 优点 | 缺点与边界 | 可靠性判断及依据 |
|---|---|---|---|---|
| **PaperQA2** | 论文问答、带页码引用的证据收集、精读的资料层 | 针对科学文献；元数据、上下文摘要与重排、可配置模型；当前 README 有图表/公式等多模态能力说明，含测试和评测复现材料。 | 它是组件库，不能直接给出研究进度或技术主树；检索与多次模型调用增加成本；公式被解析出来不等于数学推导经过证明。尤其公开版 FAQ 明确：内部版本使用不能开放的论文访问资源，部分工具如引用遍历尚未与公开版对齐，需自行提供 PDF。 | **优先试点，证据较充分；输出可靠性仍需本领域测试。** Apache-2.0；未归档；API `pushed_at` 2026-10-20。当前 README 说明 2025-12 转 CalVer，去掉跨发布向后兼容保证，必须锁版本和做适配隔离。[仓库/FAQ](https://github.com/Future-House/paper-qa#faq) · [元数据](https://api.github.com/repos/Future-House/paper-qa) |
| **GPT Researcher** | 科研日报中的外部搜索、多来源汇总、自定义研究报告；Agent 编排参考 | Web 与本地资料、MCP、研究报告引用、LangGraph/AG2 示例；有前后端、测试、evals 与部署说明。 | 通用网络研究并非严谨论文精读；有引用不自动证明结论受原文支持；必须替换学术来源、保留证据片段，并限制循环与搜索预算。不能仅靠多个智能体互相同意验收。 | **工程候选较强，学术质量需专项评测。** Apache-2.0；未归档；`pushed_at` 2026-10-10。此次 release 接口读取遇临时传输错误，不据此判断是否缺少发布。[官方 README](https://github.com/assafelovic/gpt-researcher) · [元数据](https://api.github.com/repos/assafelovic/gpt-researcher) |
| **kujenga/zotero-mcp** | Zotero 到自建知识层的窄接口：条目搜索、完整元数据、全文 | 三个工具，维护与权限面较小；支持 Local API/Web API；有 tests、工作流、锁文件、Docker 与 PyPI 安装路径。 | 本身没有语义谱系、阅读状态、增量同步和批注回写；本地路径依赖 Zotero 正在运行，全文仍受 Zotero 能否提取影响。不能把这个项目的三个只读工具推广成“Zotero API 永远只读”。 | **轻量适配首选候选。** MIT；未归档；2026-08-07 发布 0.3.1。需要用用户实际 Zotero 版本做兼容测试，并区分 Web/Local 的搜索行为。[官方 README](https://github.com/kujenga/zotero-mcp) · [0.3.1](https://github.com/kujenga/zotero-mcp/releases/tag/0.3.1) |
| **ArxRec** | 每日推荐的用户反馈机制与轻量交付思路 | 作者具体说明了最近 48 小时论文、个人历史论文与反馈、向量相似度、离线任务、静态展示；产品闭环清晰。 | 单人原型，不含精读/知识图谱/稳定运维；仓库根目录未见 LICENSE、README 或测试目录，API license=null。不能因代码公开便默认能合法复制；建议重新实现其一般思路。 | **设计参考；不作为直接代码基底。** 未归档；`pushed_at` 2026-04-21；这也可能只是内容刷新。公开信息不足以判断稳定性。[仓库](https://github.com/pppoe/ArxRec) · [根目录](https://api.github.com/repos/pppoe/ArxRec/contents) |
| **Paper2Slides** | 从证据到讲述大纲、主题、阶段检查点；论文海报或演示草稿 | MIT；CLI、React/FastAPI 界面；官方 README 有四阶段处理、断点续跑、并行生成和样例。 | 官方代码结构最后阶段是图片生成，展示样例为 PDF；不能直接承诺可编辑 PPTX。README 的“消除信息漂移”等是主张，无本次验证。外部模型、解析依赖、图像中的文字和公式都需检查。`--fast` 会跳过 RAG 索引。 | **可用于设计参考和试验，不做周报最终渲染核心。** 未归档；`pushed_at` 2026-05-20；GitHub releases 查询为空，根目录未见测试目录，这不证明所有子目录都没有测试。周报应接原生可编辑 PPTX 渲染器，图片生成只用于辅助插图。[官方 README](https://github.com/HKUDS/Paper2Slides) · [元数据](https://api.github.com/repos/HKUDS/Paper2Slides) |

## 给 CTO 的可执行约束

1. **保留 Zotero 作为文献与阅读工具。** 自建系统持有 `library_id + item_key` 映射、源版本、证据位置和自己的研究关系。MCP 是工具接口，不是同步算法；增量同步、幂等和冲突处理要另做。
2. **先形成证据对象，再形成摘要、技术关系与幻灯片。** 每条知识关联论文、页码/段落/公式、原文片段、生成版本；用户确认过的知识不会被重新生成覆盖。作者“为什么这么想”的内容标为推测重建，不写成可验证作者事实。
3. **技术谱系用多父关系图保存，用树状主干展示。** “引用”“改进”“采用”“竞争”“同主题”各自明确，主干由用户方向与证据决定；仅向量相似无法判断继承。
4. **多 Agent 的目标是分工与交叉检查，不是投票制造确定性。** 独立审阅需要访问原始证据；每个任务限制最多修订轮数、成本和时间，无新证据时结束并报告争议。
5. **日报先短名单后总结。** 获取→DOI/arXiv ID 去重→偏好过滤→Top-N→读取足够内容→摘要→已读/略过反馈。摘要不可用时明确“仅摘要筛选”，不输出全文级评价；无新结果与抓取失败分开显示。
6. **以用户自己的样本验收。** 用若干已读论文、已知技术关系、容易检索失败的公式与表格，分别检查原文定位、结论受证据支持、错误可修订、任务可恢复、PPT 可编辑且无溢出；把基准数字与当前实际产品表现分开。

本轮未建立定时任务、未安装上述项目、未访问用户 Zotero 文献库、未运行代码。最终采用之前需要一个小样本集成试点；当前报告能支持选型与架构设计，不能保证模型输出质量。
