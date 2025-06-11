def login_req(func):
    def inner(name,status):
        if status == False:
            print("Please create account and login")
        else:
            return func(name,status)
        
    return inner
