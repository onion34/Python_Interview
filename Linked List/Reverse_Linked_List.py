# Python Interview
# Reverse Linked List / p.219
# parameter head: Node(class)
# return: Node(class)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    @staticmethod
    def solution_by_recursion(head: Node) -> Node:
        def reverse(node: Node, prev: Node = None):
            if not node:
                return prev

            next_node, node.next = node.next, prev
            return reverse(next_node, node)

        return reverse(head)

    @staticmethod
    def solution_by_iteration(head: Node) -> Node:
        cur, prev = head, None

        while cur:
            next_node, cur.next = cur.next, prev
            prev, cur = cur, next_node

        return prev
