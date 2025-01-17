'''
multiple
commments 
can be created using - ''' '''
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------

# line continuation   - use balckslash \ to continue a statement to next line

total=1+2+3+4+5+6+7+\
4+5+6
print(total)   #o/p=43


# ---------------------------------------------------------------------------------------------------------------------------------------------------
#break  - exit the loop prematurely
for i in range(5):
    if i==2:
        break
    print("i in break example",i)       #o/p= 0 1

#continue -skip the current iteration and continue the next iteration
for i in range(5):
    if i==2:
        continue
    print(i)     #o/p= 0 1 3 4


#pass   - is a null operation .it does nothing
for i in range(5):
    if i==2:
        pass
    print(i)  #o/p= 0 1 2 3 4


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# display prime numbers b/w 1 and 100  //// number which is only divisible by one or the number itself.

for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num %i == 0:
                
                break
        else:
            print(num)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Write a program that prints a 5x5 grid of asterisks (*) using nested loops.

for i in range(0,5):
    for j in range(0,5):
        print("*", end =" " )
    print(" ")
     
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers 

sum=0

while(True):   #starts an infinite loop that keeps running unless something inside the loop tells it to stop.
   
    n=int(input("enter a num"))   #The user is continuously asked to input a number.
    if n==0: #condition is met, and the loop is exited using break.
        break
    sum= sum+n
    
  
print("sum of all numbers entered=",sum)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
 
#Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop.

n=int(input("enter a number"))
for i in range(1,n+1):
    if i%2 ==0:
        print(i)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
  
    
#Write a program that calculates the factorial of a number input by the user using a while loop.

n=int(input("enter a number"))
fact = 1 #Initialize the factorial result as 1 (since factorial of 0! and 1! is 1)
i = 1
while i <= n:
    fact = fact * i  # Multiply the current value of fact by i
    i += 1
print("The factorial is :" ,fact)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Write a program that calculates the sum of the digits of a number input by the user using a while loop.

sum_of_digits=0

n= int(input("enter a num"))
while n > 0:
    digit = n % 10  #To extract the last digit of a number.
    sum_of_digits += digit
    n = n // 10  #remove the last digit of a number, effectively "shifting" the digits to the right.

print("The sum of the digits is: ",sum_of_digits)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------


# Write a program that checks if a number input by the user is a prime number using a for loop.

n = int(input("Enter a number: "))

# Prime numbers are greater than 1
if n > 1:
    for i in range(2, n):
        if n % i == 0:  # If n is divisible by any number other than 1 and itself
            print(f"{n} is not a prime number.")
            break
    else:
        # The else part of the for loop is executed only if the loop is not broken
        print(f"{n} is a prime number.")
else:
    # If the number is 1 or less, it is not prime
    print(f"{n} is not a prime number.")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Write a program that prints the first n Fibonacci numbers, where n is input by the user.

n=int(input("enter a numbeer"))

a,b=0,1 # Initialize the first two numbers in the Fibonacci sequence

count =0  # Initialize a counter to keep track of how many numbers have been printed

while( count<n):
    print(a)
    a,b= b,a+b
    count=count+1
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#If num is a NumPy array:
import numpy as np
num = np.array([[-2.91732533,  1.825289  ],
                [ 8.28034046, 10.37035566],
                [ 8.64383354,  9.80619912]])

# Extract the first column
print(num[:, 0])#o/p=[-2.91732533  8.28034046  8.64383354]
# Extract the second column
print(num[:,1])#o/p= [ 1.825289   10.37035566  9.80619912]

# Access the first row using slicing
print(num[0, :]) #o/p= [-2.91732533  1.825289  ]

#If num is a Python list:

num = [[-2.91732533,  1.825289  ],
       [ 8.28034046, 10.37035566],
       [ 8.64383354,  9.80619912]]

# Access the first row (first sub-list)
print(num[0])

# Access the first column
first_column = [row[0] for row in num]

print(first_column)  #[-2.91732533, 8.28034046, 8.64383354]

# ---------------------from loops--------------------------------------------------------------------------------------------------------------------------------------
### sum of first n natural numbers

n=10
sum =0
count=1
while count<=n:
    print(count)  # print first n number //for checking 
    sum =sum+count
    count=count+1
print("sum of first 10 natural numbers",sum) #answer=55

#or

sum=0
for i in range(11):
    sum=sum+i
print("print sum of first 10 natural numbers",sum)

####-------------------------------------------------------------------------------------------------
