#Strings
li = [1,2,3,4,5]
print(li[4])

#List Slicing
amazon_cart = [
    "Notebooks",
    "Pens",
    "Toys",
    "Grapes"
]
print(amazon_cart)
new_cart = print(amazon_cart[0:3]) #this is a whole new list in itself

#Lists are Mutable
amazon_cart[0] = "Pencil"
print(amazon_cart)

#if we only want to copy the list use the below syntax
new_cart = amazon_cart[:]

new_cart = amazon_cart  #now the two list are interdependent 
#if we change one thing in new_cart it will reflect back in the amazon_cart
