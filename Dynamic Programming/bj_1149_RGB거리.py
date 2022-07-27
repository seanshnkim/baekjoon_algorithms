import sys

nHouse = int(input())
color_tup = ('red', 'green', 'blue')
color_info = []
for _ in range(nHouse):
    cost_tup = map(int, sys.stdin.readline().split())
    color_dict = {}
    for color, cost in zip(color_tup, cost_tup):
        color_dict[color] = cost
    color_info.append(color_dict)

sumCost_list = []
sumCost_list.append([color_info[0]['red'], color_info[0]['green'], color_info[0]['blue']])

for lev in range(nHouse-1):
    # if start is red
    red_green = sumCost_list[lev][0] + color_info[lev+1]['green']
    red_blue = sumCost_list[lev][0] + color_info[lev+1]['blue']
    # if start is green
    green_red = sumCost_list[lev][1] + color_info[lev+1]['red']
    green_blue = sumCost_list[lev][1] + color_info[lev+1]['blue']
    # if start is blue
    blue_red = sumCost_list[lev][2] + color_info[lev+1]['red']
    blue_green = sumCost_list[lev][2] + color_info[lev+1]['green']

    # 원칙: 같은 layer에 대해서 같은 숫자에 도달하면 반드시 비교, 합이 큰 것은 버리고 작은 것만 살린다.
    rCost = min(green_red, blue_red)
    gCost = min(red_green, blue_green)
    bCost = min(red_blue, green_blue)
    sumCost_list.append([rCost, gCost, bCost])

maxSum = min(sumCost_list[-1])
print(maxSum)

