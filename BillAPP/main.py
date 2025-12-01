def computeBill(unitsConsumed):
    if unitsConsumed <= 100:
        bill = unitsConsumed * 2.5
    elif unitsConsumed <= 200:
        bill = ((100 * 2.5)) + ((unitsConsumed - 100) * 3.9)
    else:
        bill = (100 * 2.5) + (100 * 3.9) + (unitsConsumed - 200) * 5
    return bill   

def printBill(customerName, unitsConsumed, totalBill):
    print("*************************************************************************")
    print(f"***  Customer Name   : {customerName}")
    print(f"***  Units Consumed  : {unitsConsumed}")
    print(f"***  Total Bill (₹)  : {totalBill}")
    print("*************************************************************************")
    print()


customerNumber = int(input("Number of Customers: "))
   
for i in range(customerNumber):
    print(f"\n--- Customer {i + 1} ---")
    customerName = input("Enter Name: ")
    unitsConsumed = float(input("Enter number of units consumed: "))

    totalBill = computeBill(unitsConsumed)
    printBill(customerName, unitsConsumed, totalBill)

