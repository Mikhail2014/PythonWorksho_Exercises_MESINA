#A program to process a file of DNA text, such as:
#ATGCAATTGCTCGATTAG
#Count the percent of C+G present in the DNA

DNA_file= open("DNA_text.txt").read()
DNAlength = len(DNA_file)
print("The DNA text total number is: ", DNAlength)

C = DNA_file.count('C')
G = DNA_file.count('G')
print("The number of letter Cs in the DNA are:", C)
print("The number of letter Gs in the DNA are:", G)
sum = C+G
print("The sum of C+G is:", sum)

percent = 100.00*sum/DNAlength
print("The percent of C+G present in the DNA is: ", percent)
