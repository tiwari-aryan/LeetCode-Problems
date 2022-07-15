class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = ListNode(0)
        sum_next = sum_list
        next_num = 0
        while l1 or l2 or next_num:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            if val_1 + val_2 + next_num >= 10:
                sum_next.next = ListNode(val_1 + val_2 + next_num - 10)
                next_num = 1
            else:
                sum_next.next = ListNode(val_1 + val_2 + next_num)
                next_num = 0

            sum_next = sum_next.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sum_list.next
