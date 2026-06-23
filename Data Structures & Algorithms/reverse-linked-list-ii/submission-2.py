class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for _ in range(left-1):
            prev=prev.next
        curr=prev.next
        rev_prev=None
        for _ in range(right-left+1):
            temp=curr.next
            curr.next=rev_prev
            rev_prev=curr
            curr=temp
        tail=prev.next
        prev.next=rev_prev
        tail.next=curr
        return dummy.next