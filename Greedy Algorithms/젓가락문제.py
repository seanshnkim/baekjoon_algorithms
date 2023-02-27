
# 입력 데이터인 pairs 예시 1:
# [AB, DC, DA, BC]
'''
AB DC DA BC 
AB DA CD BC -> 1
AA BD CD BC -> 2
AA DD BC BC -> 3
AA DD BB CC -> 4
'''
# 정답은 4

# 예시 2:
# [AC, DB, BD, CA]
'''
AC DB BD CA
AC DB BC DA -> 1
AC CB BD DA -> 2
CC AB BD DA -> 3
CC BB AD DA -> 4
CC BB AA DD -> 5
'''
# 정답은 5

# 사람 수는 최대 6명!

def solution(pairs):
    ...