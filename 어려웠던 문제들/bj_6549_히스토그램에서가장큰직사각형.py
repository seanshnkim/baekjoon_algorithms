import sys
input = sys.stdin.readline

while True:
    # N, *heights = list(map(int, input().split() ))
    inputs = list(map(int, input().split() ))
    if inputs == [0]:
        break
    N, *heights = inputs
    
    # FIXME - i=0일 때에도 max_area 업데이트는 해주어야 한다.
    # max_area = 0
    max_area = heights[0]
    stack = []
    for i in range(N):
        if i == 0:
            stack.append(i)
            continue
        
        if heights[i] >= heights[i-1]:
            stack.append(i)
            
        else:
            while stack and heights[stack[-1]] > heights[i]:
                curr = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    # stack의 마지막 남은 한 원소였다는 뜻은, 해당 heights[curr]가 0~curr 범위에서 가장 작은 height였다는 뜻이므로
                    # left = 0
                    left = -1
                right = i
                # FIXME - curr이 아니라 heights[curr] -> 이런 실수 반복하면 안된다
                # max_area = max(max_area, curr*(right-left-1))
                max_area = max(max_area, heights[curr]*(right-left-1))
                
            stack.append(i)
    
    right = N
    while stack:
        curr = stack.pop()
        if stack:
            left = stack[-1]
        # 즉 stack의 마지막 하나 남은 원소였다는 건, max_area <- heights[curr] * N 을 해야한다는 뜻
        else:
            #FIXME - left = 0이 아니라
            left = -1
        max_area = max(max_area, heights[curr]*(right-left-1))
    
    print(max_area)
    



