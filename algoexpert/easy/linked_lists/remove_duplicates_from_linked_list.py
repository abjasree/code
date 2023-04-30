# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    current_node = linkedList
    while current_node is not None:
        next_distinct_node = current_node.next
        while (
            next_distinct_node is not None
            and next_distinct_node.value == current_node.value
        ):
            next_distinct_node = next_distinct_node.next
        current_node.next = next_distinct_node
        current_node = next_distinct_node

    return linkedList
