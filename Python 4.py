"""
4.	A traffic system records the average speed of vehicles every hour for 12 hours.
Write a program that: Reads 12 speed values (floats). Calculates the average speed. Displays whether traffic flow was “Slow” (avg < 40), “Normal” (40–80), or “Fast” (avg > 80).
Concepts: list input, loop, conditional check, average calculation.

"""
speed = []
print("Please enter the 12 speeds")
for i in range(12):
    speed.append(float(input(f"Enter speed for hour {i+1}: ")))

Average = sum(speed)/12
if Average < 40 :
   print("Slow")
elif 40 <= Average <=80 :
    print("Normal")
else :
    print("Fast")
