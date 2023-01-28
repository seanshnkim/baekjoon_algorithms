from itertools import permutations
import pandas as pd

def solution_false(seq):
    N = len(seq)
    seq = list(seq)
    idx = N-1
    while idx > 0 and seq[idx-1] > seq[idx]:
        idx -= 1

    if idx == 0:
        return -1

    next_val = seq[idx-1] + 1
    next_idx = seq.index(next_val)
    seq[idx-1], seq[next_idx] = next_val, seq[idx-1]
    seq[idx:] = sorted(seq[idx:])
    
    return ' '.join(map(str, seq))


def solution_true(a):
    a = list(a)
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return -1
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return ' '.join(map(str,a))

false_answers = {}
true_answers = {}
for i in range(2, 11):
    for p in permutations(range(1, i)):
        false_answers[p] = solution_false(p)
        true_answers[p] = solution_true(p)

pd.DataFrame.from_dict(data=false_answers, orient='index').to_excel("false_answer.xlsx")
pd.DataFrame.from_dict(data=true_answers, orient='index').to_excel("true_answer.xlsx")