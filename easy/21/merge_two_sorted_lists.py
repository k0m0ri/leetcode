# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: [ListNode], list2: [ListNode]) -> [ListNode]:
    head = ListNode()
    current = head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        # currentを進める
        current = current.next

    # 残っているのNodeをマージする
    current.next = list1 or list2
    # 先頭のNodeを返す
    return head.next


# test
num1 = ListNode(1)
num2 = ListNode(2)
num1.next = num2
num3 = ListNode(4)
num2.next = num3

num4 = ListNode(1)
num5 = ListNode(3)
num4.next = num5
num6 = ListNode(4)
num5.next = num6

head = mergeTwoLists(num1, num4)
while head:
    print(head.val)
    head = head.next
