def build_prefix_sum(arr):
    N = len(arr)
    prefix = [0] * (N + 1)  # Create padded array
    for i in range(N):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

def query(prefix, left, right):
    # arr[left...right] (inclusive)
    return prefix[right + 1] - prefix[left]

# Example
arr = [10, 2, 8, 5, 3]
prefix_array = build_prefix_sum(arr)

print(f"Prefix Sum Array: {prefix_array}")
print(f"Sum of [2, 8, 5] is: {query(prefix_array, 1, 3)}")
print(f"Sum of [10, 2, 8] is: {query(prefix_array, 0, 2)}")

# Output:
# Prefix Sum Array: [0, 10, 12, 20, 25, 28]
# Sum of [2, 8, 5] is: 15
# Sum of [10, 2, 8] is: 20