# 참고: https://velog.io/@woga1999/파이썬으로-구현하는-링크드-리스트
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_head = self.head
        while curr_head:
            print(curr_head.data, end=' ')
            curr_head = curr_head.next
    
    # get node with its index
    def get_node(self, index):
        if self.head is None:
            print("Linked list is empty")
            return None
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
            if node is None:
                print("Index out of range")
                return None
        return node

    # https://leetcode.com/problems/linked-list-cycle/
    # push data to the front of the list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # append index version
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    # insert with previous node instance
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # delete node with its value(key)
    def delete_node(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def delete_node_at_position(self, position):
        if self.head == None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position -1):
            temp = temp.next
            if temp is None:
                break
        if temp is None or temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def get_count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # Linked list starts searching from head. This is why linked lists have O(n) search time.
    # Linked lists have a performance advantage over normal lists when implementing a queue.
    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False