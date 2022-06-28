import sys

n = 22
dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]


def go(a, b, c):
    # 1. 기저 사례 & 예외처리
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return go(20, 20, 20)

    # 2. 중복검사
    if dp[a][b][c] is not None:
        return dp[a][b][c]

    # 3. 점화식 구현
    dp[a][b][c] = go(a-1, b, c) + go(a-1, b-1, c) + go(a-1, b, c-1) - go(a-1, b-1, c-1)
    """
    if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    """
    # 4. return
    return dp[a][b][c]


if __name__ == "__main__":
    while True:
        a, b, c = map(int, sys.stdin.readline().split(" "))
        
        if a == b == c == -1:
            break
            
        res = go(a, b, c)
        print("w(%d, %d, %d) = %d" % (a, b, c, res))