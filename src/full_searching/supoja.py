# https://programmers.co.kr/learn/courses/30/lessons/42840
class Node:
    def __init__(self, left=None, value=None, right=None):
        self.left = left
        self.value = value
        self.right = right

    def __str__(self):
        return '-{}-'.format(self.value)


class CircularLinkedList:
    def __init__(self, values=None):
        self.head = Node()
        self.tail = Node()
        head = self.head
        tail = self.tail
        head.left = tail
        head.right = tail
        tail.left = head
        tail.right = head
        if values is not None:
            self.add_all(values)

    def is_empty(self):
        return self.head.right == self.tail

    def __str__(self):
        node = self.head.right
        string = ''
        if self.is_empty(): return ''
        while node != self.tail:
            string += str(node)
            node = node.right
        return string

    def add(self, value):
        tail = self.tail
        last_inserted_node = tail.left
        new_node = Node(last_inserted_node, value, tail)
        last_inserted_node.right = new_node
        tail.left = new_node

    def add_all(self, values):
        for value in values:
            self.add(value)

    def get_first_node(self):
        right = self.head.right
        if right == self.tail:
            return None
        else:
            return right

    def get_circular_next(self, node):
        right = node.right
        if right == self.tail:
            return self.head.right
        else:
            return right


def solution(answers):
    result = []
    patt1 = CircularLinkedList([1, 2, 3, 4, 5])
    patt2 = CircularLinkedList([2, 1, 2, 3, 2, 4, 2, 5])
    patt3 = CircularLinkedList([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    # print(patt1, patt2, patt3)
    p1 = patt1.get_first_node()
    p2 = patt2.get_first_node()
    p3 = patt3.get_first_node()
    cnts = {1: 0, 2: 0, 3: 0}
    for answer in answers:
        if answer == p1.value: cnts[1] += 1
        if answer == p2.value: cnts[2] += 1
        if answer == p3.value: cnts[3] += 1
        p1 = patt1.get_circular_next(p1)
        p2 = patt2.get_circular_next(p2)
        p3 = patt3.get_circular_next(p3)
    # print(cnts)
    max_cnt = max(cnts.values())
    for (key, value) in cnts.items():
        if value == max_cnt:
            result.append(key)
    return result