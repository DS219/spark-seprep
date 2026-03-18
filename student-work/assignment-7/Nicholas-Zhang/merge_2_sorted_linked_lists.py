# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # create iterating nodes and reference to new head
        temp = node = ListNode()

        # iterate through both lists and add nodes to our new list
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # append the rest of any remaining list
        node.next = list1 or list2

        # return the original copy we made
        return temp.next

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Test the mergeTwoLists function
if __name__ == "__main__":
    # Create two sorted linked lists
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    # Merge the lists
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    # Print the merged linked list
    print_linked_list(merged_list)
