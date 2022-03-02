# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

import numpy as np

def main():
    gridLimit = 2
    grid = np.arange(1,(gridLimit * gridLimit)+1).reshape(gridLimit, gridLimit)

    print(grid[1][1])


if __name__ == "__main__":
    main()
