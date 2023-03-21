import sys
input = sys.stdin.readline
DIVISOR = 1000000

INPUT_CODE = input().rstrip('\n')

def solution(input_code):
    len_code = len(input_code)
    # dp[n] = K : n은 자릿수, K는 해석될 수 있는 경우의 수
    dp = [0]*(len_code+1)
    dp[0] = 1
    # A는 1부터 시작. 만약 앞이 0이면 말이 안되는 코드 -> 0 출력
    if input_code[0] != '0':
        dp[1] = 1
    else:
        return 0

    for i in range(2, len_code+1):
        one_digit = input_code[i-1]
        two_digits = input_code[i-2:i]
        if two_digits[0] != '0' and int(two_digits) <= 26:
            dp[i] += dp[i-2]
        if one_digit != '0' and int(one_digit) <= 26:
            dp[i] += dp[i-1]
        
        # 암호가 잘못되어 암호를 해석할 수 없는 경우에는 0을 출력한다.
        if dp[i] == 0:
            return 0
        dp[i] %= DIVISOR
            
    return dp[-1]


print(solution(INPUT_CODE))
# if 해석 안된다 -> 0 출력
# 암호는 5000자리 이하
# 암호는 숫자로 이루어져 있다

'''
A -> 1    G -> 7    M -> 13
B -> 2    H -> 8    N -> 14
C -> 3    I -> 9
D -> 4    J -> 10
E -> 5    K -> 11
F -> 6    L -> 12
Z -> ... 26

암호가 다음과 같이 주어졌다고 해보자.
25 -> BE
   -> Y
   
251 -> BEA
    -> YA
    -> B* ? WRONG

2511 -> BEAA
     -> YAA
     -> BE + K
     -> Y + K

# 세자리 + 두자리
25114 -> BEA + N
      -> YA + N
# or 네자리 + 한자리
'''

