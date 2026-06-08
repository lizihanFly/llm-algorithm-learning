import torch


def main() -> None:
    torch.manual_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"device: {device}")

    x = torch.linspace(-1.0, 1.0, 256, device=device).unsqueeze(1)
    y = 3.0 * x + 2.0 + 0.05 * torch.randn_like(x)

    weight = torch.randn(1, 1, device=device, requires_grad=True)
    bias = torch.zeros(1, device=device, requires_grad=True)
    lr = 0.2

    for epoch in range(1, 101):
        prediction = x @ weight + bias
        loss = ((prediction - y) ** 2).mean()

        loss.backward()

        with torch.no_grad():
            weight -= lr * weight.grad
            bias -= lr * bias.grad
            weight.grad.zero_()
            bias.grad.zero_()

        if epoch % 20 == 0:
            print(
                f"epoch={epoch:3d} "
                f"loss={loss.item():.6f} "
                f"weight={weight.item():.4f} "
                f"bias={bias.item():.4f}"
            )

    print(f"final: weight={weight.item():.4f}, bias={bias.item():.4f}")


if __name__ == "__main__":
    main()
