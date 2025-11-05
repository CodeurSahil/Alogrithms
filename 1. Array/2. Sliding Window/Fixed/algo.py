def find_max_sum_subarray(arr, k):
    if not arr or len(arr) < k:
        return 0
        
    # 1. Initialize the first window
    current_sum = sum(arr[0:k])
    max_sum = current_sum
    
    # 2. Start sliding from the k-th element
    for i in range(k, len(arr)):
        
        # 3. The "slide" logic
        # Add the new element entering the window
        # Subtract the old element leaving the window
        current_sum = current_sum + arr[i] - arr[i - k]
        
        # 4. Update the result
        max_sum = max(max_sum, current_sum)
        
    return max_sum

# Example
my_list = [1, 3, -1, -3, 5, 3, 6, 7]
k_size = 3
print(f"The max sum is: {find_max_sum_subarray(my_list, k_size)}")
# Output: The max sum is: 16