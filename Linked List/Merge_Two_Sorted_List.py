# Python Interview
# Merge Two Sorted List / p.213
# parameter l1: Node(class), l2: Node(class)
# return: Node(class)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(data)


def solution_by_recursion(l1, l2):
    if not l1 or (l2 and l1.data > l2.data):
        l1, l2 = l2, l1

    if l1:
        l1.next = solution_by_recursion(l1.next, l2)

    return l1
