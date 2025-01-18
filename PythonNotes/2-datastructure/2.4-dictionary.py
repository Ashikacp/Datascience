# Dictionaries are the collections of key-value pairs, enclosed in curly braces.
#unorderd collection of item. Key must be unique and immutable,while values can be of any type.

#create empty dictionary
empty_dict={}
print(type(empty_dict))  #o/p= <class 'dict'>

#another way to create empty dict
empty_dict=dict()
print(type(empty_dict))  #o/p= <class 'dict'>

student={
    'name':'krish',
    'age': 32,
    'grade':24
}
print(student) #o/p={'name': 'krish', 'age': 32, 'grade': 24}

#Single key is always used 
student={'name':'krish', 'age': 32,'name':24} # here "name" key is not unique hence previous value(krish) got replaced with recent value(24)
print(student) #o/p={'name': 24, 'age': 32}

# ---------------------------------------  Accessing dictionary elements  --------------------------------------------------------------------------------------------------------------------

# Accessing dictionary elements

student={'name':'krish', 'age': 32,'grade':'A'}
print(student['grade']) #o/p=A
print(student['age']) #o/p=32

# Accessing dict elements uding get() methods

print(student.get('name'))  #o/p=krish
print(student.get('last_name')) #o/p= None (last_name key is not present in the dataset)
print(student.get('last_name','not available')) #o/p= not available ,ie it will print the string whichever we give instead of a none value

# ---------------------------------------------- Modify dict elements   -------------------------------------------------------------------------------------------------------------

# Modify dict elements

student={'name':'krish', 'age': 32,'grade':'A'}

student['age']=33  #updated existing value of the key
print(student) #o/p={'name': 'krish', 'age': 33, 'grade': 'A'}

student['address']='India'  #added new key and value
print(student) #o/p={'name': 'krish', 'age': 33, 'grade': 'A', 'address': 'India'}

#delete the key
del student['grade']  #delete key and value pair
print(student) #o/p={'name': 'krish', 'age': 33, 'address': 'India'}

# ------------------------------------------------------   # Dict Methods  -----------------------------------------------------------------------------------------------------

student={'name':'krish', 'age': 32,'grade':'A'}

#get all the keyes
key= student.keys()
print(key) #o/p=dict_keys(['name', 'age', 'grade'])

#get all the values
val=student.values()
print(val) #o/p= dict_values(['krish', 32, 'A'])

#get key-value pair
items=student.items()    #list of tuple
print(items) #o/p= dict_items([('name', 'krish'), ('age', 32), ('grade', 'A')])

# ----------------------------------------------------------  Shallow copy  -------------------------------------------------------------------------------------------------

student={'name':'krish', 'age': 32,'grade':'A'}
student_copy=student   #copied student dict
print(student_copy) #o/p= {'name': 'krish', 'age': 32, 'grade': 'A'}

student['name']="ashika"  # updated student name
print(student)  #o/p= {'name': 'ashika', 'age': 32, 'grade': 'A'}
print(student_copy) #o/p= {'name': 'ashika', 'age': 32, 'grade': 'A'}  #copy variable also got updated

# here if you update original variable,copy variabel also will get updated 

#Shallow copy provides a differnt memory location hence whenever we change one variable it wont impact the other variable

student={'name':'jayesh', 'age': 32,'grade':'A'}
st_copy = student.copy()

student['name'] = 'swaroop'

print("Original List:", student)  #o/p = {'name': 'swaroop', 'age': 32, 'grade': 'A'}
print("Shallow Copied List:", st_copy)  #{'name': 'jayesh', 'age': 32, 'grade': 'A'}

# ---------------------------------------   #iterating over dict --------------------------------------------------------------------------------------------------------------------

#we can use loop to iterate like in the case of list /tuple

# Iterate over keys

student={'name':'jayesh', 'age': 32,'grade':'A'}
for key in student.keys():
    print(key)#o/p= name age grade

# Iterate over values

for values in student.values():
    print(values) #o/p= jayesh 32 A

# Iterate over Key-Value pair

for key,value in student.items():
    print(f"{key}:{value}") #o/p= (name:jayesh  age:32     grade:A

 # ---------------------------------------------------------  # Nested dict --------------------------------------------------------------------------------------------------

students={
    'student1':{'name':'jayesh', 'age': 32},
    'student2':{'name':'ashika', 'age': 29}
}
print(students)  #o/p={'student1': {'name': 'jayesh', 'age': 32}, 'student2': {'name': 'ashika', 'age': 29}}


# Access nested dict elements
print(students['student2']['name'])  #o/p=ashika
print(students['student2']['age'])  #o/p=29

# Iterating over nested dict

for student_id,student_info in  students.items():
    print(f'{student_id}:{student_info}')
    for key,vallue in student_info.items():
        print(f'{key}:{vallue}')

#o/p=
'''
student1:{'name': 'jayesh', 'age': 32}
name:jayesh
age:32
student2:{'name': 'ashika', 'age': 29}
name:ashika
age:29
'''

 # ----------------------------------------- # Dictionary Comprehension  ------------------------------------------------------------------------------------------------------------------

# Dictionary Comprehension

square={x:x**2 for x in range(5)}
print(square) ##o/p= {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Conditional dict Comprehension

even={x:x**2 for x in range(10) if x%2==0}  
print(even) #{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}  square of even numbers

# --------------------------------------------------  Practical Implementation  ---------------------------------------------------------------------------------------------------------

#  use a dict to count the frequency of the elements in the list

num_list=[1,2,2,3,3,3,4,4,4,4]

freq={}  #Stores each number as a key and its frequency as the value.

for num in num_list:

    if num in freq: 
        freq[num]=freq[num]+1 #If the number (num) is already in the dictionary freq, it increments the count.

    else: 
        freq[num]=1 #If the number is not in the dictionary, it adds it with a count of 1.

print(freq)  #o/p= {1: 1, 2: 2, 3: 3, 4: 4}
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#merge 2 dictionaries into one

dict1={'a':1,'b':2}
dict2={'b':3,'c':4}

# **dict1- ** is keyword argument -any value that is present in the form of key value pair
merged_dict={**dict1,**dict2}
print(merged_dict) #o/p={'a': 1, 'b': 3, 'c': 4}

