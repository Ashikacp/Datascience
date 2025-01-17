
# list is a collection of ordered and mutable elements , enclosed in square brackets.


fruits=["apple","banana","orange","kiwi","guava"]

print(fruits[0]) # index=0          o/p= apple

print(fruits[1:]) # index 1 to n    o/p=['banana', 'orange', 'kiwi', 'guava']

print(fruits[1:3])  # index 1, 2 .wont take indx=3     o/p=['banana', 'orange']

print(fruits[-1:]) # o/p= ['guava']

print(fruits[-1:-2])   #o/p=[]

fruits[1:]='watermelon'
print(fruits)  #o/p= ['apple', 'w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n']

#-----------------------------------------LIST METHODS----------------------------------------------------------------------------------
#basic List Operation

fruits.append("cherry") #add an item to the end 
print(fruits)  #o/p=['apple', 'banana', 'orange', 'kiwi', 'guava', 'cherry']

fruits.insert(1,"banana") #add an item at indx=1 
print(fruits) #o/p= ['apple', 'banana', 'banana', 'orange', 'kiwi', 'guava', 'cherry']

fruits.remove("banana") #remove the first occurance of an item
print(fruits) #o/p= ['apple', 'banana', 'orange', 'kiwi', 'guava', 'cherry']


fruits=["apple","banana","orange","kiwi","guava"]
pop_fruits=fruits.pop() # remove and return last element

print(pop_fruits)  #o/p=guava
print(fruits) #['apple', 'banana', 'orange', 'kiwi']

print(fruits.index("kiwi")) #o/p=3

fruits.insert(1,"banana") 
print(fruits) #o/p=['apple', 'banana', 'banana', 'orange', 'kiwi']
print(fruits.count("banana")) #o/p=2

fruits.sort() #sort in ascending order
print(fruits) #o/p=['apple', 'banana', 'banana', 'kiwi', 'orange']

fruits.reverse() 
print(fruits)  #o/p=['orange', 'kiwi', 'banana', 'banana', 'apple']

fruits.clear()  # remove all items from the list
print(fruits) #o/p=[]
#-----------------------------------------slicing list------------------------------------------------------------------------------

num=[1,2,3,4,5,6,7,8,9]
print(num[2:5])   #o/p=[3, 4, 5]
print(num[:5])    #o/p=[1, 2, 3, 4, 5]
print(num[5:])    #o/p=[6, 7, 8, 9]

print(num[::])    #o/p=[1, 2, 3, 4, 5, 6, 7, 8, 9]      #for num[::] All the elements will be printed
print(num[::2])   #o/p=[1, 3, 5, 7, 9]   # step size=2
print(num[::-1])  #o/p=[9, 8, 7, 6, 5, 4, 3, 2, 1]
print(num[::-2])  #o/p=[9, 7, 5, 3, 1]

#-------------------------------------  iterating over list --------------------------------------------------------------------------------------

num=[1,2,3,4,5,6,7,8,9,10]

for i in num:
    print(i, end=" ")  #o/p= 1,2,3,4,5,6,7,8,9,10

#iterate with index

num=[1,2,3,4,5,6,7,8,9,10]

for index,number in enumerate(num):
    print(index,number) 
#-------------------------------------------  #list comprehension --------------------------------------------------------------------------------

lst=[]
for x in range(5):
    lst.append(x ** 2)

print(lst)  #o/p= [0, 1, 4, 9, 16]
 
#we can use another format called LIST COMPREHENSION   [expression for item in iterable]

square=[x**2 for x in range(5)]
print(square)  #o/p= [0, 1, 4, 9, 16]

## basic list comprehension
square=[num**2 for num in range(10)]
print(square)  #o/p= [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

##list comprehension with conditions    [expression for item in iterable if condition]

even=[num for num in range(10) if num%2==0]
print(even)  # o/p=[0, 2, 4, 6, 8]

#nested list comprehension  [expression for item1 in iterable1 for item2 in iterable2]

lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair=[(i,j) for i in lst1 for j in lst2]
print(pair) #o/p=(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd'), (4, 'a'), (4, 'b'), (4, 'c'), (4, 'd')]


words=["hello","world","python","list","comprehension"]
length=[len(word) for word in words]
print(length)  #o/p=[5, 5, 6, 4, 13]

#---------------------------------------------------------------------------------------------------------------------------


#Create a list of the first 20 positive integers. Print the list.
lst=[]
for i in range(1,21):
    lst.append(i)
print(lst) #o/p=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#---------------------------------------------------------------------------------------------------------------------------
#Create a new list containing only the even numbers from the list lst. using a list comprehension,Print the new list.
lst = list(range(1, 21))
print(lst)
evens = [x for x in lst if x % 2 == 0]
print(evens)
#---------------------------------------------------------------------------------------------------------------------------
#Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.

import random

random_numbers = [random.randint(1, 20) for _ in range(15)]
print(random_numbers) #o/p=[4, 17, 17, 4, 17, 16, 14, 15, 5, 3, 14, 19, 9, 12, 19]

sorted_numbers = sorted(random_numbers)
print(sorted_numbers) #o/p=[3, 4, 4, 5, 9, 12, 14, 14, 15, 16, 17, 17, 17, 19, 19]

sorted_numbers_desc = sorted(random_numbers, reverse=True)
print(sorted_numbers_desc) #o/p=[19, 19, 17, 17, 17, 16, 15, 14, 14, 12, 9, 5, 4, 4, 3]

unique_numbers = list(set(random_numbers))
print(unique_numbers) #o/p=[3, 4, 5, 9, 12, 14, 15, 16, 17, 19]
#---------------------------------------------------------------------------------------------------------------------------

 #Use a list to collect and analyze user feedback.
# Collecting user feedback
feedback = ["Great service!", "Great food","GREAT Person","Very satisfied", "Could be better", "Excellent experience"]

# Adding new feedback
feedback.append("Not happy with the service")

positive_feedback_count =sum(1 for comment in feedback if 'great' in comment.lower() or 'excellent' in comment.lower())
print(positive_feedback_count)  #o/p=4