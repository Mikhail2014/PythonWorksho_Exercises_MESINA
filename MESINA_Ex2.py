#A Python program that computes the factorial of an integer
print("Exercise 2: Factorial of an Integer:");

Number = input("Enter integer Value: ");
factorial = 1
for i in range(1,Number + 1):
    factorial = factorial*i
print ("The factorial of the inputted number:",Number,"is",factorial);

