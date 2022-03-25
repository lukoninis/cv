import click
import numpy as np


CAMERA = np.array([
    [400, 0, 960],
    [0, 400, 540],
    [0, 0, 1],
])

ROTATE = np.array([
    [np.cos(np.pi / 4), -np.sin(np.pi / 4), 0, 0],
    [np.sin(np.pi / 4), np.cos(np.pi / 4), 0, 0],
    [0, 0, 1, -10],
])

@click.command()
@click.argument("x", type=int, required=True, nargs=1)
@click.argument("y", type=int, required=True, nargs=1)
@click.argument("z", type=int, required=True, nargs=1)
def main(x: int, y: int, z: int):
    point = np.array([x, y, z, 1])

    point_in_camera = CAMERA @ (ROTATE @ point)
    point_in_image = (point_in_camera / point_in_camera[2])[:2]

    print(point_in_image)


if __name__ == "__main__":
    main()
