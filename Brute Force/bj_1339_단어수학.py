import sys
input = sys.stdin.readline
from collections import defaultdict

def convert(cur_string, alpha2num_dict):
    res = ''
    for s in cur_string:
        # value가 int형은 아니고 숫자 형태의 문자열임
        res += alpha2num_dict[s]
    return int(res)

N = int(input())
words = [input().rstrip('\n') for _ in range(N)]
max_length = max(len(word) for word in words)

alphabets = set()
for word in words:
    for alp in word:
        alphabets.add(alp)
alphabets = list(alphabets)

'''
예를 들어 주어진 단어 중 가장 긴 단어 길이가 5이라면
len(alpha_dict['A']) == len(alpha_dict['B']) == ... 5로 모두 동일하다.
alpha_dict['A'] = [0,1,0,2,3]가 의미하는 건 알파벳 A가 모든 단어 통틀어서
1번째 자릿수에서 1번, 3번째 자리에서 2번, 3번째 자리에서 3번 등장했고 0번째, 2번째에서는 등장 X
'''
alp_dict = defaultdict(lambda: [0]*max_length)
for L in range(max_length):
    for word in words:
        if len(word) >= max_length - L:
            i = L - (max_length - len(word))
            cur_alp = word[i]
            alp_dict[cur_alp][L] += 1

# 비트마스크 연산 개념을 응용했지만, order가 의미하는 건:
# order가 큰 알파벳일수록 해당 알파벳에 더 큰 숫자가 부여되어야 한다
alp_order = []
for alp, counts in alp_dict.items():
    order = 0
    for i in range(max_length):
        # FIXME - 단순히 2를 곱해주면 안된다. order += counts[i] << (max_length-1-i)
        order += counts[i] * 10**(max_length-1-i)
    alp_order.append( (alp, order) )
# order가 큰 순서대로 정렬하되 order가 같다면 알파벳 순서대로 정렬한다(어차피 결과는 같지만,
# 한 가지 결과로 단정해야 하므로 이렇게 정했다)
alp_order.sort(key=lambda x: (-x[1], x[0]))

alpha2num = {}
numbers = list(range(10))
for alp, _ in alp_order:
    alpha2num[alp] = str(numbers.pop())

answer = 0
for word in words:
    answer += convert(word, alpha2num)
print(answer)