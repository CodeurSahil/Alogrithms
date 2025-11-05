import math

def find_min_subarray_length(arr, S):
    left = 0
    current_sum = 0
    min_length = math.inf
    
    # 'right' loop handles expansion
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # 'while' loop handles recording and shrinking
        # This is the key part of the variable window
        while current_sum >= S:
            # 1. Record the answer
            current_length = (right - left) + 1
            min_length = min(min_length, current_length)
            
            # 2. Shrink the window
            current_sum -= arr[left]
            left += 1
            
    # If no window was found
    if min_length == math.inf:
        return 0
    else:
        return min_length

# Example
my_list = [2, 3, 1, 2, 4, 3]
S = 7
print(f"Min length is: {find_min_subarray_length(my_list, S)}")
# Output: Min length is: 3