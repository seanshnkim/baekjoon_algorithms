import sys
input = sys.stdin.readline
from itertools import permutations

def convert(cur_string, alpha2num_dict):
    res = ''
    for s in cur_string:
        # value가 int형은 아니고 숫자 형태의 문자열임
        res += alpha2num_dict[s]
    return int(res)


N = int(input())
words = [input().rstrip('\n') for _ in range(N)]

alphabets = set()
for word in words:
    alphabets.update(set(a for a in word))
alphabets = list(alphabets)
n_alpha = len(alphabets)

words = [(w, len(w)) for w in words]
words.sort(lambda x: x[1])

answer = 0
for perm in permutations(range(10-n_alpha, 10)):
    alph2num_dict = {a:str(n) for a,n in zip(alphabets, perm)}
    cur_sum = 0
    for word in words:
        cur_sum += convert(word, alph2num_dict)
    if cur_sum > answer:
        answer = cur_sum
