head = map();

slow, fast = head, head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
