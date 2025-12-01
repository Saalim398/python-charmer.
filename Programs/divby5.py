mylist = range(1, 101)
total = sum(num for num in mylist if num % 5 == 0)
print(f"The sum of number divisible by 5 is: {total}")