import sys
input = sys.stdin.readline
from itertools import product

N = int(input())


def coin2bits(c):
    if c == 'H':
        return 0
    elif c == 'T':
        return 1
    
    
def invert(curr_state, k, invert_column=False):
    if invert_column == False:
        for i in range(N):
            curr_state[k][i] ^= 1
    else:
        for i in range(N):
            curr_state[i][k] ^= 1


def decide_columns(curr_state):
    cnt_tails_total = 0
    
    for c in range(N):
        cnt_tails_col = sum(curr_state[r][c] for r in range(N))
        
        if cnt_tails_col > N//2:
            invert(curr_state, c, invert_column=True)
            cnt_tails_col = N-cnt_tails_col
            
        cnt_tails_total += cnt_tails_col
    
    return cnt_tails_total
    

state = [list(map(coin2bits, [s for s in input().rstrip('\n')])) for _ in range(N)]
answer = float('inf')
bit_rows = product([0,1], repeat=N)

for br in bit_rows:
    tmp_state = state.copy()
    for i in range(N):
        if br[i] == 1:
            invert(tmp_state, i)
    
    answer = min(answer, decide_columns(tmp_state))

print(answer)