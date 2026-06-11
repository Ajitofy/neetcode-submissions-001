# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        prev = None
        curr = head

        while curr:
            curr = curr.next
            count +=1
        curr = head #re-assign
        for _ in range(count-n):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            curr = curr.next
            head.next =None
            head = curr

        return head


