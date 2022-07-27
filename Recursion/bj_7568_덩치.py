# 2022-06-26(June 26th, 2022), Sehyun Kim

n = int(input())
wh_info = []

for _ in range(n):
    wh_info.append(list(map(int, input().split())))

rank_list = [1 for i in range(n)]
for k in range(n-1):
    for l in range(k+1, n):
        if wh_info[k][0] < wh_info[l][0] and wh_info[k][1] < wh_info[l][1]:
            rank_list[k] += 1
        elif wh_info[k][0] > wh_info[l][0] and wh_info[k][1] > wh_info[l][1]:
            rank_list[l] += 1

print(*rank_list)