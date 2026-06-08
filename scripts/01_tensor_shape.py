import torch


def main() -> None:
    print("== Tensor and shape ==")

    x = torch.arange(12, dtype=torch.float32)
    print("x:", x)
    print("x.shape:", tuple(x.shape))

    matrix = x.view(3, 4)
    print("matrix:\n", matrix)
    print("matrix.shape:", tuple(matrix.shape))

    transposed = matrix.T
    print("transposed.shape:", tuple(transposed.shape))

    weights = torch.ones(4, 2)
    product = matrix @ weights
    print("product.shape:", tuple(product.shape))
    print("product:\n", product)

    bias = torch.tensor([10.0, 100.0])
    with_bias = product + bias
    print("with_bias.shape:", tuple(with_bias.shape))
    print("with_bias:\n", with_bias)

    print("success: tensor shape demo finished")


if __name__ == "__main__":
    main()
