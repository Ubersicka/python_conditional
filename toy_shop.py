price_excursion = float(input())
count_puzzle = int(input())
count_speaking_doll = int(input())
count_bear = int(input())
count_minion = int(input())
count_truck = int(input())

puzzle = 2.60
speaking_doll = 3
bear = 4.10
minion = 8.20
truck = 2

total_price_toys = (count_puzzle * puzzle) + (count_speaking_doll * speaking_doll) \
                   + (count_bear * bear) + (count_minion * minion) + (count_truck * truck)

count_all = count_puzzle + count_speaking_doll + count_bear + count_minion + count_truck

if count_all >= 50:
    discount_shop = total_price_toys * 0.25
    win_money = total_price_toys - discount_shop
    rent = win_money * 0.1
    profit = win_money - rent
else:
    win_money = total_price_toys
    rent = win_money * 0.1
    profit = total_price_toys - rent

left_moneys = price_excursion - profit

if profit >= price_excursion:
    left_money = profit - price_excursion
    print (f"Yes! {left_money:.2f} lv left.")
else:
    print (f'Not enough money! {left_moneys:.2f} lv needed.')
