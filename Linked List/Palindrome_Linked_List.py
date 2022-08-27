# Python Interview
# Palindrome Linked List / p.201
# parameter head: Node(class)
# return: bool

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


def solution_by_list(head):
    ls = []

    if not head:
        return True

    node = head
    while node is not None:
        ls.append(node.data)
        node = node.next

    while len(ls) > 1:
        if ls.pop(0) != ls.pop():
            return False

    return True


def solution_by_deque(head):
    from collections import deque
    dq = deque()

    if not head:
        return True

    node = head
    while node is not None:
        dq.append(node.data)
        node = node.next

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True


def solution_by_runner(head):
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next = slow, rev
        slow = slow.next

    if fast:
        slow = slow.next

    while rev and rev.data == slow.data:
        slow, rev = slow.next, rev.next

    return not rev
