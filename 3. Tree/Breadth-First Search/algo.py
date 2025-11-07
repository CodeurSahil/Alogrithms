def bfs(root):
    if root is None:
        return

    queue = []  # Use a list as a queue
    queue.append(root)  # 1. Start with the root
    
    while queue:
        # 2. Dequeue the front node
        # .pop(0) is a FIFO (queue) operation
        current = queue.pop(0) 
        
        # 3. Process the node
        print(current.value) 
        
        # 4. Enqueue children
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)