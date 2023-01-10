first_number = int (input ("Give me the value of the first number: ")) 
second_number = int (input ("Enter the value of the second number: "))
third_number = int (input ("Enter the third number: "))

#we assume the first number is the largest

largest_number = first_number

if second_number > largest_number:
    largest_number = second_number

if third_number > largest_number:
    largest_number = third_number

print ("the largest number is :", largest_number )