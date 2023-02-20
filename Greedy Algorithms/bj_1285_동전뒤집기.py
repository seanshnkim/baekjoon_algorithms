import sys
input = sys.stdin.readline

N = int(input())

def coin2bits(c):
    if c == 'H':
        return 0
    elif c == 'T':
        return 1
    
    
# def invert(curr_state, k, invert_column=False):
#     if invert_column == False:
#         for i in range(N):
#             curr_state[k][i] ^= 1
#     else:
#         for i in range(N):
#             curr_state[i][k] ^= 1


# def decide_columns(curr_state, inverse=False):
#     cnt_tails_total = 0

#     for c in range(N):
#         cnt_tails_col = sum(curr_state[r][c] for r in range(N))
        
#         if cnt_tails_col > N//2:
#             cnt_tails_col = N-cnt_tails_col
            
#         cnt_tails_total += cnt_tails_col
        
#     return cnt_tails_total


state = [list(map(coin2bits, [s for s in input().rstrip('\n')])) for _ in range(N)]
answer = float('inf')
# bit_rows = product([0,1], repeat=N)

# FIXME - 매번마다 리스트의 복사본을 만들고 변경하려니까 너무 오래 걸리는 것
# for br in bit_rows:
for curr_state in range(1<<N):
    # tmp_state = state.copy()
    curr_state_min_cnt = 0
    for c in range(N):
        min_cnt_col = 0
        # if br[i] == 1:
        for r in range(N):
            curr_bit = state[r][c]
            # 그때그때마다 바로 적용한다. 바로 아래 if문은, 해당 행을 invert했다는 뜻
            if (curr_state & (1<<r)) != 0:
                curr_bit = state[r][c] ^ 1
            
            min_cnt_col += curr_bit
        
        if min_cnt_col > N//2:
            min_cnt_col = N-min_cnt_col
            
        curr_state_min_cnt += min_cnt_col
    
    answer = min(answer, curr_state_min_cnt)

print(answer)