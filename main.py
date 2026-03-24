order = []
total_cost = 0.0
order_requested = True
while order_requested:
    print ("select sandwich")

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
            order.append(soda)
        elif soda == "sprite":
            r = print ("$4.50")
            total_cost += 4.50
            order.append(soda)
        if soda == "Dr. Pepper":
            t = print ("$5")
            total_cost += 5
            order.append(soda)
    if drink == "lemonade":
        u = print ("$6")
        total_cost += 6
        order.append(drink)
    elif drink == "no drink":
        pass 
    m = input("Would you like desert?")
    if m == "yes":
        desert = input ("cookie, cake, or brownie?")
        if desert == "cookie":
            print ("$2.50")
            total_cost += 2.5
            order.append(desert)
        if desert == "cake":
            print ("$3.75")
            total_cost += 3.75
            order.append(desert)
        if desert == "brownie":
            print ("$3")
            total_cost += 3
            order.append(desert)
        else:
            pass
    sauces = input("would you like ketchup?")
    if sauces == "no":
        pass
    if sauces == "yes":
        quantity = input("how many packets would you like?")
        total_cost = total_cost + 1*int(quantity)
    order_requested = (input("would you like to keep ordering?") == "yes")

combo_eligible = ("tuna" in order or "chicken" in order or "veggie" in order) \
    and ("coke" in order or "sprite" in order or "Dr. Pepper" in order) \
    and ("cookie" in order or "brownie" in order or "cak" in order)
if combo_eligible:
    k = input("congatulations! you have selected the right combination for our deal! Please confirm yes to get 1$ off")
    if k == "yes":
        total_cost = total_cost - 1
print (total_cost)