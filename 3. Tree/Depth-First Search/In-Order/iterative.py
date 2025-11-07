def in_order_iterative(root):
    stack = []
    current = root
    
    while current is not None or stack:
        # 1. Go Left (L)
        while current is not None:
            stack.append(current)
            current = current.left
            
        # 2. Process Node (N)
        current = stack.pop()
        print(current.value)
        
        # 3. Go Right (R)
        current = current.right

# Approach
def in_order_iterative(root):
    stack = []
    current = root
    
    while current or stack:
        
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(stack.val)
            current = current.right