#FIXME - https://www.acmicpc.net/board/view/59860
# 정답은 3이나, 출력이 2로 나오는 코드

import sys

N = int(sys.stdin.readline())
arr_2D = []

for n in range(N):
    arr_2D.append(list(sys.stdin.readline().rstrip('\n')))


def search_row(i):
    cnt = max_cnt_row = 1
    for k in range(N-1):
        if arr_2D[i][k] == arr_2D[i][k+1]:
            cnt += 1
        else:
            max_cnt_row = max(max_cnt_row, cnt)
            cnt = 1
    #REVIEW - 실수한 부분: 다시 한번 max 값을 업데이트해주어야 함
    return max(max_cnt_row, cnt)


def search_col(j):
    # 열에 대해 cnt 계산:
    cnt = max_cnt_col = 1
    for k in range(N-1):
        if arr_2D[k][j] == arr_2D[k+1][j]:
            cnt += 1
        else:
            max_cnt_col = max(max_cnt_col, cnt)
            cnt = 1
    #REVIEW - 실수한 부분: 다시 한번 max 값을 업데이트해주어야 함
    return max(max_cnt_col, cnt)


ans = []
max_rows = []
max_cols = []

for i in range(N):
    max_rows.append(search_row(i))
    max_cols.append(search_col(i))

for i in range(N):
    for j in range(N):
        # search toward right
        if j < N - 1 and arr_2D[i][j] != arr_2D[i][j+1]:
            arr_2D[i][j], arr_2D[i][j+1] = arr_2D[i][j+1], arr_2D[i][j]
        
            # 행에 대해 cnt 계산:
            max_cnt_row = max(max_rows[i], search_row(i))
        
            # 열에 대해 cnt 계산:
            max_cnt_col = max(max_cols[j], max(search_col(j), search_col(j+1)))

            ans.append(max(max_cnt_row, max_cnt_col))
            arr_2D[i][j+1], arr_2D[i][j] = arr_2D[i][j], arr_2D[i][j+1]
        
        # search downward
        if i < N -1 and arr_2D[i][j] != arr_2D[i+1][j]:
            arr_2D[i][j], arr_2D[i+1][j] = arr_2D[i+1][j], arr_2D[i][j]
            
            # 행에 대해 cnt 계산:
            max_cnt_row = max(max_rows[i], max(search_row(i), search_row(i+1)))

            # 열에 대해 cnt 계산:
            max_cnt_col = max(max_cols[j], search_col(j))
            
            ans.append(max(max_cnt_row, max_cnt_col))
            arr_2D[i+1][j], arr_2D[i][j] = arr_2D[i][j], arr_2D[i+1][j]

print(max(ans))