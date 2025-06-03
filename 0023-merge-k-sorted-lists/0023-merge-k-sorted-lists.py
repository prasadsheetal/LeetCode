class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Attach remaining nodes if any list still has nodes
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merged_head = None
        for linked_list in lists:
            merged_head = self.mergeTwoLists(merged_head, linked_list)

        return merged_head