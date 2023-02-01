import sys

H, W = map(int, sys.stdin.readline().split())
board = []
for _ in range(H):
    input_str = sys.stdin.readline().split()
    board.extend(list(int(i) for i in input_str[-1]))

max_sum = 0
#REVIEW - range(1<<(H*W)), range(1<<(H*W+1))
# K 자리수의 이진수 중 가장 큰 수는 2^(K-1) 이다.
# range(1<<K) = 0, 1, 2 ... 2^(K-1)
for bitmask in range(1<<(H*W)):
    curr_board_sum = 0
    checked = [False for _ in range(H*W)]
    
    for bit in range(H*W):
        if checked[bit]:
            continue
        
        checked[bit] = True
        piece_sum = board[bit]
        
        if bitmask & (1<<bit) == 0:
            move = 1
            #REVIEW - and (bit+move) < W 가 아니라 (bit+move) < 
            while bitmask & (1<<(bit+move)) == 0 and ((bit%W) + move) < W:
                piece_sum *= 10
                piece_sum += board[bit+move]
                checked[bit+move] = True 
                move += 1

        else:
            move = W
            # REVIEW -  여기서도 실수? 
            # bitmask & (1<<(bit+move)) == 1 이 아니라 0만 아니면 됨
            while bitmask & (1<<(bit+move)) != 0 and ((bit//W) + move//W) < H:
                piece_sum *= 10
                piece_sum += board[bit+move]
                checked[bit+move] = True 
                move += W
        
        curr_board_sum += piece_sum
        
    max_sum = max(max_sum, curr_board_sum)

print(max_sum)