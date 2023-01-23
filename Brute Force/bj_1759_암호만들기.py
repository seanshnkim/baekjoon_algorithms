import sys

pw_len, num_alphabets = map(int, sys.stdin.readline().split())
alphabets = list(sys.stdin.readline().split())
alphabets.sort()


def is_possible_pw(substr):
    cnt_vowel = cnt_conson = 0
    for l in substr:
        if l in ['a', 'e', 'i', 'o', 'u']:
            cnt_vowel += 1
        else:
            cnt_conson += 1
    if not (cnt_vowel >= 1 and cnt_conson >= 2):
        return False
    return True


def solution(substr, start):
    if len(substr) == pw_len:
        if is_possible_pw(substr):
            print(substr)
        return
    
    for i in range(start+1, num_alphabets):
        solution(substr + alphabets[i], i)

    return

solution(alphabets[0], 0)

