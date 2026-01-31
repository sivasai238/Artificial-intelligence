def water_jug(a, b, target):
    visited = set()
    stack = [(0, 0, [])]
    while stack:
        curr_a, curr_b, path = stack.pop()
        if (curr_a, curr_b) in visited: continue
        visited.add((curr_a, curr_b))
        new_path = path + [(curr_a, curr_b)]
        if curr_a == target or curr_b == target: return new_path
        # Rules: Fill, Empty, Pour
        moves = [(a, curr_b), (curr_a, b), (0, curr_b), (curr_a, 0),
                 (curr_a - min(curr_a, b - curr_b), curr_b + min(curr_a, b - curr_b)),
                 (curr_a + min(curr_b, a - curr_a), curr_b - min(curr_b, a - curr_a))]
        for m in moves: stack.append((*m, new_path))

print("Water Jug Path:", water_jug(4, 3, 2))
