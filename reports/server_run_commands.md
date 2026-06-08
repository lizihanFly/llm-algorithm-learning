# 服务器运行命令

以下命令由用户复制到 FinalShell 执行。

## 第一次 clone

```bash
mkdir -p ~/llm_projects/repos
cd ~/llm_projects/repos
git clone https://github.com/lizihanFly/llm-algorithm-learning.git
cd llm-algorithm-learning
source /usr/local/anaconda3/bin/activate llm-train
python scripts/gpu_linear_regression.py
```

成功标准：

- `git clone` 完成后出现仓库目录；
- 激活环境后命令行显示 `(llm-train)`；
- 脚本打印 `device: cuda` 和 RTX 2080 的 GPU 名称；
- 最终 weight 接近 3，bias 接近 2。

## 后续更新

```bash
cd ~/llm_projects/repos/llm-algorithm-learning
git pull
source /usr/local/anaconda3/bin/activate llm-train
python scripts/gpu_linear_regression.py
```

成功标准：

- `git pull` 显示已更新或 `Already up to date`；
- 脚本正常完成 100 epoch。

## Mini-PyTorch Training Lab

```bash
cd ~/llm_projects/repos/llm-algorithm-learning
git pull
source /usr/local/anaconda3/bin/activate llm-train
python scripts/01_tensor_shape.py
python scripts/02_autograd_linear.py
python scripts/03_nn_module_regression.py
python scripts/04_dataset_dataloader.py
```

成功标准：

- 四个脚本都能正常结束；
- 回归脚本的 loss 下降；
- 最终 weight 接近 3，bias 接近 2。

## 长任务规则

- 当前服务器没有 tmux；
- 后续长任务使用 screen 或 nohup；
- 正式训练前必须先执行 dry-run。
