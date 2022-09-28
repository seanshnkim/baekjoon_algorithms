import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
inordered = list(map(int, (sys.stdin.readline().split())))
postordered = list(map(int, (sys.stdin.readline().split())))

inordered_val2idx = [0 for _ in range(N+1)]
for i in range(N):
    inordered_val2idx[inordered[i]] = i

preordered = []

def preorder(start, end, post_root_idx):
    root = postordered[post_root_idx]
    preordered.append(root)
    if start >= end:
        return None
    in_root_idx = inordered_val2idx[root]
    n_left = in_root_idx - start
    n_right = end - in_root_idx

    if n_left > 0:
        preorder(in_root_idx-n_left, in_root_idx-1, post_root_idx - n_right - 1)
    if n_right > 0:
        preorder(in_root_idx+1, end, post_root_idx - 1)


preorder(0, N-1, N-1)
print(*preordered)