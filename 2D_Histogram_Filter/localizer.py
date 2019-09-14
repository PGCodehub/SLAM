import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = beliefs

    #
    # TODO - implement this in part 2
    height = len(beliefs)
    width = len(beliefs[0])
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            hit = (color == grid[i][j])

            new_beliefs[i][j] = cell*(p_hit * hit + (1- hit) * p_miss)

    s = 0
    for i, row in enumerate(new_beliefs):

        for j, cell in enumerate(row):

            s += cell


    for i, row in enumerate(new_beliefs):
        for j, cell in enumerate(row):

            new_beliefs[i][j] = cell  / s


    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]

    heighti = len(new_G)
    widthi = len(new_G[0])

    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i - dy ) % height
            new_j = (j - dx ) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
