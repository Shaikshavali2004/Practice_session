from login import login_req


def home_page(name,status):
    print("Go to the flipkart Home Page")


@login_req
def services_page(name,status):
    print("Use the services from flipkart")

@login_req
def orders(name,status):
    print("To make orders Please login into flipkart account first")

def reviews(name,status):
    print("Provide reviews to the products")

home_page("SV",True)
services_page("SV",True)
orders("SV",False)
reviews("SV",True)