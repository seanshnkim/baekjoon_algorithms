import sys
input = sys.stdin.readline

'''
1. 노트를 위에서 아래로
이름을 적어 넣을 때 이미 정해진 순서대로!!!
2. 같은 줄에서는 왼쪽 맨 끝에서 오른쪽으로 차례로
3. 각 사람의 이름 사이에 빈칸을 하나씩 두어야 한다
4. 만약 한 줄에 적다가 그 줄의 끝에 이름 다 들어가지 않고 잘리면 안되므로,
새로운 줄에 이름을 써야 한다.
5. 오른쪽에 남게 되는 칸 수의 제곱의 합이 최소가 되도록 하려고 한다.
6. 제일 마지막 줄은 앞으로 이름을 적을 기회가 있으므로 계산에 넣지 않는다.
'''
# N = 사람 수, M = 칸 가로 크기
N, M = map(int, input().split())
numbers = list(int(input()) for _ in range(N))

# [7, 4, 2, 3, 2, 5, 1, 12, 7, 5, 6]

# dp[n] -> n번째 숫자에서 쓰기를 마쳤을 때, 누적 (제곱) 합의 배열
dp = [[] for _ in range(N)]
dp[0].append([0, M-numbers[0]])

last_idx = 0
acc_reversed = numbers[-1]
for i in range(N-2, -1, -1):
    acc_reversed += numbers[i]+1
    if acc_reversed > M:
        last_idx = i+1
        break


for i in range(1, N):
    least_sum = float('inf')
    for acc_sum, prev_left in dp[i-1]:
        # 같은 줄에 여전히 넣을 수 있다면
        cur_left = prev_left - 1 - numbers[i]
        if cur_left >= 0:
            dp[i].append([acc_sum, cur_left])
        
        # least sum 계산
        tmp = acc_sum + prev_left * prev_left
        if tmp < least_sum:
            least_sum = tmp
    
    # 마지막 항은 항상
    dp[i].append([least_sum, M-numbers[i]])


least_sum = float('inf')
for i in range(last_idx, N):
    
    for acc_sum, prev_left in dp[i]:
        tmp = acc_sum + prev_left * prev_left
        if tmp < least_sum:
            least_sum = tmp

print(least_sum)

'''
dp[0] <- 169
dp[1] <- 
'''


'''
7 4 2 3  : 19
2 5 1 : 10
12 7 : 20
5 6

7 4 2   : 15
3 2 5 1 : 14
12 7 : 20
5 6

7 4 2 3 2 5 1 12 7 5 6
7 ->  0:(0, 13)
4 ->  0:(0, 8), 1:(13^2, 16)
2 ->  0:(0, 5), 1:(13^2, 13), 2:(8^2, 18)
3 ->  0:(0, 1), 1:(13^2, 9), 2:(8^2, 14), 3:(5^2, 17)
2 ->  1:(13^2, 6), 2:(8^2, 11), 3:(5^2, 14), 4:(1^2, 18)
5 ->  1:(13^2, 0), 2:(8^2, 5),  3:(5^2, 8),  4:(1^2, 12), 5:(8^2+11^2, 15)
1 ->  2:(8^2, 3), 3:(5^2, 6),  4:(1^2, 10), 5:(13^2+6^2, 13), 6:(8^2+5^2, 19) -> 5번째에서 끝나는 것 중 제곱 합이 가장 작은 걸 골라야 한다.
12 -> 5:(13^2+6^2, 0), 6:(8^2+5^2, 6), 7:(5^2+6^2, 8)
7 ->  7:(5^2+6^2, 0), 8:(5^2+6^2+8^2, 13)
5 ->  8:7, 9:15
6 ->  8:0, 9:8, 10:14

정리하면,
0에서 끝나는: 13
1에서 끝나는: 8, 13
2에서 끝나는: 5, 13, 18

'''