number = int(input())
bonus = 0

if number <= 100:
    bonus += 5  #bonus = bonus + 5
elif 100 < number < 1000:
    bonus += number * 0.2 #number * 20/100
else: #elif number > 1000
    pass
    bonus += number * 0.1

if number % 2 == 0:
    #bonus += 1
    bonus = bonus + 1
elif number % 10 == 5:
    bonus = bonus + 2

print (bonus)
print (bonus + number)

