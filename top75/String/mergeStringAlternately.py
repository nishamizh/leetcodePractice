from itertools import zip_longest


def mergeAlternately(word1: str, word2: str) -> str:
    mergedStr = ''
    for i in range(len(word1) if len(word1) > len(word2) else len(word2)):
        if (i < len(word1)):
            mergedStr += word1[i]
        if (i < len(word2)):
            mergedStr += word2[i]

    return str(mergedStr)


print(mergeAlternately(word1="abcdf", word2="pqr"))

# alias 2
def mergeAlternately(word1: str, word2: str) -> str:
    return ''.join([a + b for a, b in zip_longest(word1, word2, fillvalue='')])

# alias 3
word1="abcdf"
word2="pqr"
result = ""
for i in range(0, min(len(word1), len(word2))):
    result += word1[i]
    result += word2[i]
    if len(word1) > len(word2):
        result += word1[len(word2):]
    elif len(word1) < len(word2):
        result += word2[len(word1):]
print(result)

#alias 3:
# 1768. Merge Strings Alternately
# you are given two strings word1 and word2.Merge the strings by adding letters in alternating order, starting
# with word1.If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"