# 2022-06-26(June 26th, 2022), Sehyun Kim

def print_asterisk(num):
    printList = []
    if num == 3:
        printList.append("***")
        printList.append("* *")
        printList.append("***")
        return printList
    else:
        for i in range(3):
            temp = print_asterisk(num/3)
            tempLen = len(print_asterisk(num/3))
            return [temp[i] * 3 for i in range(tempLen)] + \
                   [temp[i] + (" " * int(num/3)) + temp[i] for i in range(tempLen)] + \
                   [temp[i] * 3 for i in range(tempLen)]
        
inputInt = int(input())

for line in print_asterisk(inputInt):
    print(line)

# printList = []
# printList.append("***")
# printList.append("* *")
# printList.append("***")

# printList2 = ["---", "- -", "---"]

# print([printList[i] + printList2[i] for i in range(len(printList))])

