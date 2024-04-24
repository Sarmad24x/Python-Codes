shoplist=['apple','mango','Banana','carrot']

print("I have ",len(shoplist),"in the list.")

print("These items are "),
for item in shoplist:
    print (item)

print("\n i also have to buy rice")
shoplist.append("Rice")
print("My List now", shoplist)

print("sorting")
shoplist.sort()
print("Sorted List", shoplist)

print("The first itm i will buy is ",shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("My list now ",shoplist)

