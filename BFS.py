from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (current, path) = queue.popleft()

        if current == end:
            return path

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            if (0 <= next_row < rows and 0 <= next_col < cols and
                maze[next_row][next_col] == 0 and (next_row, next_col) not in visited):
                visited.add((next_row, next_col))
                queue.append(((next_row, next_col), path + [(next_row, next_col)]))
                
    return None

# Definindo o labirinto
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

# Encontrar o caminho
path = bfs(maze, start, end)
print("Caminho encontrado:", path)
