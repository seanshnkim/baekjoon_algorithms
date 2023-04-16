import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [ [int(i) for i in input().rstrip('\n')] for _ in range(H)]
board_sum = sum(sum(row) for row in board)

def cal_sum(start_r, start_c, end_r, end_c):
    cur_sum = 0
    for r in range(start_r, end_r+1):
        cur_sum += sum(board[r][start_c:end_c+1])
    
    return cur_sum


ans = 0

if H == 1:
    for c in range(1, W-1):
        first_sum = sum(board[0][0:c])
        
        for cc in range(c+1, W):
            second_sum = sum(board[0][c:cc])
            third_sum = board_sum - (first_sum + second_sum)
            ans = max(ans, first_sum * second_sum * third_sum)
            
    print(ans)
    
elif W == 1:
    for r in range(1, H-1):
        first_sum = sum(board[tmp][0] for tmp in range(r))
        
        for rr in range(r+1, H):
            second_sum = sum(board[tmp][0] for tmp in range(r, rr))
            third_sum = board_sum - (first_sum + second_sum)
            ans = max(ans, first_sum * second_sum * third_sum)

    print(ans)

else:
    for r in range(H):
        for c in range(W):
            # FIXME
            first_sum = cal_sum(0, 0, r, c)
            
            if r == H-1:
                if c == W-1:
                    continue
                else:
                    for rr in range(H-1):
                        second_sum = cal_sum(0, c+1, rr, W-1)
                        third_sum = board_sum - (first_sum + second_sum)
                        ans = max(ans, first_sum * second_sum * third_sum)
                    
                    if c < W-1:
                        for cc in range(c+1, W-1):
                            second_sum = cal_sum(0, c+1, H-1, cc)
                            third_sum = board_sum - (first_sum + second_sum)
                            ans = max(ans, first_sum * second_sum * third_sum)
                    
                    
            else:
                if c == W-1:
                    for cc in range(W-1):
                        second_sum = cal_sum(r+1, 0, H-1, cc)
                        # third_sum =  cal_sum(r+1, cc+1, H-1, W-1)
                        third_sum = board_sum - (first_sum + second_sum)
                        ans = max(ans, first_sum * second_sum * third_sum)
                    
                    if r < H-1:
                        for rr in range(r+1, H-1):
                            second_sum = cal_sum(r+1, 0, rr, W-1)
                            third_sum = board_sum - (first_sum + second_sum)
                            ans = max(ans, first_sum * second_sum * third_sum)
                else:
                    # first trial
                    second_sum = cal_sum(r+1, 0, H-1, c)
                    # third_sum = cal_sum(0, c+1, H-1, W-1)
                    third_sum = board_sum - (first_sum + second_sum)
                    ans = max(ans, first_sum * second_sum * third_sum)
                    
                    # second_trial
                    second_sum = cal_sum(r+1, 0, H-1, W-1)
                    # third_sum = cal_sum(r+1,)
                    third_sum = board_sum - (first_sum + second_sum)
                    ans = max(ans, first_sum * second_sum * third_sum)
            
    print(ans)
            