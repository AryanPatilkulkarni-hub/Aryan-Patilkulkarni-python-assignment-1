"""
6.	A company needs a program that reads employee names and their basic salary.
The program should: Calculate total salary including HRA (20%) and DA (10%).
Stop taking input when the user types "stop". Display each employee’s total salary at the end.
Concepts: while loop, arithmetic operations, condition check, formatted output.

"""

employee = []
print("Please enter employee details and enter stop to finish")
while True:
    name = input("Enter employee name: ")
    if name == "stop":
        break
    try:
        bsalary = int(input("Enter basic salary: "))
        hra = bsalary*0.20
        da = bsalary*0.10
        tsalary = bsalary+hra+da
        employee.append({
            'name': name,
            'basic salary': bsalary,
            'total salary': tsalary
        })
    except ValueError:
        print("Error: Please enter a valid salary!")
print("Employee report")
for i in employee:
    print(f"Employee: {i['name']}")
    print(f"Basic Salary: {i['basic salary']:.2f}")
    print(f"Total Salary: {i['totalsalary']:.2f}")
