#. How to execute inner functions.

def outer():
    
    print("Outer function is executing now")

    def inner():
        print("This is a inner function")

    def logout():
        print("Please logout")

    inner()
    logout()

outer()

#Output: 
   # Outer function is executing now
   # This is a inner function
   # Please logout