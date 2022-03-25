import click
from dataclasses import dataclass
import numpy as np
import typing as tp


@dataclass
class Point:
    x: float
    y: float

    def get(self) -> np.array:
        return np.array(self.x, self.y, 1)


def read_points(path: str) -> tp.List[Point]:
    points : tp.List[Point] = []

    with open(path, "r") as f:
        for line in f:
            x, y = line.strip("\n").split(" ")
            points.append(Point(x=float(x), y=float(y)))

    assert points, "File can not be empty"
    assert len(points) > 3, "Four points required"
    return points


def create_matrix(lhs: tp.List[Point], rhs: tp.List[Point]) -> np.array:
    matrix = np.array([
        [-lhs[0].x, -lhs[0].y, -1, 0, 0, 0, lhs[0].x * rhs[0].x, lhs[0].y * rhs[0].x, rhs[0].x],
        [0, 0, 0, -lhs[0].x, -lhs[0].y, -1, lhs[0].x * rhs[0].y, lhs[0].y * rhs[0].y, rhs[0].y],

        [-lhs[1].x, -lhs[1].y, -1, 0, 0, 0, lhs[1].x * rhs[1].x, lhs[1].y * rhs[1].x, rhs[1].x],
        [0, 0, 0, -lhs[1].x, -lhs[1].y, -1, lhs[1].x * rhs[1].y, lhs[1].y * rhs[1].y, rhs[1].y],

        [-lhs[2].x, -lhs[2].y, -1, 0, 0, 0, lhs[2].x * rhs[2].x, lhs[2].y * rhs[2].x, rhs[2].x],
        [0, 0, 0, -lhs[2].x, -lhs[2].y, -1, lhs[2].x * rhs[2].y, lhs[2].y * rhs[2].y, rhs[2].y],

        [-lhs[3].x, -lhs[0].y, -1, 0, 0, 0, lhs[3].x * rhs[3].x, lhs[3].y * rhs[3].x, rhs[3].x],
        [0, 0, 0, -lhs[3].x, -lhs[3].y, -1, lhs[3].x * rhs[3].y, lhs[3].y * rhs[3].y, rhs[3].y],
    ])

    return matrix


def get_homography(matrix: np.array) -> np.array:
    _, _, v = np.linalg.svd(matrix)

    result = v[-1].reshape(3, 3)
    scale = result[2][2]
    result = np.round(result / scale, 3)

    return result


@click.command()
@click.option("--lhs_path", "-l", type=click.Path(exists=True), required=True)
@click.option("--rhs_path", "-r", type=click.Path(exists=True), required=True)
def main(lhs_path: str, rhs_path: str):
    lhs_points = read_points(lhs_path)
    rhs_points = read_points(rhs_path)

    assert len(lhs_points) == len(rhs_points), "Num of points must be equal"

    matrix = create_matrix(lhs_points, rhs_points)
    print(matrix)

    homography = get_homography(matrix)
    print(homography)


if __name__ == "__main__":
    main()
