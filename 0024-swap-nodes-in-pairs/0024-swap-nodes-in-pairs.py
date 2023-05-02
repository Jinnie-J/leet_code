# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        node = head
        arr = []

        while node is not None :
            arr.append(node.val)
            node = node.next
        for i in range(1,len(arr),2) :
            arr[i], arr[i-1] = arr[i-1], arr[i]

        prev = None

        while arr:
            node = ListNode(arr.pop())
            node.next = prev
            prev = node

        return node