'''given two linked lists return the node at which the two lists intersect'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Plan
# iterate through the list and make it doubly linked
# set previous equal to set
# find the node with two items in its previous set
# that would work but is harder than it needs to be
# alternate:
# create a set of all nodes in list a
# iterate through list b, as soon as a node is in the set its the intersect

# O(n^2) time but O(1) memory:
# for each in a
# check if each in b is same as a

# get the length of each list
# len a - len b = steps to move forward in longer list
# itterate through both comparing


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    # create pointers
    curra = headA
    currb = headB
    # set up the lengths
    lena = 0
    lenb = 0
    # walk through list
    while curra is not None or currb is not None:
        if curra:
            lena += 1
            curra = curra.next
        if currb:
            lenb += 1
            currb = currb.next
    # find which is longer, move the curr to equal points
    if lena > lenb:
        long = headA
        short = headB
        move = lena-lenb
    if lenb > lena:
        long = headB
        short = headA
        move = lenb-lena
    if lena == lenb:
        long = lena
        short = lenb
        move = 0
    for _ in range(move):
        long = long.next
    # find the intersection where the two line up.
    while long != short:
        if long.next is None:
            return None
        long = long.next
        short = short.next

    return long
