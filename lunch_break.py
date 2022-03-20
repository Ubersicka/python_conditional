import math

name_of_serie = input()
episode_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght / 8
# print(lunch_time)
rest_time = break_lenght / 4
# print(rest_time)

left_break_time = break_lenght - lunch_time - rest_time

if episode_lenght <= left_break_time:
    print(f"You have enough time to watch {name_of_serie} and left with \
{math.ceil(left_break_time-episode_lenght)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serie}, you need \
{math.ceil(episode_lenght-left_break_time)} more minutes.")
