# 仓库目录与资料归属

当前仓库是规划与开发主仓库。应用目录尚无上游源码；以下为已建立的职责边界，空的预留目录由后续引入步骤创建。采用 Open Notebook 原栈时保留其内部目录，避免为了套自定目录大规模搬动上游文件。

```text
SelfPromotion/
  AGENTS.md                 唯一核心约定
  README.md                 人类项目入口
  docs/
    INDEX.md                按任务导航
    HANDOFF.md              新窗口接手背景、步骤与阶段依赖
    STATUS.md               当前事实与下一步
    product/                产品范围、模块能力与质量边界
    architecture/           当前架构及标注日期的旧方案
    engineering/            详细接口/实现讨论参考
    decisions/              ADR：选择、理由、代价与替代关系
    development/            Git、目录、上下文及管理方法
    research/               项目选型证据与博客评价
    proposals/ archive/     历史方案与交付记录
    assets/                 可公开的开发图示及提示词
  apps/
    notebook/               预留：锁定版本的 Open Notebook 应用
  packages/
    research-core/          自有科研领域逻辑；通过 API/适配器连接上游
    contracts/              稳定 schema、接口与小型无隐私示例
  renderers/pptx/           可编辑 PPT 输出适配器
  skills/                   产品的声明式解读/汇报 Skill
  tests/                    代码/集成测试；只放合成或获准公开小样本
  evals/                    评测方案、脱敏标注与数据集清单
  scripts/                  仓库检查与后续可重复开发脚本
  data/                     本地个人资料和运行数据，默认不入 Git
    papers/ notes/          独立导入论文/获准快照、个人阅读笔记
    db/ indexes/ cache/     数据库、可重建索引、缓存
    artifacts/ logs/        解析产物与运行记录
    backups/                本地备份；不是 Git 的替代品
  outputs/                  生成日报、周报和 PPT，默认不入 Git
```

## 哪些进入 Git

代码、产品/开发文档、接口 schema、经过脱敏的配置示例、依赖锁文件、可再分发的小测试样本进入 Git。`data/` 和 `outputs/` 只跟踪各自 README，里面的个人 Markdown 笔记也被排除。密钥、`.env`、数据库、模型权重、缓存和日志不进入 Git。

Git 忽略不能撤销已经跟踪的文件，提交前检查清单。必要的大型公开基准应提供下载清单和校验值，明确许可后再决定专门存储方式；目前不因两张架构 PNG 就引入 Git LFS。

## 论文放哪里

Zotero 已有原件保持原位，项目保存身份/版本/附件关联，不复制其完整库。独立上传的 PDF 与获准保留的不可变快照进入 `data/papers/`；解析结果进入 `data/artifacts/`。科研私人笔记在 `data/notes/`，项目开发说明在 `docs/`，两者不要混放。默认路径可在后续应用配置中调整，不把本机绝对路径硬编码进源码。

## 上游怎么进入

主仓库保持单一 Git 历史。后续将选定 Open Notebook commit 以明确的上游导入方式放入 `apps/notebook/`，保留原许可证与目录；优先采用可审计的 Git subtree/导入提交，而不是嵌套 Git 仓库或直接拼接多个项目的源码。该路径现在没有上游文件；本轮不执行导入。

自有领域逻辑隔离在 `packages/research-core/`，其持久层优先适配上游数据库，不因代码隔离就新增第二个正式知识库。跨前后端只共享必要 schema。实际接口在试点中校准后再建包和依赖，不创建空的可运行项目来冒充完成。

## 开发和使用中的归档规则

- 根目录只放项目入口、许可证/贡献规范和必要构建配置；方案、会议总结和调研统一归入 `docs/` 对应主题。新目录先明确职责，不用多个 `misc`、`temp`、`new` 存相同内容。
- 新开发文档须被 `docs/INDEX.md` 或它链接的下级文档引用；模块扩大后再增加模块 README，不为每个代码文件写一份重复说明。
- 同一主题维护当前正文，旧选择通过 ADR/Git 追溯；废弃材料明确标记，不与当前入口并列为最新方案。
- 上游代码保留原目录，改造集中在少量挂接点与自有模块；导入时记录仓库、commit、许可证、挂接位置和后续升级方法。
- 应用实现时按稳定标识生成路径：论文可采用 `data/papers/<paper_id>/<version_id>/`，解析产物采用 `data/artifacts/<run_id>/`，报告采用 `outputs/<类型>/<日期>/<report_id>/`；各自保存来源/版本/状态清单，避免依靠手工文件名辨认。此项目前是实现要求，不是已经运行的机制。
- 临时开发文件放被忽略的 `_scratch/`，缓存必须可重建；清理缓存不能误删原文、用户笔记或已确认产物。需要保留的成果及时移入正式目录，个人数据备份与源码 Git 分开。

维护与检查责任见 [上下文与文档维护约定](context-loading.md)。
