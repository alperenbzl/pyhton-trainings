# toplama

from math import sqrt


def hesapla(p1, operator, p2=0):
    result = 0
    if operator == "+":
        result = p1 + p2
    if operator == "-":
        result = p1 - p2
    if operator == "*":
        result = p1 * p2
    if operator == "/":
        result = p1 / p2
    if operator == "k":
        result = p1 * p1
    if operator == "b":
        result = 1 / p1
    if operator == "z":
        result = sqrt(p1)
    if operator == "d":
        result = abs(p1)
    if operator == "x":
        result = pow(p1, p2)
    return result


# toplama
def topla(param1, param2):
    return int(param1) + int(param2)


# cıkarma
def cikarma(s1, s2):
    return int(s1) - int(s2)


# carpma
def carpma(p1, p2, p3):
    return int(p1) * int(p2) * int(p3)


# bolme
def bolme(k1, k2):
    return int(k1) / int(k2)


# factorial
def faktoriyel(sayi):
    # faktoriyel hesapla
    if sayi == 0:
        return 1
    toplam = 1

    for i in range(sayi, 0, -1):
        toplam = i * toplam
        print(toplam)
    return toplam


def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)


def fibonacci(n):
    # todo
    fList = []
    fList.insert(0, 0)
    for i in range(1, n + 1):
        if i <= 2:
            fList.insert(i, 1)
        else:
            fList.insert(i, fList[i - 2] + fList[i - 1])
    return fList[n]


def fibonacci_recursive(n):
    # todo
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


result = fibonacci_recursive(4)
print(result)
result = fibonacci(6)
print(result)
