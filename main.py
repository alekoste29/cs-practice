from pathlib import Path
from runpy import run_path

import numpy as np


def reshap_rows(values, width):
    if width <= 0:
        raise ValueError("width must be positive")
    values = np.asarray(values, dtype=float).ravel()
    padding = -values.size % width
    if padding:
        values = np.pad(values, (0, padding))
    return values.reshape(-1, width).tolist()


def block(matrix, rows, colums):
    matrix = np.asarray(matrix, dtype=float)
    return matrix[np.ix_(rows, colums)].tolist()


def column_means(matrix):
    matrix = np.asarray(matrix, dtype=float)
    return matrix.mean(axis=0).tolist()


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(block(matrix, [0, 2], [1, 2]))
    print(reshap_rows(range(1, 11), 3))
    print(column_means(matrix))
    run_path(str(Path(__file__).parent / "lab08" / "lab08_numpy.py"))
