import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def main() -> None:
    torch.manual_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"device: {device}")

    x = torch.linspace(-1.0, 1.0, 1024).unsqueeze(1)
    y = 3.0 * x + 2.0 + 0.05 * torch.randn_like(x)

    dataset = TensorDataset(x, y)
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

    model = nn.Linear(1, 1).to(device)
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    for epoch in range(1, 21):
        total_loss = 0.0

        for batch_x, batch_y in dataloader:
            batch_x = batch_x.to(device)
            batch_y = batch_y.to(device)

            prediction = model(batch_x)
            loss = loss_fn(prediction, batch_y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item() * batch_x.size(0)

        avg_loss = total_loss / len(dataset)
        if epoch % 5 == 0:
            print(
                f"epoch={epoch:2d} "
                f"loss={avg_loss:.6f} "
                f"weight={model.weight.item():.4f} "
                f"bias={model.bias.item():.4f}"
            )

    print(f"final: weight={model.weight.item():.4f}, bias={model.bias.item():.4f}")


if __name__ == "__main__":
    main()
