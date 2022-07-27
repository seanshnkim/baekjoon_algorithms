def solution(bridge_length, weight, truck_weights):
    answer = 0
    # [0, 0, 7, 4, 5, 6]
    bridge = [0 for _ in range(bridge_length)] + truck_weights
    while bridge:
        # 앞에서부터 하나씩 제거하면서
        bridge.pop(0)
        # 다리 길이 만큼의 트럭 무게가
        # 다리가 견딜 수 있는 무게보다 큰 경우
        if sum(bridge[:bridge_length]) > weight:
            # 대기
            bridge.insert(bridge_length-1, 0)
        # 반복마다 시간 증가
        answer += 1
    return answer

#############################################################################
def solution2(bridge_length, weight, truck_weights):
    # on_bridge는 queue다.
    on_bridge = []
    count = 0
    # truck_weights 가 비어있는 null case인 경우
    if not truck_weights:
        return 0
    cur_truck = truck_weights.pop(0)
    on_bridge.append(cur_truck)
    bridge_weight = sum(on_bridge)

    while on_bridge:
        while (bridge_weight + cur_truck < weight) & (len(on_bridge) < bridge_length) & truck_weights:
            on_bridge.insert(0, cur_truck)
            bridge_weight += cur_truck
            cur_truck = truck_weights.pop(0)

        tail = on_bridge.pop()
        bridge_weight -= tail
        count += 1

    return count





    answer = 0
    return count