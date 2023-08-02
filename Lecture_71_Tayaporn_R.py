#lecture71 โปรแกรมแสดงบิล
#เพิ่มการรวมบิล หลังจากเลือกเมยูได้แล้ว แสดงผลใบเสร็จ

menuList = []
priceList = []

def showbill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

while True:
    menuName = input("Plese Enter Menu:")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showbill()

dish = input("What would you like to order? (Enter the dish name): ")

if dish in menuList:
    dish_index = menuList.index(dish)
    print(dish, "is selected")
    quantity = int(input("How many do you want?: "))
    total_price = int(priceList[dish_index]) * quantity
    print("-----------------")
    print(dish,"          x",quantity)
    print("Total price:", total_price)
    print("-----------------")
else:
    print("the dish is not available")


