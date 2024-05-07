# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, curr = None, head
        curr.val *= 2
        if curr.val > 9:
            curr.val %= 10
            prev = ListNode(1, curr)
            head = prev
        prev = curr
        curr = curr.next
        while curr:
            curr.val *= 2
            if curr.val > 9:
                curr.val %= 10
                prev.val += 1
            prev = curr
            curr = curr.next
        return head
        