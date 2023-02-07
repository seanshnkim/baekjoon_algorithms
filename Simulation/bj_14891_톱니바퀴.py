import sys
input = sys.stdin.readline

# wheels[1] -> 1번 톱니바퀴의 상태
wheels = [[0]*8]

for _ in range(4):
    wheels.append([int(i) for i in input().rstrip('\n')])
    
how_to_rotate = [0]*5
checked = [False]*5
    
#REVIEW - 재귀함수의 output을 혼동 실수!!
def rotate_wheels(wheel_idx, orient):
    how_to_rotate[wheel_idx] = orient
    checked[wheel_idx] = True
    
    #FIXME- 재귀함수의 무한 반복 에러 -> 이런 실수
    
    if wheel_idx-1 >= 1 and checked[wheel_idx-1] == False:
        if wheels[wheel_idx][-2] != wheels[wheel_idx - 1][2]:
            how_to_rotate[wheel_idx-1] = rotate_wheels(wheel_idx-1, (-1)*orient)
    if wheel_idx+1 <= 4 and checked[wheel_idx+1] == False:
        if wheels[wheel_idx][2] != wheels[wheel_idx + 1][-2]:
            how_to_rotate[wheel_idx+1] = rotate_wheels(wheel_idx+1, (-1)*orient)
    
    return orient


def rotate(wheel_idx, orient):
    if orient == -1:
        first = wheels[wheel_idx][0]
        wheels[wheel_idx][0:7] = wheels[wheel_idx][1:]
        wheels[wheel_idx][-1] = first
    elif orient == 1:
        last = wheels[wheel_idx][-1]
        wheels[wheel_idx][1:] = wheels[wheel_idx][0:7]
        wheels[wheel_idx][0] = last


def calc_score():
    sum_score = 0
    for k in range(1,5):
        if wheels[k][0] == 1:
            sum_score += 1<<(k-1)
    return sum_score
    

n_rotate = int(input())
for n in range(n_rotate):
    w, o = map(int, input().split())
    rotate_wheels(w, o)
    for k in range(1,5):
        rotate(k, how_to_rotate[k])
        checked[k] = False
        how_to_rotate[k] = 0

print(calc_score())