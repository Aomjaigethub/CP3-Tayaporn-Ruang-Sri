#โปรแกรมร้านขายของง่ายๆ

userid = input("enter userID:")
userpassword = input("enter password:")

if userid == "zz" and userpassword == "zz":
    print()
    print("logged in")
    print()
    print("welcome", userid, "to simple shop")
    print("----------item list----------")
    print("1. congo banana     25.00 THB")
    print("2. sudan apple      69.00 THB")
else:
    print("Login failed.")

print()
print("what would you like to buy?")
cart = int(input("enter the number from the list:"))

if cart == 1:
    print()
    print("Congo Banana selected")
    amount = int(input("how many do you want?"))
    total = 25 * amount
    print("-------------Order Summary------------")
    print("Congo Banana          x", amount, total, "THB")
    print("--------------------------------------")
    print("total                    ", total, "THB")
    print("thank you for shopping with us")
    print("--------------------------------------")

elif cart == 2:
    print()
    print("Sudan Apple selected")
    amount = int(input("how many do you want?"))
    total = 69 * amount
    print("-------------Order Summary------------")
    print("Sudan Apple           x", amount, total, "THB")
    print("total                    ", total, "THB")
    print("thank you for shopping with us")
    print("--------------------------------------")
else:
    print("--this item does not exist, Try again--")
