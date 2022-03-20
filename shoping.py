budget = float(input())
videocards = int(input())
processors = int(input())
ram = int(input())

price_videcard = 250
price_videocard_total = price_videcard * videocards
price_processor = price_videocard_total * 0.35
price_processor_total = processors * price_processor
price_ram = price_videocard_total * 0.1
price_ram_total = ram * price_ram

total_price_all = price_videocard_total + price_processor_total + price_ram_total
# print (price_videocard_total)
# print (price_processor)
# print (price_ram_total)

if videocards > processors:
    discount = total_price_all * 0.15
    total = total_price_all - discount
else:
    total = total_price_all

if budget >= total:
    print (f"You have {budget - total:.2f} leva left!")
elif budget <= total:
    print (f"Not enough money! You need {total - budget:.2f} leva more!")
