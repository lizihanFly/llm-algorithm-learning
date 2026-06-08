# 服务器运行命令

以下命令由用户复制到 FinalShell 执行。仓库地址和仓库名需要替换为实际值。

## 第一次 clone

```bash
cd ~/llm_projects/repos
git clone <你的GitHub仓库地址>
cd <仓库名>
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
cd ~/llm_projects/repos/<仓库名>
git pull
source /usr/local/anaconda3/bin/activate llm-train
python scripts/gpu_linear_regression.py
```

成功标准：

- `git pull` 显示已更新或 `Already up to date`；
- 脚本正常完成 100 epoch。

## 长任务规则

- 当前服务器没有 tmux；
- 后续长任务使用 screen 或 nohup；
- 正式训练前必须先执行 dry-run。
