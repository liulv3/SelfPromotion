# Git 与个人 GitHub 工作流

本地已建立 `main` 仓库，第一笔提交保存原始资料，后续提交保存目录和选型变化。当前没有远端或推送；查看真实状态用 `git status`、`git log --oneline`、`git remote -v`。

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

## 后续上传个人 GitHub

先确定个人账号下的目标仓库、名字和可见性，并检查是否已有历史；本轮没有推测这些信息或创建仓库。创建一个空远端时无需自动生成另一份 README/许可证，避免不必要的初始历史分叉。已有远端历史时先获取并比较，不用强推覆盖。

新建空远端后的标准步骤（占位符不是已配置的地址）：

```text
git remote add origin <个人仓库URL>
git remote -v
python scripts/check_repo.py
git status --short --branch
git push -u origin main
```

`origin` 指向个人仓库；未来 `upstream` 可指向 Open Notebook。添加和读取上游不授权向其推送。GitHub CLI 当前未安装，后续可用已授权连接器或 Git 认证方式，没必要为本地初始化安装它。

## 提交与许可证边界

只上传源码、开发文档和明确可公开的小样本；个人论文、私人笔记、用户进度、日报及凭据默认排除。配置示例只用占位值。项目自身发布许可证在公开分发前明确；引入上游时保留其许可证和第三方归属，不能把未来仓库默认设成任意许可证。

忽略规则不是备份：科研数据通过应用备份方案保护，Git 只负责代码和开发文档。迁移文档的初始状态可在基线提交 `725968e` 查看。
