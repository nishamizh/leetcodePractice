def gcdOfStrings(str1: str, str2: str) -> str:
    if len(str1) and len(str2) >0:
        list1=[]
        for i in range(len(str1)):
            subStr=''
            for j in range(len(str2)):
                if(i+j<len(str1)):
                    if str1[i+j] == str2[j]:
                        subStr+=str2[j]
                else:
                    break
            list1.append(subStr) if len(subStr)>0 else None
    return str(min(list1,key=len)) if len(list1)>0 else ''

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