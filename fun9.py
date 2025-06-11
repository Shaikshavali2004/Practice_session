#. How to execute inner functions in another way using return keyword.

def outer():
    
    print("Outer function is executing now")

    def inner():
        print("This is a inner function")
    
    def logout():
      print("Please logout")

    #return inner 
    return logout
 
#inner=outer() #Output:Outer function is executing now

#inner()  #Output:This is a inner function

logout=outer() #Output:Outer function is executing now

logout()  #Output:Please logout
