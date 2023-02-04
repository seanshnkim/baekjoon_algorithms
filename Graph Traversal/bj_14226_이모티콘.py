import sys
from collections import deque

MAX_N = 1001
N = int(sys.stdin.readline())

# visited[k] = k개의 이모티콘을 (화면에) 만들었을 때 [cnt, n_clipboard] 쌍(cnt는 시간, n_clipboard는 클립보드에 저장된 단어 개수)
visited = [[-1, 0] for _ in range(MAX_N)]
visited[1] = [1, 0]

def bfs(q):
    while q:
        curr = q.popleft()
        
        # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기하거나(2번 방법) 
        # 현재 화면의 이모티콘에서 1개를 삭제(3번)
        for next in [curr+visited[curr][1], curr-1]:
            if 0 <= next < MAX_N:
                if visited[next][0] == -1:
                    visited[next][0] = visited[curr][0] + 1
                    # 현재 클립보드에 저장된 이모티콘의 개수는 그대로 유지한다.
                    visited[next][1] = visited[curr][1]
                    q.append(next)
                
                elif visited[next][0] > visited[curr][0]+1:
                    # 이걸 언제 해야할지 모르겠다.
                    # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
                    visited[curr][0] += 1
                    visited[curr][1] = curr * 2
                    q.append(next)

                
        for next in next_steps:
            if 0 <= next < MAX_N:
                if visited[next][0] == -1:
                    # 시간이 1초 걸리고
                    visited[next][0] = visited[curr][0] + 1
                    # 클립
                    visited[next][1] = visited[curr][1]
                    q.append(next)
                    
                    if next == N:
                        return visited[next][0]
                else:
                    # save current emoticons on screen to clipboard
                    # 현재 이모티콘(curr 개)을 클립보드에 저장
                    visited[curr][1] = curr
                    visited[curr][0] += 1
            


q = deque([1])
