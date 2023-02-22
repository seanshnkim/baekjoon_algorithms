import sys
input = sys.stdin.readline

N_vocab, K_char = map(int, input().split())
vocabulary = [input().rstrip('\n') for _ in range(N_vocab)]


def is_indices_valid(indices):
    necessary_idx = [ord(ch)-ord('a') for ch in ['a', 'c', 'i', 'n', 't']]
    for ni in necessary_idx:
        if ni not in indices:
            return False
    return True
    

if K_char < 5:
    print(0)
else:
    cnts_alphabet = [[False]*26 for _ in range(N_vocab)]
    answer = 0 
    
    for a_idx in range(26):
        for v_idx in range(N_vocab):
            if chr(97+a_idx) in vocabulary[v_idx]:
                cnts_alphabet[v_idx][a_idx] = True
    
    for i in range(1<<26):
        cnt_select = 0
        selected_idx = []
        curr_cnt = 0
        for a_idx in range(26):
            if i & (1<<a_idx) != 0:
                cnt_select += 1
                selected_idx.append(a_idx)
        if cnt_select == K_char and is_indices_valid(selected_idx):
            for n in range(N_vocab):
                for si in selected_idx:
                    if cnts_alphabet[n][si]:
                        cnts_alphabet[n][si] = False
            
            for n in range(N_vocab):
                if sum(cnts_alphabet[n]) == 0:
                    curr_cnt += 1
            
            answer = max(answer, curr_cnt)
    
    
    
