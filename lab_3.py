#Лаба №3 "Задача о простых множителях"
#На вход дается одно число х, нужно вывести все числа от 1 до х, удовлетворяющие условию:
#3^k*5^j*7^i=xi 3,9.7.5
#где i, j, k - натуральные числа или могут быть равны 0.

import math
x = int(input())
xi = 1
numbers = set() #создаем мн-во неповторяющихся элементов
while xi < x:
    for i in range(0, int(math.log(x, 7)+1)):
        for j in range(0, int(math.log(x, 5)+1)):
            for k in range(0, int(math.log(x, 3)+1)):
                xi = 7**i + 5**j + 3**k
                if xi <= x:
                    numbers.add(xi)
                else:
                    break
print(*numbers) #опер * передает все элементы мн-ва в вызов print() как отдельные аргументы