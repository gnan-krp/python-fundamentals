#My First Basic Loop Program#
largest_number = -999999999
 
number = int(input("Enter a number or type -1 to stop: "))
 
while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to stop: "))
 
print("The largest number is:", largest_number)


#My Second Basic Loop Program#
odd_numbers = 0
even_numbers = 0

number = int(input("Enter a number or type 0 to stop: "))

while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Enter a number or type 0 to stop: "))

print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

