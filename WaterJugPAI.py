from collections import deque

def water_jug_bfs(a, b, target):
    queue = deque([(0, 0)])
    visited = set((0, 0))
    path = {}
    path[(0, 0)] = None

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        if jug1 == target or jug2 == target:
            solution_path = []
            while current_state is not None:
                solution_path.append(current_state)
                current_state = path[current_state]
            solution_path.reverse()
            return solution_path

        next_states = []
        next_states.append((a, jug2))
        next_states.append((jug1, b))
        next_states.append((0, jug2))
        next_states.append((jug1, 0))
        pour_amount = min(jug1, b - jug2)
        next_states.append((jug1 - pour_amount, jug2 + pour_amount))
        pour_amount = min(jug2, a - jug1)
        next_states.append((jug1 + pour_amount, jug2 - pour_amount))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                path[state] = current_state

    return None

if __name__ == '__main__':
    a = int(input("Enter the capacity of jug1: "))
    b = int(input("Enter the capacity of jug2: "))
    target = int(input("Enter the target: "))

    solution = water_jug_bfs(a, b, target)

    if solution:
        print("Path from initial state to solution state:")
        for state in solution:
            print(f"({state[0]}, {state[1]})")
    else:
        print("Solution not possible.")
