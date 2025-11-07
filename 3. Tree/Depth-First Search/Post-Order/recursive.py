def post_order_recursive(node):
    if node is None:
        return
    
    # 1. Go Left (L)
    post_order_recursive(node.left)
    
    # 2. Go Right (R)
    post_order_recursive(node.right)
    
    # 3. Process Node (N)
    print(node.value)