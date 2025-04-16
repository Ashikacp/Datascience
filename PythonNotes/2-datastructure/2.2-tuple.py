#Tuple is collection of ordered and immutable elements enclosed in parentheses()

# Tuples are Immutable ie, we can’t change values in them.
 
#creating a tuple
empty_tuple=()    #create empty tuple
print(empty_tuple)        #o/p= ()
print(type(empty_tuple))  #o/p= <class 'tuple'>

tup=tuple() #create empty tuple
print(type(tup)) # o/p=<class 'tuple'>
lst=list()  
print(type(lst))  #o/p=<class 'list'>

mixed_tuple=(1,"hello",3.14,True)
print(mixed_tuple)   #o/p=(1, 'hello', 3.14, True)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#TYPE conversion

num=tuple([1,2,3,4,5,6])  #list converted into tuple
print(num)  #o/p=(1, 2, 3, 4, 5, 6)

num=list((1,2,3,4,5))  #converted tuple into list
print(num)  #o/p=[1, 2, 3, 4, 5]

# -----------------------------------------------------------------------------------------------------------------------------------------------------------


#Accessing tuple elements   (same as in list)

num=(1,2,3,4,5,6)
print(num[0])  #o/p=1
print(num[-1]) #o/p=6
print(num[0:4]) #o/p= (1, 2, 3, 4)
print(num[::])  #o/p=(1, 2, 3, 4, 5, 6)
print(num[::-1]) #o/p=(6, 5, 4, 3, 2, 1)   #reverse of tuple value

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Tuple operation
#Concantination of Tuple

mixed_tuple=(1,"hello",3.14,True)
num=(1,2,3,4,5,6)

concantination_tuple=mixed_tuple+num
print(concantination_tuple)  #o/p=(1, 'hello', 3.14, True, 1, 2, 3, 4, 5, 6)

mult=mixed_tuple * 3   # n no:of times tuple will append
print(mult)  #o/p= (1, 'hello', 3.14, True, 1, 'hello', 3.14, True, 1, 'hello', 3.14, True)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#immutable nature of Tuple

lst=[1,2,3,4,5]
lst[1]="krish"  # list are mutable
print(lst)  #o/p= [1, 'krish', 3, 4, 5]

num=(1,2,3,4,5,6)
num[1]="krish"
print(num)  #o/p= TypeError: 'tuple' object does not support item assignment
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#TUPLE methods

num=(1,2,3,1,4,5,6,1)
print(num.count(1))  #o/p=3

print(num.index(1))  #o/p=0 #it wil give  the first index of given value. index of 1 =0

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Packing a tuple

packed_tuple=1,"hello",3.14   #whenver we define values in a way like comma separated ,bydefault it will pack and return a packed tuple
print(packed_tuple)  #o/p= (1, 'hello', 3.14)

# Unpacking a tuple

a,b,c=packed_tuple
print(a)  #o/p=1
print(b)  #o/p=hello
print(c)  #o/p=3.14

#unpacking with *

numbers=(1,2,3,4,5,6)
first,*middle,last=numbers

print(first)  #o/p= 1
print(middle) #o/p=[2, 3, 4, 5]
print(last)   #o/p=6

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Nested List

lst=[[1,2,3,4],[6,7,8,9],[1,'hello',3.14,'c']]  #Nested List (list inside a list)
print(lst[0]) #o/p= [1, 2, 3, 4]
print(lst[0][3]) #o/p= 4
print(lst[0][0:3])  #o/p=[1, 2, 3]


lst=[[1,2,3,4],[6,7,8,9],(1,'hello',3.14,'c')]  #tuple inside a list
print(lst[2][1:3])  #o/p=('hello', 3.14)
print(lst[0])  #o/p=[1, 2, 3, 4]


#Nested Tuple

nested_tuple=((1,2,3),('a','b','c'),(True,False))  #tuple inside a tuple
print(nested_tuple[0]) #o/p=1, 2, 3)
print(nested_tuple[1][2]) #o/p= ç

#Iterating over nested Tuple

for sub_tuple in nested_tuple:   #sub_tuple refers to each individual tuple inside the nested_tuple.
    for item in sub_tuple:      #This inner loop iterates over each item within the current sub_tuple.
        print(item,end=" ")
    print()
'''
#o/p= 
1 2 3 
a b c 
True False 
'''
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.

def min_in_tuple(tpl):
    return min(tpl)

def max_in_tuple(tpl):
    return max(tpl)

def sum_of_tuple(tpl):
    return sum(tpl)

sample_tpl = (1, 2, 3, 4, 5)
print(f"Minimum: {min_in_tuple(sample_tpl)}")
print(f"Maximum: {max_in_tuple(sample_tpl)}")
print(f"Sum: {sum_of_tuple(sample_tpl)}")

'''
o/p= 
Minimum: 1
Maximum: 5
Sum: 15
'''