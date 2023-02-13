#ЛАБА №7 Сортировка Шелла

from random import randint

#создаем случайную последовательность
x = int(input("Введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

step=len(nums)//2
while step>0:
    for i in range(step, len(nums)):
        j=i
        while j>=step and nums[j]<nums[j-step]:
            nums[j], nums[j - step]=nums[j - step], nums[j]
            j=j-step
    step=step//2
print(*nums)