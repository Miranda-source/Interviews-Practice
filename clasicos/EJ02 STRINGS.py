"""
Write a function called first_non_repeating_character(s) that returns the first character in a string that does not appear more than once.

If every character appears more than once, return None.

Examples:

Input:  "swiss"
Output: "w"
Input:  "aabbcc"
Output: None
Input:  "programming"
Output: "p"

Requirements:

The function should be case-sensitive.
Spaces should be treated as characters

"""


def first_non_repeating_character(s):
    counts = {}

    # Count how many times each character appears
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # Find the first character that appears only once
    for char in s:
        if counts[char] == 1:
            return char

    return None


print(first_non_repeating_character("swiss"))
print(first_non_repeating_character("aabbcc"))
print(first_non_repeating_character("programming"))