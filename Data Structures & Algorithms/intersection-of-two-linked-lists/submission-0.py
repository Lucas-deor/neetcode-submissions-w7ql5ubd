# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA, listB = headA, headB

        while listA != listB:
            if listA == None:
                listA = headB
            else: 
                listA = listA.next
            
            if listB == None:
                listB = headA
            else: 
                listB = listB.next

            if listA == listB:
                return listA

        return None