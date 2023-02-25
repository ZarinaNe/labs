#Лаба №2 "Задача об арифметическом выражении"
#На вход подаётся математическое выражение. Элементы - числа. Операции - "+ - * /".
#Также есть скобочки. Окончанием выражения служит "=".
#Программа должна вывести результат выражения.
#Программа также должна делать "проверку на дурака": нет деления на 0, все скобки стоят верно (см лабу №1) и т.п.

priority = {'+': 1,
            '-': 1,
            '*': 2,
            '/': 2}
exep = ['(', ')']

#разделение всех элементов выражения, получаем массив с разделенными элементами: числа, скобки, операции
def separate(s):
    arr = []
    elem = ''
    for i in range(len(s)):
        if s[i].isdigit():
            elem += s[i]
        else:
            if elem != '':
                arr.append(elem)
                elem = ''
            arr.append(s[i])
    return arr

def last(arr):
    return arr[len(arr)-1]

def if_empty(arr):
    return len(arr) == 0

def count_two(b, a, sign):
    if sign == '+':
        return a+b
    if sign == '-':
        return a-b
    if sign == '*':
        return a*b
    if sign == '/':
        return a/b

def count(s):
    i = 0
    expression = separate(s)
    print(expression)
    numbers = []
    signs = []
    for elem in expression:
        if elem.isdigit():
            numbers.append(int(elem))
        elif elem == '(':
            signs.append(elem)
        elif elem == ')':
            i = len(signs) - 1
            if if_empty(signs):
                print("ошибка в расставлении скобок")
                return False
            #вычисление выражения в скобках
            while signs[i] != "(":
                if i == 0 and signs[i] != "(":
                    print("ошибка в расставлении скобок")
                    return False
                res = count_two(numbers.pop(), numbers.pop(), signs.pop())
                numbers.append(res)
                i -= 1
            if last(signs) in exep:
                signs.pop()
            else:
                print("ошибка")
                return False
        elif elem == "=":
            res = count_two(numbers.pop(), numbers.pop(), signs.pop())
            numbers.append(res)
            if if_empty(signs):
                print(last(numbers))
                return True
            else:
                print("ошибка в расставлении знаков операций или скобок")
                return False
        else:
            if if_empty(signs) or last(signs) in exep:
                signs.append(elem)
            elif priority[elem] > priority[last(signs)]:
                signs.append(elem)
            else:
                while not if_empty(signs):
                    res = count_two(numbers.pop(), numbers.pop(), signs.pop())
                    numbers.append(res)
                signs.append(elem)

s = '2+2='
count(s)