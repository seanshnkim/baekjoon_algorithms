numTest = int(input())

# 40으로 썼다가 index error 발생. 사소하지만 실전에선 치명적인 실수니 주의하자.
dp_table = [[0,0] for i in range(41)]

dp_table[0][0] = 1
dp_table[1][1] = 1

def zero_one_cnt(num):
    if dp_table[num] != [0,0]:
        return dp_table[num]
    else:
        # 이 방식은 매 테스트 케이스마다 n = 2 부터(맨 밑바닥부터) 매번 훑어 올라가야 한다는 단점이 있다
        for n in range(2,num+1):
            if dp_table[n] == [0,0]:
                dp_table[n][0] = dp_table[n-2][0] + dp_table[n-1][0]
                dp_table[n][1] = dp_table[n-2][1] + dp_table[n-1][1]
        return dp_table[num]


for t in range(numTest):
    numFib = int(input())
    res = zero_one_cnt(numFib)
    print(res[0], res[1])
