budget = float(input())
number_of_statists = int(input())
one_dress_statist = float(input())
decor =  budget * 0.1 #budget * 10 / 100
dresses_price = number_of_statists * one_dress_statist
if number_of_statists > 150:
    dresses_price *= 0.9 #dresses_price = dresses_price * 90 / 100
needed_money = decor + dresses_price
difference = abs(needed_money-budget)
if needed_money > budget: #Парите не стигат
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else: #Парите стигат --> budget >= needed_money
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
