# Rohit Mandapati

Hi, my name is Rohit Mandapati and I am a freshman at BU. My favorite language is Java because it's level of complexity is a great launching ground to learn other languages, and mastering it lets you become fluent in many principles that are crucial to learning to program.

### Example Code Snippet
```
public class Test {

    private class Node {
        int data;
        Node next;

        Node(int new_data) {
            data = new_data;
            next = null;
        }
    }

    static Node reverseList(Node head) {
        Node curr = head, prev = null, next;
        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}
```

### Explanation

This code snippet reverses a linked list data structure.