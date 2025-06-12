#Writing a program using for loop.
"""

product_price = [98,198,298,398,498]
new_price = []

for price in product_price:
    new_price.append(price + 1)

print(product_price)
print(new_price)

"""

#Program using map function.
"""

prd_price = [100,200,300,400,500]

def subone(price):
    return price-1

map_obj = map(subone, prd_price)
new_prices = list(map_obj)
 
print(prd_price)
print(new_prices)

"""

#How to write the above program using lambda function.

print(list(map(lambda price:price-1,[1000,2000,3000,4000,5000])))