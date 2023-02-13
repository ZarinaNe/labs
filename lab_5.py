#Лаба №5 Cортировка вставками

from random import randint

#создаем случайную последовательность
x = int(input("Введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

for i in range(1, len(nums)):
    for j in range(i,0,-1):
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
        else:
            break
print(*nums)