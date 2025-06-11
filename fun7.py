# How to create inner function

def outer():
    
    #print("Outer function is executing now")

    return 18

    def inner():
        print("This is a inner function")

    def logout():
        print("Please logout")

#outer()  #output: Outer function is executing now

print(outer()) #output: 18