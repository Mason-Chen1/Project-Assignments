foodPrice = {"Chicken": 1.59, "Beef": 1.99, "Cheese": 1.00, "Milk": 2.50}

def sumPrice(price1, price2):
    sum = (price1 + price2)
    print("The total price of Chicken and Beef is " + str(sum))

print(sumPrice(foodPrice.get("Chicken"), foodPrice.get("Beef")))

def differencePrice(price1, price2):
    difference = (price1 - price2)
    print("The difference of Beef and Chicken is " + str(difference))

print(differencePrice(foodPrice.get("Beef"), foodPrice.get("Chicken")))


shoeQuantity = {"Jordon 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

def restock(item1, item2):
    new = (item1 * item2)
    print("There are now " + str(new) + " pairs of Yeezy's")

print(restock(shoeQuantity.get("Yeezy"), 3))

def clearanceSale(item1, item2):
    amount = (item1 / item2)
    print("We only have " + str(amount) + " pairs of SB Dunks left")

print(clearanceSale(shoeQuantity.get("SB Dunk"), 5))

cityNames = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
cityNames.sort(key=len)
print(cityNames)

#Sort numbers by size
sort = sorted(foodPrice.items(), key=lambda x: x[1])
for i in sort:
    print(i[0], i[1])
