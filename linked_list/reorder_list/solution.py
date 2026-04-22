# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        head2 = slow.next
        slow.next = None
       
        curr = head2
        prev = None


        while curr:


            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt


        firstHalf = head
        secondHalf = prev
           
        while secondHalf:
            next1 = firstHalf.next
            next2 = secondHalf.next


            firstHalf.next = secondHalf
            secondHalf.next = next1


            firstHalf = next1
            secondHalf = next2
