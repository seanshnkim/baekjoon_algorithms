from collections import defaultdict

def possible_next(curr_res, N):
    return [curr_n + N, curr_n - N, curr_n * N, curr_n // N, N - curr_n, N // curr_n]


def solution(N, number):
    # if k is made in c times, made_cnt[k] = c
    made_cnt = defaultdict(labmda: -1)
    made_cnt[N] = 1
    
    # dp[k]는 N을 최소 k번 써서 만들 수 있는 모든 수를 담고 있는 리스트
    dp = [[] for _ in range(9)]
    dp[1] = [N]

    if number == N:
        return 1

    i = 1
    while i <= 8:
        for curr_n in dp[i]:
            possible_nums = possible_next(curr_n, N)

            for n in possible_nums:
                if made_cnt[n] == -1:
                    made_cnt[n] = i+1
                    dp[i+1].append(n)
                
                if n == number:
                    return i+1
        
        dp[i+1].append( )


        i += 1

    return answer