# Practice basic Coding with me - Nisha
# This is purely for first timers

# Q1.  https://leetcode.com/problems/two-sum/ - full question description at the end of all problems

class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}

        for i,num in enumerate(nums):
            x = target-num

            if(x in hm):
                return(hm[x],i)
            
            hm[num]=i

    nums = [2,7,11,15]
    target = 9
    result = twoSum(nums,target)
    print(result)

# Q2   https://leetcode.com/problems/valid-parentheses/description/
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {")":"(", "}":"{", "]":"["}
        st = []

        for c in s:
            if c in '{[(':
                st.append(c)
            else:
                if not st or st.pop()!=pairs[c]:
                    return False
        
        return not st

    s = "(){}[]"
    result1 = isValid(s)
    print(result1)


    def search(nums, target):
        left,right = 0,len(nums)-1

        while left<=right:
            mid = (left+right)//2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1


        return -1    


    nums = [-1,0,3,5,9,12]
    target = 9
    print(search(nums, target))
    
    


""" 
Q1 - two-sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists."""

# Q2

"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
# Q3
"""
704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""