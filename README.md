# 大模型算法学习与 LoRA 微调实践

## 项目目标

本项目用于从零学习大模型算法技术栈，并逐步完成可复现、可评测、可二次开发的训练项目。目标方向包括大模型算法、NLP、模型微调以及 LLM 训练与评测。

当前阶段专注 PyTorch、Transformer、Hugging Face、PEFT/LoRA 和模型评测，不以 RAG、Agent 或 Streamlit 应用为主线。

## 技术路线

Python → NumPy / Pandas / Matplotlib → PyTorch → 深度学习基础 → Transformer → Hugging Face Transformers → Datasets → PEFT / LoRA / QLoRA → 模型评测 → GitHub 项目复现 → 服务器训练 → 简历包装

## 本地与服务器分工

### 本地电脑

- 学习基础知识并阅读源码；
- 编写和调试小规模示例；
- 准备少量样例数据；
- 编写脚本、README 和实验报告；
- 使用 Git 管理代码。

### 服务器

- 运行 PyTorch GPU 验证；
- 执行 dry-run、训练和评测；
- 保存不提交 GitHub 的 checkpoint、模型和日志；
- 执行需要较长时间的任务。

## 当前服务器环境

- 用户：`lizihan`
- 用户目录：`/home/lizihan`
- GPU：NVIDIA GeForce RTX 2080，8GB
- conda 环境：`llm-train`
- Python：3.10.4
- PyTorch：2.6.0+cu118
- CUDA available：True
- transformers：4.46.3
- accelerate：1.1.1
- peft：0.13.2

## 已完成

服务器已完成 PyTorch GPU 最小训练闭环验证。线性回归 toy demo 的目标函数为 `y = 3x + 2 + noise`，最终结果约为：

- weight ≈ 3.002
- bias ≈ 1.996

## 在服务器运行

首次获取项目后，进入仓库并激活环境：

```bash
cd ~/llm_projects/repos/<仓库名>
source /usr/local/anaconda3/bin/activate llm-train
python scripts/gpu_linear_regression.py
```

脚本会自动选择 CUDA 或 CPU，并输出 device、GPU 名称、loss、weight 和 bias。训练结束时，weight 应接近 3，bias 应接近 2。

更完整的 clone、pull 和长任务说明见 `reports/server_run_commands.md`。

## Mini-PyTorch Training Lab

第一个正式学习小项目用于掌握 PyTorch 训练脚本的最小闭环：

- `scripts/01_tensor_shape.py`：学习 Tensor、shape、view、matmul 和广播；
- `scripts/02_autograd_linear.py`：不用 `nn.Module`，手写参数并用 Autograd 拟合线性函数；
- `scripts/03_nn_module_regression.py`：使用 `torch.nn.Linear`、`MSELoss` 和 optimizer；
- `scripts/04_dataset_dataloader.py`：使用 `TensorDataset` 和 `DataLoader` 组织小批量训练。

服务器运行方式：

```bash
cd ~/llm_projects/repos/llm-algorithm-learning
source /usr/local/anaconda3/bin/activate llm-train
python scripts/01_tensor_shape.py
python scripts/02_autograd_linear.py
python scripts/03_nn_module_regression.py
python scripts/04_dataset_dataloader.py
```

成功标准：脚本能正常结束；回归脚本的 weight 接近 3，bias 接近 2。

## 下一步学习计划

1. 完成 Mini-PyTorch Training Lab；
2. Mini-Transformer；
3. Hugging Face 模型推理；
4. LoRA / PEFT 微调。
