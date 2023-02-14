import sys
input = sys.stdin.readline

n_people, n_trains = map(int, input().split())
times = list(map(int, input().split()))


# def get_cnts(curr_t):
#     # 운행시간 time = t초 
#     # 즉 curr_t = 8이라면, t=7까지 탑승한 인원만 포함하는 것.
#     return sum( ( curr_t // t) for t in times )
def get_cnts(curr_t):
    # t=curr_t까지 열차에 탑승한 (아직 안 내려도 상관없음) 인원들 수를 구한다.
    cnt = 0
    for t in times:
        if curr_t % t > 0:
            cnt += (curr_t // t) + 1
        else:
            cnt += (curr_t // t)
    return cnt


def get_order(curr_t, curr_cnt, targ_cnt):
    for i in range(n_trains):
        if curr_t % times[i] == 0:
            curr_cnt += 1
        if curr_cnt == targ_cnt:
            # 열차의 순서를 리턴
            return i+1
            # return curr_t + 1
    
    # 여전히 사람을 다 못 태웠다면
    if curr_cnt < targ_cnt:
        return get_order(curr_t+1, get_cnts(curr_t+1), targ_cnt)
    

left = min(times) * (n_people // n_trains)
right = max(times) * (n_people // n_trains)
#FIXME - 반례: N = 3인데, M = 1일 경우?
# answer = n_people 
if n_trains == 1:
    print(1)
#FIXME - elif n_people -> 같을 때도
# elif n_people < n_trains:
elif n_people <= n_trains:
    print(n_people)
else:
    answer = 0
    while left <= right:
        # mid = 가능한 운행시간 -> 우선 이분 탐색(매개변수 탐색)으로 운행시간을 찾고,
        # 해당 운행시간 안에 태울 수 있는 사람 수(cnt)가 n_people보다 크거나 같다면 운행시간(mid)을 줄이고,
        # 해당 운행시간 안에 태울 수 있는 사람 수(cnt)가 n_people-M보다 작다면 운행시간을 늘린다.
        # cnt가 n_people-M 이상 n_people 이하이면 해당 운행시간 안에 답을 구한다.
        # 그래서 찾고자 하는 운행시간은 cnt 값이 n_people-M 이상 n_people 이하인 운행시간
        mid = (left+right) // 2
        
        curr_n_people = get_cnts(mid)
        # if curr_n_people >= n_people:
        if curr_n_people >= n_people:
            right = mid-1
        elif curr_n_people < n_people - n_trains:
            left = mid+1
        else:
            answer = get_order(mid, curr_n_people, n_people)
            break
    print(answer)

'''
반례:
3 1
4
output: 3
answer: 1

반례 2:
2000000000 1
30
output: 0
answer: 1
'''