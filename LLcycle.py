'''given a linked list determine if it has a cycle in it'''
''' a cycle is just a graph loop'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    visited = set()
    current = head
    if current:  # have to check for an empty list
        while current not in visited and current.next is not None:
            visited.add(current)
            current = current.next
        if current.next is None:
            return False
        else:
            return True
    else:
        return False
