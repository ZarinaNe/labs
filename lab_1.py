#Лаба №1 "Задача о скобках"
#На вход подаётся строка, состоящая из скобок.
#Программа должна определить правильность введённого скобочного выражения.

print('Введите строку')
s = input()
stack = []
right = True
for i in s:
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        if not stack:
            right = False
            break
        open = stack.pop()
        if open == '(' and i == ')':
            continue
        if open == '{' and i == '}':
            continue
        if open == '[' and i == ']':
            continue
        right = False
        break
if right and len(stack) == 0:
    print('Строка существует')
else:
    print('Строка не существует')