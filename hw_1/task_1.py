import numpy as np


def main():
    matrix = np.matrix([
        [0.5, 2.16506351, 0.4330127],
        [-0.8660254, 1.25, 0.25],
        [0., 0.5, 2.5]
    ])

    u, _, vh = np.linalg.svd(matrix)

    print(matrix)

    ort_matrix = u * vh
    print(ort_matrix)

    # it seems like rotate over OZ.
    # angle:
    print((180 / np.pi) * np.arcsin(ort_matrix[0, 0]))


if __name__ == "__main__":
    main()
