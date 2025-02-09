# difference between 2 numbers

def diff(a,b):
    if abs(abs(a)- abs(b))<=5:

        return True
    else:
        return False

check = diff(-19,19)
print(check)