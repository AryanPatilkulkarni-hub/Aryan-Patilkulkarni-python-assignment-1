"""
3.	You’re building a small program for a school. The user must enter the student’s name and marks in three subjects. The program should calculate the total, average, and display a grade. If marks are not between 0 and 100, show an error message. 
Concepts: Input/Output, data validation, arithmetic, if–elif–else.

"""

try :
  name = input("Please enter the students name ")
  mark1 = int(input("Please enter the marks of subject 1 "))
  mark2 = int(input("Please enter the marks of subject 2 "))
  mark3 = int(input("Please enter the marks of subject 3 "))
  if 0<= mark1 <= 100 and 0<= mark2 <= 100 and 0<= mark3 <= 100 :
    total = mark1 + mark2 + mark3
    print(f"Total marks : {total}")
    Average = total/3
    print(f"Average marks : {Average:.2f}")
    if Average >= 90 :
      print("Grade : A")
    elif Average >= 80 :
      print("Grade : B")
    elif Average >= 70 :
      print("Grade : C")
    elif Avergae >= 60 :
      print("Grade : D")
    else :
      print("Grade : F")
  else :
    print("Please enter marks between 0 and 100")
except :
  print("Please enter the information in the correct data type")
