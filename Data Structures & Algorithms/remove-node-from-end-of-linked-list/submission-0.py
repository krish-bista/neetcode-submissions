# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        


        length = 0
        # Find length of linklist
        curr = head
        while curr:
            length += 1
            curr = curr.next
        

        idxToRemove = length - n
        if idxToRemove == 0:
            return head.next
        curridx = 0
        curr = head
        while curr:
            if curridx == idxToRemove - 1:
                curr.next = curr.next.next
            curr = curr.next
            curridx+=1
        return head



