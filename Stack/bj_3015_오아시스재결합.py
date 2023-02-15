import sys
input = sys.stdin.readline

N = int(input())
seq = [int(input()) for _ in range(N)]
stack = [0]
cnt = 0
# which_pairs = []

for i in range(1, N):
    if seq[stack[-1]] <= seq[i]:
        same_ones = []
        while stack and seq[stack[-1]] <= seq[i]:
            if stack and seq[stack[-1]] == seq[i]:
                same_ones.append(stack.pop())
                # which_pairs.append((same_ones[-1], i) )
                cnt += 1
            else:
                stack.pop()
                # which_pairs.append((stack.pop(), i) )
                cnt += 1
        if stack:
            # which_pairs.append((stack[-1], i) )
            cnt += 1
        while same_ones:
            stack.append(same_ones.pop())
    else:
        # which_pairs.append((stack[-1], i) )
        cnt += 1
        
    stack.append(i)

print(cnt)