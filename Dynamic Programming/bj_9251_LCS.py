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
    
    if dp[i+1][0] == -1:
        idx_in_strA = strA.rfind(strB_char)
        dp[i][0] = idx_in_strA
        # 아예 현재 strB_char가 strA에 없다면,그냥 [-1,0]으로 냅둬야 한다.
        if idx_in_strA == -1:
            continue
        
        # FIXME - line 29 추가
        dp[i][1] = 1
        # 얘도 마찬가지로 while문 돌려서 dp[i+2][0], dp[i+3][0]... 계속 비교해보면 되지 않나?
        for j in range(i+2, lenB):
            if dp[j][0] != -1:
                if dp[j][0] > idx_in_strA:
                    dp[i][1] = dp[j][1] + 1
                    break
                elif dp[j][0] == idx_in_strA:
                    dp[i][1] = dp[j][1]
                    break
        
    else:
        # NOTE: rfind(value= start= end=) -> end는 "미만"이다(string slicing 규칙과 동일)
        idx_in_strA = strA.rfind(strB_char, 0, dp[i+1][0]+1)
        
        #  strB_char가 strB[i+1] 문자 기준에서 왼쪽에 없다면, 오른쪽으로 탐색한다.
        if idx_in_strA == -1:
            idx_in_strA = strA.rfind(strB_char, dp[i+1][0])
            dp[i][0] = idx_in_strA
            
            # 아예 현재 strB_char가 strA에 없다면,그냥 [-1,0]으로 냅둬야 한다.
            if idx_in_strA == -1:
                continue
            # if idx_in_strA != -1, 최소한 문자 하나는 일치한다는 뜻이므로
            dp[i][1] = 1
            
            for j in range(i+1, lenB):
                if dp[j][0] != -1:
                    if dp[j][0] >= idx_in_strA:
                        if dp[j][0] == idx_in_strA:
                            dp[i][1] = dp[j][1]
                        else:
                            dp[i][1] = dp[j][1] + 1
                        break
            
        else:
            # WRONG: 바로 오른쪽 옆 걸로 업데이트하는 게 아니라, 가장 큰 값으로 업데이트해야 함
            dp[i][0] = idx_in_strA
            dp[i][1] = dp[i+1][1] +1

answer = 0
for idx, length in dp:
    if length > answer:
        answer = length
print(answer)