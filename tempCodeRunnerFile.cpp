R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
N = int(input())
for i in range(N, R):
    for j in range(C):
        matrix[i - N][j] += matrix[i][j]
for i in range(R - N):
    print(*matrix[i])
