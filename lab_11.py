#Лаба №11 быстрая сортировка

import random

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        elem = nums[0]
        less = [i for i in nums if i < elem]
        equal = [i for i in nums if i == elem]
        bigger = [i for i in nums if i > elem]
        return quick_sort(less) + equal + quick_sort(bigger)

x = int(input("введите размер списка \n"))
nums = [random.randint(1, 100) for i in range(0, x)]
print(*nums)

nums = quick_sort(nums)

print(*nums)