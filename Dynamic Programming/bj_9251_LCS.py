import sys
input = sys.stdin.readline

strA = input().rstrip('\n')
lenA = len(strA)
strB = input().rstrip('\n')
lenB = len(strB)

# dp[n][0] -> strA에서 일치하는 문자의 idx
# dp[n][1] -> strB에서 n번째 문자 기준, 최장부분수열의 길이
dp = [[-1, 0] for _ in range(lenB)]

for i in range(lenB-1, -1, -1):
    strB_char = strB[i]
    
    if i == lenB-1:
        dp[i][0] = strA.rfind(strB_char)
        dp[i][1] = 1 if dp[i][0] != -1 else 0
        continue
    
    # 코드 수정: 이제 dp[i+1][0]은 strB의 lenB-1~i+1번째까지 문자 중 strA에서 가장 왼쪽에 있던 문자의 idx로 설정
    # strA[dp[i+1][0]]과 일치할지도 모르므로 +1 해줌
    # 아냐, +1 해주면 안돼
    if dp[i+1][0] == -1:
        idx_in_strA = strA.find(strB_char)
    else:
        idx_in_strA = strA.rfind(strB_char, 0, dp[i+1][0])
    
    if idx_in_strA == -1:
        # 그렇다면 더 이상 부분수열을 왼쪽으로 계속 붙여나가, 길이를 증가할 수 없다는 뜻이므로 pass
        dp[i][0] = dp[i+1][0]
        dp[i][1] = dp[i+1][1]
        continue
    # # 같다면?
    # elif idx_in_strA == dp[i+1][0]:
    #     # 같아도 그 왼쪽에 idx가 없다면 없다는 거니까 이것도 노상관
    #     dp[i][0] = dp[i+1][0]
    #     dp[i][1] = dp[i+1][1]
    #     continue
    
    # idx_in_strA가 있다면
    else:
        dp[i][0] = idx_in_strA
        dp[i][1] = dp[i+1][1] +1
    

print(dp[0][1])

'''반례:
AAA
AAAB
정답: 3
출력: 1
'''