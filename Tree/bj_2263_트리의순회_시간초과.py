import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
inordered = list(map(int, (sys.stdin.readline().split())))
postordered = list(map(int, (sys.stdin.readline().split())))

preordered = []

def preorder(start, end, root):
    preordered.append(root)
    if start >= end:
        return None
    in_root_idx = inordered.index(root)
    post_root_idx = postordered.index(root)
    n_left = in_root_idx - start
    n_right = end - in_root_idx

    if n_left > 0:
        left_root = postordered[post_root_idx - n_right - 1]
        preorder(in_root_idx-n_left, in_root_idx-1, left_root)
    if n_right > 0:
        right_root = postordered[post_root_idx - 1]
        preorder(in_root_idx+1, end, right_root)

preorder(0, N-1, postordered[-1])
print(*preordered)