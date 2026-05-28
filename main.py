from puzzle import Puzzle
from solver import solve

initial_state = [
    [1,2,3],
    [4,0,6],
    [7,5,8]
]

start = Puzzle(initial_state)
result = solve(start)

def print_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent

    path.reverse()

    for step in path:
        for row in step.state:
            print(row)
        print("Move:", step.move)
        print("------")

if result:
    print_path(result)
else:
    print("No solution found")
    