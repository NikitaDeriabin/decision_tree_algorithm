from main import *

rows = [
    [-6.16, 8.7, -0.21, -3.63, None],
    [-4.07, 2.92, 0.87, -0.65, None],
    [2.8, 6.9, -0.79, 0.48, None]
]

print(decision_tree(dataset, rows, max_depth, min_size))
