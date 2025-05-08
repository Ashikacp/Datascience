
def even_odd(num):
    '''this fun finds even or odd'''
    if num % 2 == 0:
        print("num is even")
    else:
        print("num is odd")

#even_odd(1)  #calling a fun with parameter
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

## Function with Multiple parameter

def add(a,b):
    '''this fun add thwo varaibles'''
    return a + b

result=add(2,4)
#print(result)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

## Default parameters

def greet(name):
    print(f'hello {name}')

#greet() #TypeError: greet() missing 1 required positional argument: 'name'. so give a default value to name

#----
def greet(name="guest"):
    print(f'hello {name}')

greet()   #o/p= hello guest 
greet('jayesh')  #hello jayesh  (if we call greet fun with any name it will print that name instead of default)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

##################### Variable length arguments -positional argument and keywords arguments #################

##### Positional arguments  (basically given by *args)

#def print(num1,num2,num3,num4,num5): #instead of writing multiple parameters here we can writed def print(*args)

def print_numbers(*args):
    for numbers in args:
        print(numbers)

print_numbers(1,2,3,'krish')  # o/p= 1 2 3 krish


#### Keywords Arguments (given by **kwargs) all the parameters will be in the form of key value pairs.

def print_detaiils(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

print_detaiils(name='ashika',age=32,country='India')  #o/p= name:ashika age:32 country:India


#### combined positional and keywprds argument

def print_something(*args,**kwargs):
    for val in args:
        print(f'positional argument:{val}')
    for key,value in kwargs.items():
        print(f'{key}:{value}')

print_something(3,4,5,name='ashika',age=32,country='India')

'''
o/p=
positional argument:3
positional argument:4
positional argument:5
name:ashika
age:32
country:India
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

####### return Statement

def mult(a,b):
    return a*b

r=mult(2,3)
print(r)  #o/p=6

###### Return multiple parameters from a function

def mult(a,b):
    return a*b,a   #functn can return multiple values

r=mult(2,3)
print(r) #(6, 2)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------