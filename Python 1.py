"""
1.	Create a python program that asks the user how far they want to travel. If they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle. if they want to travel three hundred miles or more tell them to drive Super-Car
"""

distance = int(input("How far do you want to travel (in miles)? "))

if distance < 3:
    print("You should ride a Bicycle.")
elif distance>=3 and distance < 300:
    print("You should ride a Motor-Cycle.")
else:
    print("You should drive a Super-Car.")
