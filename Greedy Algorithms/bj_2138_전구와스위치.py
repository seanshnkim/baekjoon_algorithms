import sys
input = sys.stdin.readline

N = int(input())
start_state_OFF = [int(s) for s in input().rstrip('\n')]
targ_state = [int(s) for s in input().rstrip('\n')]


def invert(curr_state, idx):
    if idx == 0:
        curr_state[0] ^= 1
        curr_state[1] ^= 1
    elif idx == N-1:
        curr_state[-2] ^= 1
        curr_state[-1] ^= 1
    else:
        curr_state[idx-1] ^= 1
        curr_state[idx] ^= 1
        curr_state[idx+1] ^= 1


def is_valid(curr_state):
    return curr_state[-2] == targ_state[-2] and curr_state[-1] == targ_state[-1]


start_state_ON = start_state_OFF.copy()

# switch_0_off 
cnt_if_0_off = 0
prev = start_state_OFF[0]
for i in range(1, N):
    if prev != targ_state[i-1]:
        invert(start_state_OFF, i)
        cnt_if_0_off += 1
    prev = start_state_OFF[i]


cnt_if_0_on = 1
invert(start_state_ON, 0)
prev = start_state_ON[0]
for i in range(1, N):
    if prev != targ_state[i-1]:
        invert(start_state_ON, i)
        cnt_if_0_on += 1
    prev = start_state_ON[i]


if is_valid(start_state_OFF) and is_valid(start_state_ON):
    print(min(cnt_if_0_off, cnt_if_0_on))
elif not is_valid(start_state_OFF) and not is_valid(start_state_ON):
    print(-1)
else:
    if is_valid(start_state_OFF):
        print(cnt_if_0_off)
    else:
        print(cnt_if_0_on)
