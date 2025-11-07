def in_order_recursive(node):
    if node is None:
        return
    
    # 1. Go Left (L)
    in_order_recursive(node.left)
    
    # 2. Process Node (N)
    print(node.value)
    
    # 3. Go Right (R)
    in_order_recursive(node.right)