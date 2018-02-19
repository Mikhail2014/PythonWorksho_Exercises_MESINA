#A Python program to Construct the following pattern, using a nested loop number.
#Expected Output:
"""
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""

from __future__ import print_function

print("Exercise 3: Nesting Loop");
Number = input("Please Input Number:" );
for x in range(0, Number+1):
    print (" ")
    for y in range(0,x):
        print (x, end="")
