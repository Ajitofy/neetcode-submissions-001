# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head=dummy
        head1=list1
        head2=list2
        while head1 or head2:
            if not head1:
                dummy.next=head2
                break
            if not head2:
                dummy.next=head1
                break

            if head1.val<head2.val:
                dummy.next=ListNode(head1.val)
                head1=head1.next
                dummy=dummy.next
            elif head1.val>head2.val:
                dummy.next=ListNode(head2.val)
                head2=head2.next
                dummy=dummy.next
            else:
                dummy.next=ListNode(head1.val)
                dummy=dummy.next
                dummy.next=ListNode(head2.val)
                dummy=dummy.next

                head1=head1.next
                head2=head2.next
        curr=head.next
        head.next=None
        return curr
