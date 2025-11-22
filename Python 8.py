"""
8.	Output dictionary which contains only the odd numbers that are present in the input list as keys and their cubes as values using List Comprehension
"""

x = int(input("Please enter how many numbers you want to enter into the list: "))
n = [int(input("Enter the number: ")) for i in range(x)]
oddvalue = {num: num**3 for num in n if num % 2 != 0}
for x,y in oddvalue.items():
    print(x, ":", y)
