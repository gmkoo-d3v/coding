def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]

    answer = []

    def dfs(r, c):
        stack = [(r, c)]
        visited[r][c] = True
        total = 0

        while stack:
            r, c = stack.pop()
            total += int(maps[r][c])

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if maps[nr][nc] != 'X' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        stack.append((nr, nc))

        return total

    for r in range(rows):
        for c in range(cols):
            if maps[r][c] != 'X' and not visited[r][c]:
                answer.append(dfs(r, c))

    return sorted(answer) if answer else [-1]