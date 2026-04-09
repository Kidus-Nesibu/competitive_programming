class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        

        size = n // k
        extra = n % k
        
        result = []
        curr = head
        
        for i in range(k):
            part_head = curr
            part_size = size + (1 if i < extra else 0)

            for j in range(part_size - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            result.append(part_head)
        
        return result