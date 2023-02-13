#ЛАБА №6 Сортировка посредством выбора

from random import randint

#создаем случайную последовательность
x = int(input("Введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

for i in range(len(nums)-1):
    min_ind = i
    for j in range(i+1,len(nums)):
        if nums[min_ind] > nums[j]:
            min_ind = j
            nums[min_ind], nums[i] = nums[i], nums[min_ind]
print(*nums)