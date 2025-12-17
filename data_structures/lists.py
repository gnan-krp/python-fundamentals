#My First Lists Program
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  

numbers[0] = 111
print("\nPrevious list contents:", numbers) 

numbers[1] = numbers[4] 
print("Previous list contents:", numbers)  

print("\nList length:", len(numbers)) 


#My Second Lists Program
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  

numbers[0] = 111
print("\nPrevious list content:", numbers) 

numbers[1] = numbers[4]
print("Previous list content:", numbers)  

print("\nList's length:", len(numbers))  
del numbers[1] 
print("New list's length:", len(numbers))
print("\nNew list content:", numbers) 


#My Third Lists Program
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

