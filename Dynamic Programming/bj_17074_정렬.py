import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))

# 먼저 numbers[1:]가 정렬되어 있는지 아닌지 확인
cnt = 0
is_sorted = True
i = 0
while i < N-1:
    if numbers[i] > numbers[i+1]:
        if cnt == 1:
            cnt = 0
            break
        
        if i == 0:
            left_max = -float('inf')
        else:
            left_max = numbers[i-1]

        if numbers[i+1] >= left_max:
            if i == N-2:
                cnt = 2
            else:
                cnt += 1
                i += 1
                if numbers[i] > numbers[i+1]:
                    cnt = 0
                    break
                if numbers[i-1] > numbers[i+1]:
                    cnt = 0
                    break
                if numbers[i-1] <= numbers[i+1]:
                    cnt += 1
        else:
            if i == N-2:
                cnt = 1
            else:
                i += 1
                if numbers[i] > numbers[i+1]:
                    break
                if numbers[i-1] > numbers[i+1]:
                    break
                else:
                    cnt += 1
    i += 1

if N == 2:
    print(2)
else:
    print(cnt)