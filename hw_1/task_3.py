import click
import numpy as np


def generate_matrix(count: int) -> np.matrix:
    data = np.array(shape=(count, count))

    for i in range(0, count):
        for j in range(0, count):
            data[i][j] = i + j - 1

    return np.matrix(data)


@click.command()
@click.option("--count", type=int, required=True)
def main(count: int):
    matrix = generate_matrix(count)

    print(f"Matrix:\n{matrix}")

    u, s, vh = np.linalg.svd(matrix)
    xs = vh[abs(s) < 1e-5]
    
    # check this
    for x in xs:
        result = abs(np.sum(matrix @ x.T)) < 1e-9
        print(f"{x}: {result}")
        

if __name__ == "__main__":
    main()
