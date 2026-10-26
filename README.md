# SelfPromotion · 个人科研知识工作台

让 Zotero 中读过的论文形成可回想的记忆卡、可核查的技术谱系，以及可复用的科研日报和周报。

**当前阶段：方案与仓库建设，尚未引入上游应用、安装依赖或实现运行功能。** 最新主路线是基于 Open Notebook 原栈进行改造试点，详见 [基底决策](docs/decisions/0002-open-notebook-base.md)。

## 从这里开始

- 新窗口与协作者：[核心约定](AGENTS.md) → [开发交接](docs/HANDOFF.md) → [当前状态](docs/STATUS.md) → [任务文档索引](docs/INDEX.md)。
- 理解产品：[产品范围](docs/product/scope.md)、[当前架构](docs/architecture/current-architecture.md)。
- 看选型：[功能复用清单](docs/architecture/reuse-plan.md)、[项目排序](docs/research/base-project-ranking.md)、[博客排序](docs/research/blog-practice-ranking.md)。
- 开始开发：[目录规范](docs/development/repository-layout.md)、[Git 流程](docs/development/git-workflow.md)。

现阶段可执行检查（Python 3.9+，仅标准库）：

```text
python scripts/check_repo.py
git diff --check
```

没有应用启动命令；代码目录目前只是职责说明。个人论文和笔记默认不进入 Git，Zotero 中已有原件保持原位。上轮根目录文件的去向见 [迁移记录](docs/development/document-migration.md)。
