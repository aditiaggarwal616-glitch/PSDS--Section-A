s = input("Enter the string: ")
left = 0
max_length = 0
characters = set()
for right in range(len(s)):
    # If character is repeated, remove from left
    while s[right] in characters:
        characters.remove(s[left])
        left += 1
    # Add current character
    characters.add(s[right])
    # Find maximum length
    length = right - left + 1
    if length > max_length:
        max_length = length
print("Longest substring length:", max_length)
# abcabcbb