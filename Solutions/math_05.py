# # Print the sum of numbers from 1 to 100

# n = 100
# # By the formula
# sum_number = n * (n + 1) // 2
# print(f"Sum: {sum_number}")

# Using for loop 
#sum_number = 0
#for i in range(1, 101):
#    sum_number += i
#print(f"Sum: {sum_number}")

# using while loop 
# i = 1
# sum_number = 0
# while i <= 100:
#     sum_number += i
#     i += 1
# print("Sum:", sum_number)



#using sum range

# sum_number = sum(range(1, 101))
# print(f"Sum :{sum_number}") 


#using  Lambda 
from functools import reduce
sum_result = reduce(lambda x, y: x + y, range(1, 101))
print("Sum:", sum_result)

##