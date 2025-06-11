#4.Example program for variable length arguments
#In this type we can use (*) before the last argument in the function name like add(a, *b).

def add(a, *b):
    return a,b

r1=add(12,15,45,18)

print(r1)  #output:(12,(15,45,18))

r2=add(19,45,18,65,17)

print(r2)  #output:(19,(45,18,65,17))
