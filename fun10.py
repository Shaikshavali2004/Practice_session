
def outer_func():
    print("Outer function starts executing")

    def inner_func():
        print("Inner function starts here")

    def login():
        print("Login success")

    inner_func()
    login()

outer_func()

#Output:
   # Outer function starts executing
   # Inner function starts here
   # Login successfully
