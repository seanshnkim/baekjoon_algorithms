from collections import deque

class Node(code):
    def __init__(self):
        self.code = code
        self.n_child = 0
        self.root = None
        self.depth = 0


def solution(s1, s2, k):
    len_s = len(s1)
    start_node = Node(k)
    q = deque([start_node])
    leaf_nodes = dict()
    answer = 0

    while q:
        curr = q.popleft()
        curr_idx = []

        for i in range(len_s):
            if s2[i] == curr.code:
                curr_idx.append(i)
                curr.n_child += 1

        for idx in curr_idx:
            next_c = s1[idx]
            child_node = Node(next_c)
            # 객체가 for loop안에서 생성되면 어차피 객체도 변수니까 for loop 종료되면 사라지나?
            child_node.root = curr
            child_node.depth = curr.depth + 1
            q.append(child_node)
        
        # 만약 idx가 없다면 -> 즉 child가 없는 leaf node이다
        if not curr_idx:
            # 만약 같은 code의 노드가 이미 있다면
            if curr.code in leaf_nodes:
                # 깊이가 더 큰 노드로 교체 & 기존 노드는 root_node와 연결 해제
                if curr.depth > leaf_nodes[curr.code]:
                    prev_node_root = (leaf_nodes[curr.code]).root
                    prev_node_root.n_child -= 1

                    leaf_nodes[curr.code] = curr
            else:
                leaf_nodes[curr.code] = curr
    
    # leaf node끼리는 parent-child 관계가 성립하지 않으므로
    while leaf_nodes:
        tmp_ans = [leaf_nodes.keys()]
        tmp_ans.sort()
        answer.extend(tmp_ans)
        next_leaf_nodes = {}
        
        for node in leaf_nodes.values():
            if node.root is not None:
                node.root.n_child -= 1
                if node.root.n_child == 0:
                    next_leaf_nodes[node.root.code] = node.root
        
        # 비효율적인 걸 알지만, leaf_nodes에서 직접 원소 제거하는 건 더 문제가 많아보인다.
        leaf_nodes = next_leaf_nodes

    return answer