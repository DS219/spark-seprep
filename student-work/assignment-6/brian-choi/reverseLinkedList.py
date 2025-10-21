from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            nextNode = cur.next      
            cur.next = prev          
            prev = cur               
            cur = nextNode           

        return prev

def printList(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    sol = Solution()

    # Test 1 = [1, 2, 3, 4, 5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print("Input: [1, 2, 3, 4, 5]")
    print("Reversed:", printList(sol.reverseList(head)))
    print()

    # Test 2 = [1, 2]
    head = ListNode(1)
    head.next = ListNode(2)
    print("Input: [1, 2]")
    print("Reversed:", printList(sol.reverseList(head)))
    print()

    # Test 3 = []
    head = None
    print("Input: []")
    print("Reversed:", printList(sol.reverseList(head)))