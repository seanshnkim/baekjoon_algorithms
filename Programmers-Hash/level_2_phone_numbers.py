'''2022-02-25
출처 : 프로그래머스 > 코딩테스트 고득점 kit > 해시 > 전화번호 목록
'''


## 이거는 처음에 해쉬 안 쓰고 구현하려던 것. 무시하자
def solution(phone_book):
    hashTable = {}

    for phone_num in phone_book:
        head = phone_num[0]
        if head in hashTable:
            hashTable[head].append(phone_num)
        else:
            hashTable[head] = [phone_num]

    for key in hashTable:
        if len(hashTable[key]) > 1:
            for phone_num in hashTable[key]:
                head = phone_num[1]
                if key + head in hashTable:
                    hashTable[key + head] = hashTable.pop(key)
                    hashTable[key + head].append(phone_num)

# 해쉬를 쓰지 않고 파이썬의 built-in 기능(substr in phone_book)을 활용
# 정확한 답은 구할 수 있으나, 해쉬를 이용하지 않아 속도가 떨어진다. 시간 초과로 불합격
def solution_mine(phone_book):
    for phone_num in phone_book:
        substr = ''
        for letter in phone_num:
            substr += letter
            if(substr in phone_book && substr != phone_num):
                return False
    return True

# 해쉬 개념을 반영해서 새로 고친 풀이
def solution_hash(phone_book):
    hashTable = {}
    for phone_num in phone_book:
        hashTable[phone_num] = hash(phone_num)

    for phone_num in phone_book:
        substr = ''
        for letter in phone_num:
            substr += letter
            if((substr in hashTable) & (substr != phone_num)):
                return False
    return True

## 다른 사람들의 풀이: 해쉬를 이용한 정석 풀이
def solution_hash(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

