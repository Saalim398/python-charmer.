nterms = int(input("Enter the number of terms in Fibonacci series: "))
n1, n2 = 0, 1
n3 = 0
print("Fibonacci series: {}, {},".format(n1, n2), end=" ")
for i in range(0, nterms - 2):
    n3 = n1 + n2
    print("{},".format(n3), end=" ")
    n1 = n2
    n2 = n3