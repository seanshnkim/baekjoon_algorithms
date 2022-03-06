
### 잘못된 접근: DFS(recursion 활용)가 아니라 BFS(최단 경로)
def solution_dfs(begin, target, words):
    answer = 0

    if target not in words:
        return 0
    else:
        for word in words:
            # base case에 대해 실수했다.
            if begin == word:
                return 0
            elif isPossibleToConvert(begin, word):
                words.remove(word)
                print(words)
                answer += 1 + solution_dfs(word, target, words)
                # begin과 한 글자만 다른 단어가 words에 여러 개 주어질 경우, 하나만 선택해서 수행할 수 있도록
        return answer

def bfs(begin, target, words, visited):
    count = 0
    stack = [(begin, 0)]
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            return depth

        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a, b in zip(cur, words[i]):
                if a != b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth + 1))

# def solution_bfs(begin, target, words):
#     if target not in words:
#         return 0
#
#     answer = 0
#     visited = [False] * (len(words))
#     count = 0
#     stack = [(begin, 0)]
#
#     while stack:
#         currWord, numSteps = stack.pop()
#         if currWord == target:
#             return numSteps
#
#         for w in range(len(words)):
#             if visited[w] == False:
#                 for




    answer = bfs(begin, target, words, visited)

    return answer


def isPossibleToConvert(strA, strB):
    # strA와 strB의 길이는 같다고 가정
    numDiffLetters = [charA == charB for charA, charB in zip(strA, strB)].count(False)
    if numDiffLetters == 1:
        return True
    else:
        return False

from collections import deque

def solution3(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    visited = [False for i in range(len(words))]
    while q:
        word, numSteps = q.popleft()
        if word == target:
            answer = numSteps
            break
        for i in range(len(words)):
            numDiffLetters = 0
            print(f'{i}th word: {q}')
            print(f'Visited: {visited}\n')
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        numDiffLetters += 1
                if numDiffLetters == 1:
                    if words[i] == target:
                        return numSteps + 1
                    q.append((words[i], numSteps + 1))
                    visited[i] = True
    return answer

def solution4(begin, target, words):
    answer = 0
    queueBFS = deque()
    queueBFS.append((begin, 0))
    visited = [False for i in range(len(words))]
    while queueBFS:
        word, numSteps = queueBFS.popleft()
        if word == target:
            return numSteps
        for i in range(len(words)):
            numDiffLetters = 0
            if not visited[i]:
                if isPossibleToConvert(word, words[i]):
                    queueBFS.append((words[i], numSteps + 1))
                    visited[i] = True
    return answer

beginWord = "hit"
targetWord = "cog"
testWords = ["hot", "dot", "dog", "lot", "log", "cog"]
#print(solution3(beginWord, targetWord, testWords))
print(solution4(beginWord, targetWord, testWords))
