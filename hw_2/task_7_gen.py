import click
from dataclasses import dataclass
import numpy as np
import typing as tp


HOMOGRAPHY = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])


@dataclass
class Point:
    x: int
    y: int

    def get(self) -> np.array:
        return np.array([self.x, self.y, 1])


def write_points(path: str, points: tp.List[Point]) -> None:
    with open(path, "w") as f:
        for point in points:
            f.write(f"{point.x} {point.y}\n")

    return points


def generate_points(count: int) -> tp.List[Point]:
    x_sample = np.random.sample(count) * 200 - 100
    y_sample = np.random.sample(count) * 200 - 100

    result: tp.List[Point] = []
    for x, y in zip(x_sample, y_sample):
        result.append(Point(np.round(x), np.round(y)))
    return result


def convert_points(source: tp.List[Point]) -> tp.List[Point]:
    result: tp.List[Point] = []

    for point in source:
        common = HOMOGRAPHY @ point.get()
        common = np.round(common / common[2])
        result.append(Point(x=common[0], y=common[1]))
    return result


@click.command()
@click.option("--lhs_path", "-l", type=click.Path(exists=False), required=True)
@click.option("--rhs_path", "-r", type=click.Path(exists=False), required=True)
@click.option("--count", "-c", type=int, default=5)
def main(lhs_path: str, rhs_path: str, count: int):
    lhs_points = generate_points(count)
    rhs_points = convert_points(lhs_points)

    assert len(lhs_points) == len(rhs_points), "Num of points must be equal"

    write_points(lhs_path, lhs_points)
    write_points(rhs_path, rhs_points)
    print(HOMOGRAPHY)


if __name__ == "__main__":
    main()
