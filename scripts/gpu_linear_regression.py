import torch
from torch import nn


def main() -> None:
    torch.manual_seed(42)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"device: {device}")
    if device.type == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("GPU: unavailable, using CPU")

    x = torch.linspace(-1.0, 1.0, 1000, device=device).unsqueeze(1)
    noise = 0.05 * torch.randn_like(x)
    y = 3.0 * x + 2.0 + noise

    model = nn.Linear(1, 1).to(device)
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    for epoch in range(1, 101):
        prediction = model(x)
        loss = criterion(prediction, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 20 == 0:
            weight = model.weight.item()
            bias = model.bias.item()
            print(
                f"epoch={epoch:3d} "
                f"loss={loss.item():.6f} "
                f"weight={weight:.4f} "
                f"bias={bias:.4f}"
            )

    print(
        "final: "
        f"weight={model.weight.item():.4f}, "
        f"bias={model.bias.item():.4f}"
    )


if __name__ == "__main__":
    main()
