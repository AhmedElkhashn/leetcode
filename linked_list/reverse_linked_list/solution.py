from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currentNode = head
        prevNode = None

        while currentNode:
            nextNode =  currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode

        return prevNode
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None

        return newHead