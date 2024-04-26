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

# alias 2

def gcdOfStrings(str1: str, str2: str) -> str:
    if len(str2) > len(str1):
        str1,st2 = str2,str1

    if str2==str1: return str1

    if str1[:len(str2)]!=str2:  return ''

    return gcdOfStrings(str1[len(str2):],str2)


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