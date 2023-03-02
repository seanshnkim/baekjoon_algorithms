import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N) ]


# len(arr) = N
def search_path(arr):
    built = [False]*N
    
    for i in range(N-1):
        curr_val = arr[i]
        
        if curr_val - arr[i+1] == 1:
            bottom = arr[i+1]
            for j in range(i+1, i+L+1):
                if j >= N or arr[j] != bottom or built[j]:
                    return False

            for j in range(i+1, i+L+1):
                built[j] = True
                
        elif arr[i+1] - curr_val == 1:
            bottom = curr_val
            for j in range(i, i-L, -1):
                if j < 0 or arr[j] != bottom or built[j]:
                    return False

            for j in range(i, i-L, -1):
                built[j] = True
                
        elif abs(curr_val - arr[i+1]) > 1:
            return False
    
    return True
        
# 행
answer = 0
for r in range(N):
    if search_path(board[r]):
        answer += 1

# 열
for c in range(N):
    curr_column = [board[i][c] for i in range(N)]
    if search_path(curr_column):
        answer += 1

print(answer)