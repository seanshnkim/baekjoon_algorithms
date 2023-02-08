# 백준 2263 트리의 순회

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_pos = [0]*(N+1)
for i in range(N):
    # in order vertex position
    in_pos[in_order[i]] = i

def solve(in_start, in_end, p_start, p_end):
    # if left ==  0, then in_start > in_end(in_start+left-1)
    # if right == 0, then in_start(in_end-right+1) > in_end
    if in_start > in_end:
        return

    root = post_order[p_end] # 후위순회에서 부모노드 찾기
    print(root, end=" ")
    left = in_pos[root] - in_start # 왼쪽인자 갯수
    right = in_end - in_pos[root] # 오른쪽인자 갯수

    solve(in_start, in_start+left-1, p_start, p_start+left-1) # 왼쪽 노드
    solve(in_end-right+1, in_end, p_end-right, p_end-1) # 오른쪽 노드

# 반례 모음: https://bingorithm.tistory.com/5

'''
1. post-order에서 가장 마지막 아이템은 루트이다.
2. in-order에서 정점의 index를 매번 O(N)의 시간복잡도로 찾으면 시간 초과
따라서 인덱스 정보를 배열로 저장해놓고 가져다 쓰는 게 효율적이다.
'''

solve(0, N-1, 0, N-1)