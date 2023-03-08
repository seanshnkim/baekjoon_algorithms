import sys
input = sys.stdin.readline

N = int(input())
board_init = [list(map(int, input().split())) for _ in range(N)]


# 입력으로 주어지는 row에는 현재 빈칸을 제외한 숫자들만 있다고 하자.
def merge(numbers, reverse=False):
    merged = []
    length = len(numbers)
    if not reverse:
        start = 0
        while start < length:
            if start < length-1 and numbers[start] == numbers[start+1]:
                merged.append(numbers[start] << 1)
                start += 2
            else:
                merged.append(numbers[start])
                start += 1
    else:
        start = length - 1
        while start >= 0:
            if start > 0 and numbers[start] == numbers[start-1]:
                merged.append(numbers[start] << 1)
                start -= 2
            else:
                merged.append(numbers[start])
                start -= 1
    
    return merged


def push_board(push, board):
    new_board = []
    if push == 0 or push == 1:
        for row in board:
            row_numbers = [num for num in row if num > 0]
            # 왼쪽
            if push == 0:
                merged_num = merge(row_numbers)
            # 오른쪽
            else:
                merged_num = merge(row_numbers, reverse=True)
            new_board.append(merged_num + [0]*(N-len(merged_num)))

    
    elif push == 2 or push == 3:
        for c in range(N):
            row_numbers = [board[r][c] for r in range(N) if board[r][c] > 0]
            # 위
            if push == 2:
                merged_num = merge(row_numbers)
            # 아래
            else:
                merged_num = merge(row_numbers, reverse=True)
            new_board.append(merged_num + [0]*(N-len(merged_num)))
    
    return new_board


def solution(board, cnt):
    if cnt == 5:
        return max(max(row) for row in board)
    
    answer = 0
    for p in range(4):
        new_board = push_board(p, board)
        answer = max(answer, solution(new_board, cnt+1))
    
    return answer


print(solution(board_init, 0))