# maximum of 3 number
def max3(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

x= max3(94,9,56)
print(x)