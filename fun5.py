# #.Example program for default arguments

def cal(a,b,c=5):

    return a+b+c,a-b-c

result1 = cal(20,12,4)

print(result1)   #output:(36, 4)

result2 = cal(35,18)

print(result2)  #output:(58, 12)

print(type(result2)) #output:<class 'tuple'>