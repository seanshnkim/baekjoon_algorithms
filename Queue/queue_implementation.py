import typing

class Queue():
    def __init__(self):
        self.queue = []
        self.begin = 0
        self.end = 0

    def push(self, data: int) -> None:
        self.queue[self.end] = data
        self.end += 1
    
    def pop(self) -> None:
        self.queue[self.begin] = None
        self.begin += 1
    
    def empty(self) -> bool:
        if self.begin == self.end:
            return True
        else:
            return False
    
    def size(self) -> int:
        return self.end - self.begin

'''
C++    : vector
Java   : ArrayList
Python : List

그러나 위 언어에서 제공하는 기본 자료형으로 pop() 연산을 구현할 때,
만약 list[0](파이썬을 예시로)의 데이터를 실제로 지운다면, O(N) 시간 복잡도가 된다.
0번째 아이템을 삭제한다면 1,2...N-1번째 아이템의 index를 
모두 1만큼 앞당기는 데 O(N)의 시간 복잡도가 걸리기 때문이다.

또한 문제에서 큐를 구현할 때, 큐(배열)의 크기를 미리 결정해주어야 한다.

Queue를 가장 일반적으로 많이 쓰는 문제는 BFS이다.
'''

'''
Deque = double ended queue
1. push_front()
2. push_back()
3. pop_front()
4. pop_back()
5. front()
6. back()
'''