# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My code starts here v
class Solution:
    def add_two_numbers(self, l1: ListNode | None, l2: ListNode | None, carry=0) -> ListNode:
        l3 = ListNode(val = l1.val + l2.val + carry)

        if l3.val >= 10:
            l3.val -= 10
            carry = 1
        else: carry = 0

        if l1.next is None and l2.next is not None:
            l3.next = self.add_two_numbers(ListNode(), l2.next, carry)
        elif l2.next is None and l1.next is not None:
            l3.next = self.add_two_numbers(l1.next, ListNode(), carry)

        if carry == 1 and l1.next is None and l2.next is None and l1.val + l2.val + carry >= 10:
            l3.next = ListNode(val=1)

        if l1.next is not None and l2.next is not None:
            l3.next = self.add_two_numbers(l1.next, l2.next, carry)

        return l3
