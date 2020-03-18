# https://programmers.co.kr/learn/courses/30/lessons/42840
class Node:
    def __init__(self, left=None,value=None,right=None):
        self.left = left
        self.value = value
        self.right = right
    def __str__(self):
        return '-{}-'.format(self.value)    
class CircularLinkedList:
    def __init__(self, values = None):
        self.head = Node()
        self.tail = Node()
        head = self.head
        tail = self.tail
        head.left = tail
        head.right = tail
        tail.left = head
        tail.right = head
        if values != None: self.addAll(values)
    def isEmpty(self):
        return self.head.right == self.tail
    def __str__(self):
        node = self.head.right
        string = ''
        if self.isEmpty(): return ''
        while node != self.tail:
            string +=str(node)
            node = node.right
        return string
    def add(self, value):
        head = self.head
        tail = self.tail
        lastInsertedNode = tail.left
        newNode = Node(lastInsertedNode, value, tail)
        lastInsertedNode.right = newNode
        tail.left = newNode
    def addAll(self, values):
        for value in values:
            self.add(value)
    def getFirstNode(self):
        right = self.head.right
        if right==self.tail: return None
        else : return right
    def getCircularNext(self,node):
        right = node.right
        if right == self.tail:
            return self.head.right
        else: return right
def solution(answers):
    result = []
    patt1 = CircularLinkedList([1,2,3,4,5])
    patt2 = CircularLinkedList([2,1,2,3,2,4,2,5])
    patt3 = CircularLinkedList([3,3,1,1,2,2,4,4,5,5])
    # print(patt1, patt2, patt3)
    p1 = patt1.getFirstNode()
    p2 = patt2.getFirstNode()
    p3 = patt3.getFirstNode()
    cnts={}
    cnts[1] = 0
    cnts[2] = 0
    cnts[3] = 0
    for answer in answers:
        if answer == p1.value: cnts[1]+=1
        if answer == p2.value: cnts[2]+=1
        if answer == p3.value: cnts[3]+=1
        p1 = patt1.getCircularNext(p1)
        p2 = patt2.getCircularNext(p2)
        p3 = patt3.getCircularNext(p3)
    # print(cnts)
    maxCnt = max(cnts.values())
    for (key, value) in cnts.items():
        if value == maxCnt: result.append(key)
    return result