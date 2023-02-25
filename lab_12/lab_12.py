#Лаба №12 внешняя многофазная сортировка

import random

#генерация рандомной последовательности в input.txt
def fill_rand(name):
    f = open(name, 'w')
    for i in range(20):
        f.write(str(random.randint(1, 100)) + '\n')
    f.close()

#сортировка слиянием
def merge_sort(A):
    if len(A) <= 1:
        return A
    left = merge_sort(A[:len(A) // 2])
    right = merge_sort(A[len(A) // 2:])
    l = r = i = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            A[i] = left[l]
            l += 1
        else:
            A[i] = right[r]
            r += 1
        i += 1
    while l < len(left):
        A[i] = left[l]
        i += 1
        l += 1
    while r < len(right):
        A[i] = right[r]
        i += 1
        r += 1
    return A

def multiphase_sort(name):
    f = open(name, 'r')
    #разбиваем числа из input на два отсортированных файла
    for k in range(2):
        arr = []
        for j in range(10):
            arr.append(int(f.readline()))
        merge_sort(arr)
        name = str(k+1) + '.txt'
        f2 = open(name, 'w')
        for j in range(10):
            f2.write(str(arr[j])+'\n')
    f.close()
    f2.close()

    #объединяем и сортируем числа из файлов
    for k in range(2):
        arr = []
        f1 = open('1.txt', 'r')
        f2 = open('2.txt', 'r')
        if k == 1:
            for s in range(5):
                f1.readline()
                f2.readline()
        for j in range(5):
            arr.append(int(f1.readline()))
            arr.append(int(f2.readline()))
        merge_sort(arr)
        f = open('output.txt', 'a')
        for j in range(10):
            f.write(str(arr[j])+'\n')


name = 'input.txt'
fill_rand(name)
multiphase_sort(name)