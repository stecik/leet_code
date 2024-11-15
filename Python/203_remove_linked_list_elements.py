from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return None

    while head.next and head.val == val:
        head = head.next

    if head.val == val:
        return None

    current = head
    next = current.next
    while next:
        if next.val == val:
            next = next.next
        else:
            current.next = next
            current = next
            next = next.next
    current.next = None
    return head


def print_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


def create_list(values):
    head = ListNode()
    current = head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return head.next


head = create_list([1, 2, 6, 3, 4, 5, 6])
print_list(head)
head = removeElements(head, 6)
print_list(head)
print()

head = create_list([1, 1, 1, 1, 1, 1, 1])
print_list(head)
head = removeElements(head, 1)
print_list(head)
