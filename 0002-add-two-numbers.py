# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = cur = ListNode(0)

        carry = 0
        while l1 is not None or l2 is not None:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            
            value = l1_val + l2_val + carry
            if value < 10:
                carry = 0
            else:
                carry = 1
                value -= 10
                
            cur.next = ListNode(value)
            cur = cur.next
            
            if l1 is not None:
                l1 = l1.next
                
            if l2 is not None:
                l2 = l2.next
                
        if carry == 1:
            cur.next = ListNode(1)

        return head.next
