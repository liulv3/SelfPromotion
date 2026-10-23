# 架构相关一手资料核验

核验日期：2026-10-22。本文件记录选型证据，不表示已安装、集成或通过项目验收。

- [Zotero Local API](https://www.zotero.org/support/dev/web_api/v3/local_api)：本机 API 可离线读取；当前文档描述 Zotero 10+ 支持经用户授权写入。客户端必须按实际版本与接口能力探测；本地实例和 Web API 的对象版本不能混用。建议首版以只读联动开始，不直接写 Zotero 数据库。
- [Docling 文档模型](https://docling-project.github.io/docling/reference/docling_document/)：原文元素可携带页面与位置来源信息，可作为证据定位基础。这不等于 OCR、公式识别或结论解释一定正确。
- [Docling 仓库](https://github.com/docling-project/docling)：GitHub API 返回未归档、MIT，2026-10-22 有推送；[v2.142.0](https://github.com/docling-project/docling/releases/tag/v2.142.0) 的发布时间为 2026-10-22 UTC。代码许可证不自动代表所有模型权重与附属资源许可证。
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)：检查点用于恢复任务状态，store 用于跨任务数据；内存 checkpointer 无法跨进程重启保留状态。断点恢复仍需业务幂等、持久存储与副作用控制。
- [LangGraph 仓库](https://github.com/langchain-ai/langgraph)：GitHub API 返回未归档、MIT，2026-10-22 有推送。
- [PptxGenJS](https://github.com/gitbrent/PptxGenJS)：支持原生文本、表格、图表、母版等 PPTX 对象；GitHub API 返回 MIT、未归档，最近推送为 2025-11-28 UTC；[v4.0.1](https://github.com/gitbrent/PptxGenJS/releases/tag/v4.0.1) 发布于 2025-06-26 UTC。可作可编辑周报渲染器候选；排版、字体、公式与不同 Office 程序兼容性需要实际渲染验收。
- [arXiv API 手册源文档](https://github.com/arXiv/arxiv-docs/blob/develop/source/help/api/user-manual.md)：支持提交日期筛选与版本更新时间，连续调用建议间隔 3 秒。每日采集需处理迟到记录、修订版本和重复数据，不能仅凭一次当日查询保证完整。
- [OpenAlex 当前鉴权说明](https://help.openalex.org/api/authentication/)与[官方变更博客](https://blog.openalex.org/openalex-api-new-features-and-usage-based-pricing/)：访问预算与鉴权会变化，应在连接器中配置额度和退避；本方案不承诺无限免费访问。

核验边界：已读取官方文档、README、仓库元信息与部分 release；未运行这些项目。GitHub 连接器对本轮 `/actions/workflows` 查询返回不支持，因此不能据此确认这些组件的当前 CI 结果。
