import torch
from torch import nn


def main() -> None:
    torch.manual_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"device: {device}")

    x = torch.linspace(-1.0, 1.0, 512, device=device).unsqueeze(1)
    y = 3.0 * x + 2.0 + 0.05 * torch.randn_like(x)

    model = nn.Linear(1, 1).to(device)
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.2)

    for epoch in range(1, 101):
        prediction = model(x)
        loss = loss_fn(prediction, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 20 == 0:
            print(
                f"epoch={epoch:3d} "
                f"loss={loss.item():.6f} "
                f"weight={model.weight.item():.4f} "
                f"bias={model.bias.item():.4f}"
            )

    print(f"final: weight={model.weight.item():.4f}, bias={model.bias.item():.4f}")


if __name__ == "__main__":
    main()
