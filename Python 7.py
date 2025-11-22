"""

7.	Given list of items purchased in a file display the following: No of items purchased, No of free items, Amount to pay, Discount given, Final amount paid
Concepts: files, dictonary

Sample output for purchase-1.txt file:
No of items purchased: 5 
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405

(Test your program on below given purchase-1.txt and purchase-2.txt)

"""

purchased = {}
free = {}
discount = {}

purchased = {}
free = {}
discount = {}

def callfile(filename):
    with open(filename, "r") as file:
        line = file.readlines()

    for i in line:
        i = i.strip()
        word = i.split()
        if len(word) == 0:
            continue
        if "Discount" in i:
            discount["Amount"] = int(word[1])
        elif "Free" in i:
            item = word[0]
            free[item] = 0
        else:
            item = word[0]
            purchased[item] = int(word[-1])
    total = len(purchased)
    freeitems = len(free)
    amount = sum(purchased.values())
    discount1 = int(discount["Amount"])
    finalvalue = amount - discount1

    print(f"Total number of items purchased : {total}")
    print(f"Number of free items : {freeitems}")
    print(f"Total amount to pay : {amount}")
    print(f"Discount given : {discount1}")
    print(f"Final amount after discount : {finalvalue}")

callfile("purchase-1.txt")
callfile("purchase-2.txt")
