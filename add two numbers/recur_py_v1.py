# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My code starts here v
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        l3 = ListNode(val=l1.val + l2.val + carry)

        if l3.val >= 10:
            l3.val -= 10
            carry = 1
        else:
            carry = 0

        if l1.next == None and l2.next != None:
            l3.next = self.addTwoNumbers(ListNode(), l2.next, carry)
        elif l2.next == None and l1.next != None:
            l3.next = self.addTwoNumbers(l1.next, ListNode(), carry)

        if carry == 1 and l1.next == None and l2.next == None and l1.val + l2.val + carry >= 10:
            l3.next = ListNode(val=1)

        if l1.next != None and l2.next != None:
            l3.next = self.addTwoNumbers(l1.next, l2.next, carry)

        carry = 0

        return l3

