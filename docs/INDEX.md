# 文档索引：按当前任务读取

先看 [当前状态](STATUS.md)，再选择下表的一条路径。通常先读 1–3 份；只有解决具体问题需要时，才展开附录和历史材料。不要把所有文件一起塞入新会话。

## 当前权威入口

| 本次目标 | 首先读取 | 需要时再展开 |
|---|---|---|
| 理解项目/确认范围 | [产品范围](product/scope.md)、[当前架构](architecture/current-architecture.md) | [基底决策](decisions/0002-open-notebook-base.md) |
| 调整目录、Git、发布准备 | [目录规范](development/repository-layout.md)、[Git 流程](development/git-workflow.md) | [上下文读取约定](development/context-loading.md)、[管理方法证据](development/methods-research.md) |
| 选底座、复用上游 | [基底决策](decisions/0002-open-notebook-base.md)、[项目排序](research/base-project-ranking.md) | [博客排序](research/blog-practice-ranking.md)、2026-10-22 检索证据 |
| 做 Zotero/身份/技术谱系 | [文献与技术链](product/library-and-lineage.md)、[当前架构](architecture/current-architecture.md) | [平台接口参考](engineering/platform.md)；其中旧 SQLite 栈已被新 ADR 调整 |
| 做精读/数学/Skill | [解读与 Skill](product/reading-and-skills.md)、[当前架构](architecture/current-architecture.md) | [AI 执行参考](engineering/intelligence.md)、[架构一手资料](research/architecture-sources.md) |
| 做每日发现/科研进度/周报 | [科研管家与报告](product/steward-and-reports.md)、[当前架构](architecture/current-architecture.md) | [工程流程参考](engineering/operations.md)；执行机制需要适配上游 |
| 核查质量/设计测试 | [解读质量边界](product/reading-and-skills.md)、[试点出口](decisions/0002-open-notebook-base.md) | [评测目录说明](../evals/README.md)、[测试目录说明](../tests/README.md) |
| 追踪为什么改了方案 | [决策目录](decisions/README.md) | 下方历史资料；新决策保留旧结论的来源和替代关系 |

## 资料与历史：按问题展开

| 文件 | 用途与状态 |
|---|---|
| [2026-10-22 GitHub 检索](research/2026-10-22/github-projects.md) | 原始项目事实、许可证、维护证据；不是当前排名 |
| [2026-10-22 博客检索](research/2026-10-22/blog-practices.md) | 文章发现链和官方回源；发布日期不等于当前软件状态 |
| [初始建议书](proposals/2026-10-22-initial-proposal.md) | 首轮完整产品讨论，部分技术栈已被 ADR 0002 调整 |
| [首轮 CTO 架构](architecture/overview.md) | 2026-10-22 的工程裁决与旧工期假设，保留历史 |
| [架构逻辑图](assets/architecture/overview.png) | 逻辑模块示意，图中的框不等于独立服务 |
| [绘图记录](assets/architecture/generation.md) | 提示词、模型可核验边界和目视检查记录 |
| [旧交付索引](archive/2026-10-22-delivery-index.md) | 历史归档，不作为新会话起点 |
| [文件迁移映射](development/document-migration.md) | 将旧会话中的文件名映射到当前位置 |

## 文档维护规则

当前事实写 `STATUS.md`，产品需求写 `product/`，技术现状写 `architecture/current-architecture.md`，关键取舍写 `decisions/`，调研证据写 `research/`。历史讨论不覆盖当前决策；变更时增加或标记替代记录。添加文档时给出用途和入口，迁移时修复引用。每次需要多少上下文由任务决定，不以“全部读过”为目标。
