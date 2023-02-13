#Лаба №4 Сортировка методом прочесывания

from random import randint

#создаем случайную последовательность
x = int(input("Введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

step = len(nums)
while step > 1 or swap:
    swap = False
    i = 0
    for i in range(len(nums) - step):
        if nums[i] > nums[i+step]:
            nums[i], nums[i + step] = nums[i + step], nums[i]
            swap = True
    if step>1:
        step-=1
print(*nums) #опер * передаёт все элементы nums в вызов print() как отдельные аргументы