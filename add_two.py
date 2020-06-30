'''You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''


# plan:
# go through each linked list, extracting the digits into a string
# convert the strings to integers
# add the ints
# deconstruct the outcome back to linked list

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # initialize empty strings
    s1 = ''
    s2 = ''
    # add the current number to begining of the string
    while l1 is not None or l2 is not None:
        if l1:
            s1 = l1.val + s1
        if l2:
            s2 = l2.val + s2
        l1 = l1.next
        l2 = l2.next
    # swap to numbers
    i1 = int(s1)
    i2 = int(s2)
    # do the math and switch back to string
    out = str(i1 + i2)
    # initialize the output list while starting the reversal
    list = ListNode(out[0], next=None)
    # itterate through the rest of the string converting to ll
    for c in out[1:]:
        list = ListNode(c, next=list)
    return list
