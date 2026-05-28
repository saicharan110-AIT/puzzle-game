import heapq

goal_state = [[1,2,3],[4,5,6],[7,8,0]]

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value-1)//3
                goal_y = (value-1)%3
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def solve(initial):
    visited = set()
    heap = []
    count = 0  # 👈 important counter

    heapq.heappush(heap, (0, count, initial))

    while heap:
        cost, _, node = heapq.heappop(heap)

        if node.state == goal_state:
            return node

        visited.add(str(node.state))

        for child in node.possible_moves():
            if str(child.state) not in visited:
                count += 1
                total_cost = child.depth + heuristic(child.state)
                heapq.heappush(heap, (total_cost, count, child))

    return None