# 2022-06-25(June 25th, 2022), Sehyun Kim

def print_hanoi(numFloor, start, end):
    if numFloor == 1:
        print(start, end)
    else:
        middle = 1
        if (start == 1 and end == 2) or (start == 2 and end == 1):
            middle = 3
        elif (start == 1 and end == 3) or (start == 3 and end == 1):
            middle = 2

        print_hanoi(numFloor - 1, start, middle)
        print(start, end)
        print_hanoi(numFloor - 1, middle, end)


if __name__ == '__main__':
    numFloor = int(input())

    print(2 ** numFloor - 1)
    print_hanoi(numFloor, 1, 3)