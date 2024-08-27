def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    path = []
    visited = set()
    visited.add(start)

    while stack:
        current = stack.pop()
        path.append(current)
        
        if current == end:
            return path
        
        x, y = current
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and
                maze[nx][ny] == 0 and (nx, ny) not in visited):
                stack.append((nx, ny))
                visited.add((nx, ny))
    
    return None


maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]


start = (0, 0)
end = (4, 4)


path = dfs(maze, start, end)
if path:
    print("Caminho encontrado:")
    print(path)
else:
    print("Nenhum caminho encontrado.")
