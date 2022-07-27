def solution_stock(prices):
    counts = [0 for i in range(len(prices))]
    # indices = [i for i in range(len(prices))]
    for ind, price in enumerate(prices):
        for count, checkpoint in enumerate(prices[ind + 1:]):
            if checkpoint < price:
                counts[ind] = count + 1
                break
            else:
                counts[ind] += 1
    return counts

def solution_others(prices):
    answer =[0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer

