# write a python problem to calculate the factorial of the given number

"""def print_factors(x):
 print("The factors of", x, "are:")
 for i in range(1, x + 1):
  if x % i == 0:
   print(i)
num = int(input("Enter value: "))
print_factors(num)"""
#write a python program to check given number is armstrong number or not
"""def print_armstrong(x)"""
# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")