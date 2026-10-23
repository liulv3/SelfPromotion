# 博客实践推荐顺序

整理于 2026-10-23，沿用 2026-10-22 已核验的文章及官方仓库。**建议按下表顺序阅读：先确定证据与验收方法，再接 Zotero，再增加自动调研、推荐和演示输出。** 这是文章参考价值排序，不是整套软件底座排名；未运行项目，不以 Star 或发布频度评价文章质量。

五项评分等权，平均值仅用于排序：**实用性**看是否能指导具体决策；**可迁移性**看思路脱离作者环境后是否仍可用；**教程完整性**看实现步骤、代码和边界是否足够；**项目适配性**看是否直接解决本项目需求；**证据强度**看主张能否追溯到作者实现、官方材料和有边界的实验。各项均为主观 1–5 分：1=很弱，2=局部可用，3=有用但缺口明显，4=较完整，5=在该维度特别值得参考。分数不是实测准确率或可靠性认证。

| 顺序与文章 | 实用 | 迁移 | 教程 | 适配 | 证据 | 均分 | 采用点 / 不采用点 |
|---|---:|---:|---:|---:|---:|---:|---|
| **1. [FutureHouse：PaperQA2 工程实践](https://www.futurehouse.org/research/engineering-blog-journey-to-superhuman-performance-on-scientific-tasks)**；团队原创，2024-09-19，含实验且有开发方宣传立场 | 5 | 4 | 4 | 5 | 5 | **4.6** | **采用**证据重排、上下文摘要和允许“信息不足”的评测设计。**不采用**将特定内部实验中的优势直接当成本项目准确率承诺，也不把其解析实验结论推广到数学推导场景。 |
| **2. [Aaron Taylor：Building an MCP Server for Zotero](https://ataylor.io/blog/zotero-mcp/)**；作者自用实践，2025-02-05 | 5 | 5 | 3 | 5 | 4 | **4.4** | **采用**保留 Zotero、通过少量工具读取搜索结果/元数据/全文的边界。**不采用**把短文视作完整同步教程：增量同步、批注、冲突与回写仍需设计。 |
| **3. [Assaf Elovic：多 Agent 研究流程](https://www.langchain.com/blog/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration)**；LangChain 厂商博客的作者文章，2024-05-09 | 4 | 4 | 5 | 4 | 3 | **4.0** | **采用**任务拆分、独立子任务状态及审阅修订职责。**不采用**固定堆叠七种角色或只靠模型同意结束循环；加轮次、费用、时间和无新证据终止。 |
| **4. [Haoxiang Li：Personalized arXiv Recommendation Service](https://blog.haoxiang.org/2024/02/personalized-arxiv-recommendation-service/)**；个人原创，2024-02-16 | 4 | 4 | 3 | 4 | 3 | **3.6** | **采用**每日短名单、已读/忽略反馈、离线批处理，减少信息负担。**不采用**原文旧费用预算、仅相似度排序即代表研究价值的假设，或将个人使用数周等同长期稳定性证明。 |
| **5. [Hysen Labs：Paper2Slides 分析](https://hysenlabs.com/projects/hkuds-paper2slides)**；第三方 README 分析，页面更新 2026-09-24、署名 Dawson 审阅 2026-10-06 | 3 | 3 | 4 | 3 | 2 | **3.0** | **采用**解析→摘要→计划→生成的阶段划分及检查点。**不采用**其维护活跃度判断或“生成幻灯片即可满足周报”的推论；文章不是实际运行评测，关键结论需回看官方代码。 |

**与代码底座组合的关系：**

- **PaperQA2：代码组件候选。** [官方仓库](https://github.com/Future-House/paper-qa)为 Apache-2.0，可封装成论文证据检索服务；[FAQ](https://github.com/Future-House/paper-qa#faq)说明公开版本与内部系统存在工具和论文访问资源差异，需要自行提供 PDF。锁定版本、接自有证据格式后再测试；它不承担完整产品界面和技术谱系。
- **Zotero MCP：连接层候选。** 对应的是 MIT 的 [kujenga/zotero-mcp](https://github.com/kujenga/zotero-mcp)，不要混为其他同名项目。用于接现有文献库，自己的项目仍负责同步状态、技术关系和确认记录。
- **GPT Researcher：外部调研组件候选。** [官方仓库](https://github.com/assafelovic/gpt-researcher)为 Apache-2.0；可接每日发现与专题报告。若产品已有任务编排器，优先调用其研究能力，避免再叠一套长期运行的 Agent 组织。
- **ArxRec：仅借鉴一般思路。** [仓库](https://github.com/pppoe/ArxRec)未发现明确许可证，不将公开代码当作已获许可的复用组件；独立实现反馈闭环。
- **Paper2Slides：可选试验组件。** [官方仓库](https://github.com/HKUDS/Paper2Slides)为 MIT，末端是图片生成、展示样例为 PDF，不能承诺可编辑 PPTX。最终周报应由 PPT Skill 或原生 PPTX 渲染器接收已确认的大纲与证据；图像生成辅助视觉表达。

**共同空白需要自建：**上述文章都未完整解决可确认的技术谱系、论文身份与版本管理、用户修订保护。无论选择什么界面底座，这些数据与规则都应留在自己的领域服务中。
