def post_order_iterative(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []  # This will hold the post-order result
    
    while stack1:
        # Pop from stack1 and add to stack2
        current = stack1.pop()
        stack2.append(current)
        
        # Push left child first (so right is processed next)
        if current.left:
            stack1.push(current.left)
        # Push right child last (so left is processed next)
        if current.right:
            stack1.push(current.right)
            
    # Now, stack2 has the nodes in L-R-N order.
    # Pop and process them.
    while stack2:
        node = stack2.pop()
        print(node.value)


# Another Way
def post_order_iterative(root):
    if root is None:
        return

    stack = [root]
    visit = [False]
    
    while stack:
        curr, visited = stack.pop(), visit.pop()
       
        if curr:
            if visited:
                print(curr.val)
            else:
                stack.append(curr)
                visit.append(True)

                stack.append(curr.right)
                visit.append(False)

                stack.append(curr.left)
                visit.append(False)