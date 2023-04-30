# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    node = linkedList
    count = 0
    while node is not None:
        count += 1
        node = node.next

    middle_node = linkedList
    for i in range(count // 2):
        middle_node = middle_node.next
    return middle_node


def middleNode(linkedList):
    # Write your code here.
    slow = linkedList
    fast = linkedList
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
