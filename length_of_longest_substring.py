
def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0  # Left pointer of the sliding window

    for end in range(len(s)):
        print(s[end])
        if s[end] in char_index_map:
            # Update the start pointer to avoid repeat
            start = max(start, char_index_map[s[end]] + 1)
        
        # Update the last seen index of the character
        char_index_map[s[end]] = end
        
        # Calculate the length of the current substring
        max_length = max(max_length, end - start + 1)
        print(char_index_map)
        print(max_length)
        print(start)
        print("-------------")
    print(char_index_map)
    return max_length

# Example usage
if __name__ == "__main__":
    input_string = "abcabcbb"
    result = length_of_longest_substring(input_string)
    print(result)  # Output: 3
