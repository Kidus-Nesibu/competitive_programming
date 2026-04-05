class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)

        before_curr = before
        after_curr = after

        curr = head

        while curr:
            if curr.val < x:
                before_curr.next = curr
                before_curr = before_curr.next
            else:
                after_curr.next = curr
                after_curr = after_curr.next

            curr = curr.next

        after_curr.next = None
        before_curr.next = after.next

        return before.next