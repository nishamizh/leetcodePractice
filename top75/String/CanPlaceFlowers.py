from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    counter = 0
    j = 0
    flag = False
    if (n > 0):
        while j < (len(flowerbed)):
            if (flowerbed[j] == 0):
                if (len(flowerbed) > 1):
                    if (j == 0 and flowerbed[j + 1] == 0) or ((j == len(flowerbed) - 1) and flowerbed[j - 1] == 0):
                        counter += 1
                        flag = True
                    elif (flowerbed[j - 1] == 0) and (flowerbed[j + 1] == 0):
                        counter += 1
                        flag = True
                else:
                    counter += 1

            if counter == n:
                return True

            if flag:
                j+=2
            else:
                j+=1
    if(n==0):
        return True

    return False


print('T --> ',canPlaceFlowers([0],0))
print('T --> ',canPlaceFlowers([1,0,0,0,0,0,1],2))
print('F --> ',canPlaceFlowers([1,0,0,0,0,1],2))
print('T --> ',canPlaceFlowers([0,1,0,1,0,1,0,0],1)) # T
print('T --> ',canPlaceFlowers([0,0,0,0,0,1,0,0],0)) # T
print('T --> ',canPlaceFlowers([0,0,0,0,0,1,0,0],1)) # T
print('T --> ',canPlaceFlowers([0],1)) # T
print('T --> ',canPlaceFlowers([1,0,0,0,1],1)) # T
print('F --> ',canPlaceFlowers([1,0,0,0,1],2)) # F
print('T --> ',canPlaceFlowers([0,0,1,0,1],1)) # T
#
    #
    # 605. Can Place Flowers
    #
    # You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
    #
    # Given an integer array flowerbed containing
    # 0's and 1'
    # s, where
    # 0
    # means
    # empty and 1
    # means
    # not empty, and an
    # integer
    # n,
    # return true if n
    # new
    # flowers
    # can
    # be
    # planted in the
    # flowerbed
    # without
    # violating
    # the
    # no - adjacent - flowers
    # rule and false
    # otherwise.
    #
    # Example 1:
    # Input: flowerbed = [1, 0, 0, 0, 1], n = 1
    # Output: true
    #
    # Example 2:
    #
    # Input: flowerbed = [1, 0, 0, 0, 1], n = 2
    # Output: false
    #
    # Constraints:
    # 1 <= flowerbed.length <= 2 * 104
    # flowerbed[i] is 0 or 1.
    # There are no two adjacent flowers in flowerbed.
    # 0 <= n <= flowerbed.length