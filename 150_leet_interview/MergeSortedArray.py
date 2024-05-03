from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = 0
    j = 0
    highest_val=nums1[m-1] if m!=1 else nums1[0]
    if (m == 0):
        nums1[0:] = nums2
    if(m>0 and n>0):
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i] >= nums2[j]):
                j_val = nums2[j]
                nums1[i+1:]=nums1[i:len(nums1)-1]
                nums1[i]=j_val
                i+=1
                j+=1
            elif(nums1[i] < nums2[j]):
                if(nums1[i]==highest_val and nums1[i]!=nums1[i+1]):
                    nums1[i+1:]=nums2[j:]
                    break
                else:
                    i+=1


    print(nums1)
merge(nums1 = [-1,0,1,1,0,0,0,0,0],m =4,nums2 = [-1,0,2,2,3],n = 5)
merge(nums1 = [2,3,0,0,0],m =2,nums2 = [1,2,5],n = 3)
merge(nums1 = [1,2,3,0,0,0],m = 3,nums2 = [2,5,6],n = 3)
merge(nums1 = [1],m = 1,nums2 = [],n = 0)
merge(nums1 = [0],m = 0,nums2 = [1],n = 1)
merge(nums1 = [2,0],m = 1,nums2 = [1],n = 1)
merge(nums1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      m = 1,nums2 = [-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48],
      n = 90)
#
# 88. Merge Sorted Array
#
# Hint
# You are given two integer arrays nums1 and nums2, sorted in non - decreasing
# order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be
# stored inside the array nums1.To
# accommodate this, nums1 has
# has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n
#
# Example 1:
# Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
# Output: [1, 2, 2, 3, 5, 6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
#
# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are[] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1.The 0 is only there to ensure the merge result can fit in nums1.
#
# Constraints:
#
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
#
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?