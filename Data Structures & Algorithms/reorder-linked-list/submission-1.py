# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next

        curr2 = slow.next #
        slow.next = None # break
        prev =None

        while curr2:
            nxt = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = nxt
            
        curr1, curr2 = head, prev
        while curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next

            curr1.next = curr2
            curr2.next = nxt1

            curr1 = nxt1
            curr2 = nxt2
        
        



            
