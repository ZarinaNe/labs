#ЛАБА №8 Поразрядная сортировка

from random import randint
import math

#создаем случайную последовательность
x = int(input("Введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

digits = int(math.log10(max(nums))) + 1 #определяем макс кол-во разрядов
rang = 10

for i in range(digits):
    lists = [[] for k in range(rang)]
    for num in nums:
        tmp = int((num // 10**i) % 10)
        lists[tmp].append(num)
    nums = []
    for j in range(rang):
        nums += lists[j]
print(*nums)