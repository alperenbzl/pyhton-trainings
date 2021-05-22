# toplama

def hesapla(p1, operator, p2=0):
    result = 0
    if operator == "+":
        result = p1+p2
    if(operator == "-"):
        result = p1-p2
    if(operator == "*"):
        result = p1*p2
    if(operator == "/"):
        result = p1/p2
    if(operator == "k"):
        result = p1*p1
    if(operator == "b"):
        result = 1/p1
    return result


def topla(param1, param2):
    return int(param1)+int(param2)


# cıkarma

def cıkarma(s1, s2):
    return int(s1)-int(s2)

# carpma


def carpma(p1, p2, p3):
    return int(p1)*int(p2)*int(p3)

# bolme


def bolme(k1, k2):
    return int(k1)/int(k2)
