def pre_order_recursive(node):
    if node is None:
        return
    
    # 1. Process Node (N)
    print(node.value)
    
    # 2. Go Left (L)
    pre_order_recursive(node.left)
    
    # 3. Go Right (R)
    pre_order_recursive(node.right)