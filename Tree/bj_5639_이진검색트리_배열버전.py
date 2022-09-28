import sys
sys.setrecursionlimit(10**6)

preorder_list = []
while True:
    try:
        preorder_list.append(int(sys.stdin.readline()))
    except:
        break

def postorder(root, end):
    if root >= end:
        return None
    root_val = preorder_list[root]
    
    if preorder_list[end - 1] <= root_val:
        postorder(root+1, end)
        print(root_val)
        return None
    idx = 0
    for i in range(root + 1, end):
        if preorder_list[i] > root_val:
            idx = i
            break
    postorder(root + 1, idx)
    postorder(idx, end)
    print(root_val)

postorder(0, len(preorder_list))