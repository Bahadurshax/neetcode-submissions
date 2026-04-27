# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(first, second):
    if not first:
        return second
    if not second:
        return first
    
    if first.val < second.val:
        first.next = merge(first.next, second)
        return first
    else:
        second.next = merge(first, second.next)
        return second

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return merge(list1, list2)
        