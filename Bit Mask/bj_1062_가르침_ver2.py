import sys
input = sys.stdin.readline
from itertools import combinations

N_vocab, K_char = map(int, input().split())
vocabulary = [input().rstrip('\n') for _ in range(N_vocab)]

if K_char < 5:
    print(0)
else:
    char_sets = [set(vocab)-set(['a', 'c', 'i', 'n', 't']) for vocab in vocabulary]
    # FIXME - answer = 0 으로 단순히 초기화하면 안돼
    answer = 0
    for cs in char_sets:
        if len(cs) == 0:
            answer += 1
    
    total_char_set = set()
    for s in char_sets:
        # total_char_set += s
        # 파이썬 집합 연산 잘 안 다루다보니까...
        # REVIEW
        # setA.union(setB) -> setA의 상태는 변하지 않는다. 리턴한 값을 다시 넣어줘야 함
        total_char_set = total_char_set.union(s)
    
    total_char_list = list(total_char_set)
    # 에러 발생 원인 -> combinations(iterable_1, iterable_2)에서 
    # len(iterable_1) < len(iterable_2이면 빈 리스트를 반환하기 때문이다.
    if len(total_char_list) <= K_char-5:
        print(N_vocab)
        sys.exit(0)
        
    comb = combinations(total_char_list, K_char-5)
    
    # answer = 0
    for selected_chars in comb:
        selected_chars_set = set(selected_chars)
        cnt = 0
        for char_set in char_sets:
            if len(char_set - selected_chars_set) == 0:
                cnt += 1
        
        answer = max(answer, cnt)
    
    print(answer)