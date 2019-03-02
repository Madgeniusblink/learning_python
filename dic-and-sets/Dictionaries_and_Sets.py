

BlackShoes = {7.5: 3, 10: 2, 8: 3, 9.5: 10}

while True:
    try:
        purchaseSize = float(input("which shoes size would you like to buy?\n"))
        if purchaseSize < 0:
            break

        if BlackShoes[purchaseSize] > 0:
            BlackShoes[purchaseSize] -= 1
        else:
            print("Shoes are no longer in stock")
    except KeyError:
        print("Sorry we do not have that size")
    print(BlackShoes)


# Sets = {"elements1", "element2", "element1", "element4"}
# print(Sets)
# if "element1" in Sets:
#     print("Yes")
#
#
# CountryList = []
#
# for i in range(5):
#     Country = input("What is your fav country? ")
#     CountryList.append(Country)

# CountrySet = set(CountryList)
#
# print(CountryList)
# print(CountrySet)
#
# if "Colombia" in CountrySet:
#     print("attended")

# Dictionary = {"Scottsdale": "569852",
#               "Phoenix": "996665",
#               "Tempe": "652358"}
# CountryDictionary = {}
#
# for Country in CountryList:
#     if Country in CountryDictionary:
#         CountryDictionary[Country] += 1
#     else:
#         CountryDictionary[Country] = 1
#
# print(CountryDictionary)