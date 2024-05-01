def reverseVowels(s: str) -> str:
    lsit1 = []
    for i in s:
        if i in 'aeiouAEIOU':
            lsit1.append(i)

    characters = list(s)

    for j in range(len(s)):
        if characters[j] in 'aeiouAEIOU':
            a = lsit1.pop()
            characters[j] = a

    return ''.join(characters)

print(reverseVowels('hello'))
print(reverseVowels('leetcode'))
print(reverseVowels('aA'))

# 345. Reverse Vowels of a String
#
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
# Example 1:
# Input: s = "hello"
# Output: "holle"
#
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
#
# Example 3:
# Input: s = 'aA'
# Output: Aa
#
# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.