# 架构图生成记录

- 最终文件：`overview.png`。
- 初稿：`overview-draft.png`。
- 方法：使用内置 `image_gen` 生成，随后以同一工具补齐 Zotero 接入与活动账本通向知识底座的两条箭头；未用程序重绘或替代图像生成。
- 初始完整提示词：`prompt.txt`。
- 模型边界：当前工具不公开模型选择参数或可核验模型标识，因此无法确认用户指定的 image2。图像本身已生成并进行文字、模块、箭头与层级目视检查。
- 本图为产品与逻辑模块架构，具体部署/进程/数据表分工见 CTO 工程裁决。

最终编辑提示词：

Edit the provided software architecture diagram with exactly one narrow change: add two thin blue downward arrows in the white gap between layer 02 and layer 03. First arrow: from the bottom center of the '只读联动' card to the top edge of the wide '证据与知识底座' card, vertically aligned under the left source column. Second arrow: from the bottom center of the '真实活动账本' card to the top edge of the same wide foundation card, vertically aligned under the right source column. The existing middle arrow and '接纳后' label stay unchanged. Preserve all Chinese text, every icon, all layout geometry, colors, title, footer, and all other arrows exactly. No added labels, no other changes. These arrows complete the three input paths to the shared foundation.
