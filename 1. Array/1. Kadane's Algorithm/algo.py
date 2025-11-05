def kadane(arr):
    # Handle an empty array case
    if not arr:
        return 0
    
    # Initialize with the first element
    max_so_far = arr[0]
    current_max = arr[0]
    
    # Start from the second element
    for num in arr[1:]:
        # Is it better to start a new subarray or extend the old one?
        current_max = max(num, current_max + num)
        
        # Did we find a new overall best?
        max_so_far = max(max_so_far, current_max)
        
    return max_so_far

# Example
my_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"The maximum subarray sum is: {kadane(my_list)}")
# Output: The maximum subarray sum is: 6