# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        #create iterating nodes and reference to new head
        temp = node = ListNode()

        #iterate through both lists and add nodes to our new list
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        #append the rest of any remaining list
        node.next = list1 or list2

        #return the original copy we made
        return temp.next
    
