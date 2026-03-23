order = []
total_cost = 0.0
print ("select sandhich")
sandwich = input("chicken,tuna,veggie, no sandwich: ")
if sandwich == "chicken": 
    print("$13")
    order.append(sandwich)
    total_cost += 13
elif sandwich == "tuna":
    print("$15")
    total_cost += 15
    order.append(sandwich)
elif sandwich == "veggie":
    print("$100")
    total_cost += 100
    order.append(sandwich)
elif sandwich == "no sandwich":
    print ("select drink")
drink = input("soda, lemonade, water, no drink: ")
if drink == "soda":
    soda = input("coke, sprite, Dr. Pepper: ")
    if soda == "coke":
       e = print ("$5")
       total_cost += 5
    if soda == "sprite":
        r = print ("$4.50")
        total_cost += 4.50
    if soda == "Dr. Pepper":
        t = print ("$5")
        total_cost += 5
if drink == "lemonade":
    u = print ("$6")
    total_cost += 6
elif drink == "no drink":
   m = input("Would you like desert?")
   if m == "yes":
      d = input ("cookie, cake, or brownie?")
      if d == "cookie":
          print ("$2.50")
          total_cost += 2.5
      if d == "cake":
          print ("$3.75")
          total_cost += 3.75
      if d == "brownie":
          print ("$3")
          total_cost += 3
# g = (0.0)
# if sandwich == "chicken":
#     g = (g + 13)
# if sandwich == "tuna":
#     g = (g + 15)
# if sandwich == "veggie":
#     g = (g + 100)
# if drink == "lemonade":
#     g = (g + 6)
# if drink == "water":
#     g = (g+0)
# if soda == "coke":
#     g = (g + 5)
# if soda == "sprite":
#     g = (g + 4.50)
# if soda == "Dr. Pepper":
#     g = (g + 5)
# if d == "cookie":
#     g = (g+2.50)
# if d == "cake":
#     g = (g+3.75)
# if d == "brownie":
#     g = (g+3)
# print (g)