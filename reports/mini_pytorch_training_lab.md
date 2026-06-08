# Mini-PyTorch Training Lab

## 目标

这个小项目用于掌握 PyTorch 训练代码的最小闭环。完成后，应能说清楚：

- Tensor 的 shape 如何变化；
- Autograd 如何根据 loss 自动计算梯度；
- `nn.Module` 如何封装参数和前向计算；
- `Dataset` / `DataLoader` 如何组织小批量训练；
- 一个训练脚本如何从数据、模型、loss、optimizer 跑到结果验证。

## 脚本

- `scripts/01_tensor_shape.py`：Tensor 和 shape；
- `scripts/02_autograd_linear.py`：手写参数 + Autograd；
- `scripts/03_nn_module_regression.py`：`nn.Module` 训练线性回归；
- `scripts/04_dataset_dataloader.py`：小批量 DataLoader 训练。

## 服务器运行

```bash
cd ~/llm_projects/repos/llm-algorithm-learning
git pull
source /usr/local/anaconda3/bin/activate llm-train
python scripts/01_tensor_shape.py
python scripts/02_autograd_linear.py
python scripts/03_nn_module_regression.py
python scripts/04_dataset_dataloader.py
```

## 成功标准

- 四个脚本都能正常运行；
- `02`、`03`、`04` 的 loss 下降；
- 最终 weight 接近 3，bias 接近 2；
- 能解释 batch size、epoch、loss、gradient、optimizer 的作用。

## 本阶段不做

- 不下载大模型；
- 不做 LoRA；
- 不做正式训练；
- 不保存 checkpoint。
