import numpy as np


def main():
    lhs = np.array([1., 2., 3.])
    rhs = np.array([2., 1., 3.])

    p_vec = np.cross(lhs, rhs)

    print(lhs)
    print(rhs)

    if p_vec[2] == 0:
        if lhs[0] == rhs[0]:
            print("Same line")
        else:
            print("Parallell line")
    else:
        p_vec = p_vec / p_vec[2]
        print(p_vec[:2])

if __name__ == "__main__":
    main()
