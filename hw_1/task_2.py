import click
import numpy as np


def generate_matrix(count: int) -> np.matrix:
    data = np.ndarray(shape=(count, count))

    for i in range(0, count):
        for j in range(0, count):
            div = (i + j -1)
            data[i][j] = 1 / div if div != 0 else 1000000  # Why not?

    return np.matrix(data)


@click.command()
@click.option("--count", type=int, required=True)
def main(count: int):
    matrix = generate_matrix(count)

    print(f"Matrix:\n{matrix}")

    # SVD-based calculate inverse of a matrix
    inv_matrix = np.linalg.pinv(matrix)
    print(inv_matrix)


if __name__ == "__main__":
    main()
