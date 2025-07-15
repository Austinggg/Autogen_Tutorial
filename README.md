# Autogen Guide

## Environment Setup

```cmd
conda create -n autogen python=3.10
conda activate autogen
pip install requirements.txt
```

需自行配置 `.env`，参考[0-Client](./0-Client.ipynb)

```
OPENAI_API_KEY=sk-sdahdsadkjdhkh
```

教程中所演示的资源都放在 `./resources` 中,(将加入多模态数据~)


## 目录

| 文件/章节                                 | 内容简介                                 |
|-------------------------------------------|------------------------------------------|
| [0-Client.ipynb](./0-Client.ipynb)        | LLM Client 配置与使用方法                |
| [1-Message.ipynb](./1-Messages.ipynb)          | 多智能体对话与协作                |
| [2-Agent.ipynb](./2-Agent.ipynb) | 智能体（Agent）基础与进阶                  |
| [3-Teams.ipynb](./3-Teams.ipynb)          | 多智能体团队与协作机制                   |
| [4-HumanInTheLoop.ipynb](./4-HumanInTheLoop.ipynb) | 人类反馈与交互流程                |
| [5-Termination.ipynb](./5-Termination.ipynb) | 任务终止条件与流程控制                |
| [6-ManagingState.ipynb](./6-ManagingState.ipynb) | 状态管理与断点续聊                  |
| [7-Workflow.ipynb](./7-Workflow.ipynb)    | 工作流与复杂流程编排                     |
| [8-Memory.ipynb](./8-Memory.ipynb)        | 记忆机制与 RAG 检索增强                  |
| [9-Monitor.ipynb](./9-Monitor.ipynb)      | 日志监控与调试                           |


---
持续更新中~

