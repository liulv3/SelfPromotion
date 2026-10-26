# Git 与个人 GitHub 工作流

本地已建立 `main` 仓库，第一笔提交保存原始资料，后续提交保存目录和选型变化。2026-10-26 已连接并首次推送至用户指定的 [liulv3/SelfPromotion](https://github.com/liulv3/SelfPromotion)，`main` 跟踪 `origin/main`。查看真实状态用 `git status`、`git log --oneline`、`git remote -v`。

## 日常开发

使用 `main` + 短期 `feat/<topic>`、`fix/<topic>`、`docs/<topic>` 分支，不引入长期多分支 GitFlow。任务开始先检查已有修改，避免覆盖他人或另一智能体的工作；同一文件尽量只有一名写入者。

```text
git status --short --branch
git switch -c feat/<topic>
python scripts/check_repo.py
git diff --check
git add <明确文件或目录>
git diff --cached --stat
git diff --cached
git commit -m "feat: <具体变化>"
```

代码进入仓库后按改动补充真实测试；当前脚本验证本地链接、文档索引可达性、根目录 Markdown 归属和跟踪边界，不是应用质量测试，也不验证文档内容是否符合代码。提交前对照 [文档维护约定](context-loading.md)同步当前说明，避免在未查看清单时 `git add .`。不强推、不重写已共享历史；大改动保留独立提交。仓库级配置不改动用户全局身份。

## 远端与日常同步

`origin` 为 `https://github.com/liulv3/SelfPromotion.git`。连接时已核验该仓库存在、为空且可写，保留其原有公开可见性；本轮没有重建仓库或更改可见性，完整保留本地初始提交与后续整理历史。

已有仓库不重复执行 `git init` 或 `git remote add`。开始工作先获取并检查远端变化，提交完成后正常推送：

```text
git remote -v
git fetch origin
git status --short --branch
python scripts/check_repo.py
git diff --check
git push origin main
```

若工作分支不是 `main`，推送当前工作分支并按实际协作流程合并；出现远端领先或分叉先比较并整合，不强推覆盖。未来 `upstream` 可指向 Open Notebook，添加和读取上游不授权向其推送。上传使用 Git，连接器用于核验仓库与远端结果；不需要为此安装 GitHub CLI。

首次连接曾因旧本地代理失效而失败，已按本机系统当前代理修正本仓库 `.git/config`；没有修改全局 Git 配置。代理地址、凭据与本机配置不进入版本管理。另一台机器应使用自己的网络与认证配置。

## 提交与许可证边界

只上传源码、开发文档和明确可公开的小样本；个人论文、私人笔记、用户进度、日报及凭据默认排除。配置示例只用占位值。项目自身发布许可证在公开分发前明确；引入上游时保留其许可证和第三方归属，不能把未来仓库默认设成任意许可证。

忽略规则不是备份：科研数据通过应用备份方案保护，Git 只负责代码和开发文档。迁移文档的初始状态可在基线提交 `725968e` 查看。
