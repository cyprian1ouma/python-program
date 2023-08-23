# program to calculate the sum of numbers
# until the user enters zero

total = 0
number = int(input('Enter the number: '))

while number !=0:
    total+= number
    number = int(input("Enter the number: "))
print('Total =', total)