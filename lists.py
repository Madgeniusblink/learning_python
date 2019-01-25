myUniqueList = []
max_item = 6
myLeftovers = []


def add_to_list():
    print("To quite the list type or print 'done'")
    infinity_loop = 1
    while infinity_loop == 1:
        item = input("what would you like to add to your Unique List? ")
        if item in myUniqueList:
            print("Item is in list already")
            myLeftovers.append(item)
        elif item == "done":
            break
        else:
            myUniqueList.append(item)


add_to_list()

print("This is your list")
print(myUniqueList)
print("MY LEFTOVERS")
print(myLeftovers)
