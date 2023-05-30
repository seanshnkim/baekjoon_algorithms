import sys
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
  a, b, c, d = list(map(int, input().split()))
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

A.sort()
B.sort()
C.sort()
D.sort()

def func(A, B, C, D):
  X = sorted([a + b for a in A for b in B])
  Y = sorted([c + d for c in C for d in D])

  x = 0
  y = N**2 - 1
  ans = 0
  while True:
    try:
      cur = X[x] + Y[y]
    except:
      break
    if cur > 0:
      y -= 1
    elif cur < 0:
      x += 1
    else:
      cnt_x = x
      cnt_y = y
      while cnt_x < N**2 and X[x] == X[cnt_x]:
        cnt_x += 1
      while cnt_y >= 0 and Y[y] == Y[cnt_y]:
        cnt_y -= 1
      ans += (cnt_x - x) * (y - cnt_y)
      x = cnt_x
      y = cnt_y
      
  return ans

ans = func(A, B, C, D)
print(ans)