from math import gcd
# this return in else part took  8ms more time but .2MB less memory
"""
def gcdOfStrings(str1: str, str2: str) -> str:
    if str1+str2==str2+str1:
        lenCommonString = gcd(len(str1),len(str2))
        return str1[:lenCommonString]
    else:
        return ''
"""
# this return ''  took  8ms less time but .2MB more  memory
# if str1 + str2 == str2 + str1:
#     lenCommonString = gcd(len(str1), len(str2))
#     return str1[:lenCommonString]
#
# return ''

# alias 2 - 11mns

def gcdOfStrings(self, str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)

    def isGCD(l):
        if len1 % l or len2 % l:
            return False
        n1, n2 = len1 // l, len2 // l
        return str1[:l] * n1 == str1 and str1[:l] * n2 == str2

    for l in range(min(len1, len2), 0, -1):
        if isGCD(l):
            return str1[:l]
    return ""


print(gcdOfStrings("ABCABC","ABC"))
print(gcdOfStrings("ABABAB","ABAB"))
print(gcdOfStrings("LEET","CODE"))
print(gcdOfStrings("ABCDABC","ABC"))
# 1071. Greatest Common Divisor of Strings
#
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""