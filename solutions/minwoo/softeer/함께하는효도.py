from itertools import product

def dfs(y, x, visit, depth, k, paths):
    if depth > 3:
        temp = [(i, j) for i in range(n) for j in range(n) if visit[i][j] == 1]
        paths[k].append(temp)
        return

    visit[y][x] = 1
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = dy+y, dx+x
        if 0 <= ny < n and 0 <= nx < n and visit[ny][nx] == 0:
            dfs(ny, nx, visit, depth+1, k, paths)
    visit[y][x] = 0

def calculate_max_score(friends, board):
    max_score = 0
    for path_combination in product(*friends.values()):
        merged_set = set().union(*path_combination)
        score = sum(board[y][x] for y, x in merged_set)
        max_score = max(max_score, score)
    return max_score

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
paths = {k: [] for k in range(m)}  # 각 친구별 경로 저장을 위한 딕셔너리

# 각 친구별 가능한 모든 경로 탐색
for k in range(m):
    y, x = map(int, input().split())
    visit = [[0] * n for _ in range(n)]
    dfs(y - 1, x - 1, visit, 0, k, paths)

# 모든 친구들의 경로를 고려하여 최대 점수 계산
max_sum = calculate_max_score(paths, board)
print(max_sum)