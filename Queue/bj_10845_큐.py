'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys

class Queue():
    def __init__(self):
        self.queue = []
        self.begin = 0
        self.end = 0
    
    def empty(self) -> bool:
        if self.begin == self.end:
            return True
        else:
            return False

    def push(self, data: int) -> None:
        self.queue.append(data)
        # self.queue[self.end] = data
        self.end += 1
    
    def pop(self) -> int:
        if self.empty():
            return -1
        pop_val = self.queue[self.begin]
        self.queue[self.begin] = None
        self.begin += 1
        return pop_val
    
    def size(self) -> int:
        return self.end - self.begin
    
    def front(self) -> int:
        if self.empty():
            return -1
        return self.queue[self.begin]

    def back(self) -> int:
        if self.empty():
            return -1
        return self.queue[self.end-1]

test_queue = Queue()
N = int(sys.stdin.readline())

for _ in range(N):
    commands = sys.stdin.readline().split()
    if commands[0] == 'push':
        test_queue.push(int(commands[1]))
    if commands[0] == 'pop':
        print(test_queue.pop())
    if commands[0] == 'size':
        print(test_queue.size())
    if commands[0] == 'empty':
        print(int(test_queue.empty()))
    if commands[0] == 'front':
        print(test_queue.front())
    if commands[0] == 'back':
        print(test_queue.back())