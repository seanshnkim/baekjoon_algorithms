import sys

N, max_W = map(int, sys.stdin.readline().split())
max_W += 1

v_w_pairs = {0: 0}
data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
data.sort(reverse=True)

for w, v in data:
    new_v_w_pairs = {}
    for v_bag, w_bag in v_w_pairs.items():
        new_v = v + v_bag
        new_w = w + w_bag
        if new_v in v_w_pairs and new_w < v_w_pairs[new_v]:
            new_v_w_pairs[new_v] = new_w
        elif new_v not in v_w_pairs and new_w < max_W:
            new_v_w_pairs[new_v] = new_w

    v_w_pairs.update(new_v_w_pairs)

print(max(v_w_pairs.keys()))