def build_z_array(s):
    """
    Builds the Z-array for a given string s.
    Z[i] = length of the longest substring starting at s[i]
           which is also a prefix of s.
    """
    n = len(s)
    z = [0] * n
    l, r = 0, 0  # [l, r] represents the "Z-box"

    for i in range(1, n):
        # Case 1: i is outside the Z-box,
        # or Case 2a: i is inside and Z[k] is small
        if i <= r:
            k = i - l
            z[i] = min(r - i + 1, z[k])
        
        # Case 1 & 2b: Manually compare to expand
        # (This handles i > r or Z[k] >= r - i + 1)
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
            
        # If we expanded past the old Z-box, update it
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
            
    return z

# --- Example ---
s = "aabaabcaxaabaaba"
z_array = build_z_array(s)
print(f"String: {s}")
print(f"Z-Array: {z_array}")
# Expected: [0, 1, 0, 2, 1, 0, 0, 2, 0, 6, 1, 0, 3, 1, 0, 1]


def z_search(text, pattern):
    """
    Finds all occurrences of 'pattern' in 'text' using the Z-Algorithm.
    """
    if not pattern:
        return []

    # 1. Concatenate
    m = len(pattern)
    combined_string = pattern + "$" + text
    
    # 2. Build Z-Array
    z_array = build_z_array(combined_string)
    
    matches = []
    
    # 3. Scan Z-Array
    for i in range(len(z_array)):
        # 4. Find Match
        if z_array[i] == m:
            # Calculate index in original text
            match_index = i - m - 1
            matches.append(match_index)
            
    return matches

# --- Example ---
text = "The quick brown fox jumps over the lazy dog."
pattern = "the"

# Note: The algorithm is case-sensitive.
# To make it case-insensitive, convert both to lowercase first.
text_lower = text.lower()
pattern_lower = pattern.lower()

matches = z_search(text_lower, pattern_lower)

print(f"\nText: {text}")
print(f"Pattern: {pattern}")
print(f"Found matches at indices: {matches}")
# Expected: [0, 31]