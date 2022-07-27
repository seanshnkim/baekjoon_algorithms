list3 = [1,3,2]

sortedList = sorted(list3)

print(sortedList)

help(sorted)

from collections import deque

queueExample = deque()

queueExample.append('icn')
queueExample.append('ifk')
queueExample.append('ekf')
queueExample.append('abc')

thisSorted = sorted(queueExample)
print(type(thisSorted))

# 튜플을 원소로 가지는 리스트도 정렬이 가능한가
tupleList = [('INC', 0), ('BES', 2), ('KOR', 1)]
tupleList2 = [('c', 10), ('a', 99), ('b', 23)]
sortedList = sorted(tupleList)
sortedList2 = sorted(tupleList2)
print(sortedList)
print(sortedList2)
