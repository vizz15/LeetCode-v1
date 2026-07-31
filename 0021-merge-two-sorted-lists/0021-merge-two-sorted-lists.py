# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1=list1
        c2=list2
        l=[]
        while c1:
            l.append(c1.val)
            c1=c1.next
        while c2:
            l.append(c2.val)
            c2=c2.next
        l=sorted(l)
        dummy=ListNode(0)   
        current=dummy

        for num in l:
            current.next=ListNode(num)
            current=current.next
        return dummy.next     