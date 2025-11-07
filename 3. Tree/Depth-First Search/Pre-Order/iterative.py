def pre_order_iterative(root):
    if root is None:
        return
        
    stack = [root]  # Start with the root
    
    while stack:
        # 1. Pop and Process Node (N)
        current = stack.pop()
        print(current.value)
        
        # 2. Push Right (R) - must be pushed first!
        if current.right:
            stack.push(current.right)
            
        # 3. Push Left (L) - pushed last, so popped next
        if current.left:
            stack.push(current.left)

# Another Way
def pre_order_iterative(root):
    if root is None:
        return
        
    stack = []
    curr = root

    while curr or stack:
        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right);

            curr = curr.left;
        else:
            curr = stack.pop();
