def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Find the shortest string in the list
    shortest_str = min(strs, key=len)

    # Iterate over the characters of the shortest string
    for i, char in enumerate(shortest_str):
        # Check if the character is the same in all strings
        for string in strs:
            if string[i] != char:
                return shortest_str[:i]
    
    # If all characters are the same in all strings, return the shortest string
    return shortest_str
    
strs = ["flower", "flow", "flight"]
result = longestCommonPrefix(strs)
print(result)  # Output: "fl"
