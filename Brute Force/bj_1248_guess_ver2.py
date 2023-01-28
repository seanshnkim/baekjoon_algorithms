import sys

N = int(sys.stdin.readline())
signs = sys.stdin.readline()

sign = [[0]*N for _ in range(N)]
ans = [0]*N
cnt = 0

for i in range(N):
    for j in range(i, N):
        if signs[cnt] == '0':
            sign[i][j] = 0
        elif signs[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1
        
        
def ok(idx):
    for i in range(idx):
        s = 0
        for j in range(i, idx):
            s += ans[j]
            if i == j:
                continue
            if sign[i][j] == 0:
                if s != 0:
                    return False
            elif sign[i][j] > 0:
                if s <= 0:
                    return False
            elif sign[i][j] < 0:
                if s >= 0:
                    return False
    return True


def solution(idx):
    if idx == N:
        return ok(idx)
    
    # 1st: sign of ith number
    sign_of_ith = sign[idx][idx]
    curr_range = range(-10, 11)
    if   sign_of_ith < 0:
        curr_range = range(-10, 0)
    elif sign_of_ith > 0:
        curr_range = range(1, 11)
    else:
        curr_range = range(0, 1)
        
    # 2nd: sign of ith sum
    for i in curr_range:
        if ok(idx):
            ans[idx] = i
            if solution(idx+1):
                return True
    return False


solution(0)
print(' '.join(map(str, ans)))



