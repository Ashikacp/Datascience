### Example 1: Temperature converter
# define a function to convert temperature b/w Fahrenheit (°F) and  Celsius (°C) 

def tempConverter(temp, unit):
    if unit == 'C':
        return temp * 9/5 + 32    #Temperature in(°F) = (Temperature in (°C) * 9/5) + 32. 
    elif unit == 'F':
        return (temp - 32) * 5/9  #Temperature in(°C) = (Temperature in(°F) - 32) * 5/9.
    else:
        return None

print(tempConverter(25, 'C'))  #o/p= 77
print(tempConverter(77,'F'))  #o/p= 25
#---------------------------------------------------------------------------------------------------------------------------------------------

## Example 2: Password strength checker

def is_strong_pwd(password):
    if len(password)<8:
        return False
    if not any (char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any (char in '!@#$%^&*()_+' for char in password):
        return False
    return True
    

print(is_strong_pwd("1234"))    # o/p= False
print(is_strong_pwd("Vambz!234"))  #o/p= True

#----------------------------------------------------------------------------------------------------------------------------------------

## Example 3 : Calculate the total cost of items in a shopping cart 


def calculate_total_cost(cart):
    total_cost =0
    for item in cart:
        total_cost+=item["price"]*item["quantity"]
    
    return total_cost

# cart data

cart = [
    {"name":"apple", "price":0.5 ,"quantity":4 },
    {"name": "banana","price":0.3,"quantity":6},
    {"name":"orange","price":0.7,"quantity":3}
]
print(calculate_total_cost(cart))  # o/p= 5.8999999999999995

#----------------------------------------------------------------------------------------------------------------------------------------

#Example 4: check if a string is palindrome or not

def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1] #reverse of string

print(is_palindrome("A man a plan a canal panama"))  #o/p =True
print(is_palindrome("hello"))   #o/p =False


#----------------------------------------------------------------------------------------------------------------------------------------
#Example 5: factorial of a number using recurssion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)     # we r calling the same function inside a function.it is called recurssion

print(factorial(5))   # o/p=  120
#----------------------------------------------------------------------------------------------------------------------------------------
# Example 6: A function to read a file and count freq of each word

import string
def count_freq_word(file_path):
    word_count ={} # empty dict to count the freq of each word

    with open(file_path,'r') as file:
        for line in file :
            words=line.split()
            #print(words)  #['Hello', 'my', 'name', 'is', 'Ashika', 'ashika']
            for word in words:
                word = word.strip(string.punctuation).lower()
                print(word) #o/p= hello my name is Ashika ashika
                word_count[word] = word_count.get(word, 0) + 1

    return word_count



file_path ='/Users/ashikacherikkaparambath/Desktop/Datascience/PythonNotes/3-functions/sample.txt '
word_freq=count_freq_word(file_path)
print(word_freq)   #o/= {'hello': 2, 'my': 1, 'name': 1, 'is': 1, 'ashika': 2, 'how': 1, 'are': 2, 'you': 2, 'where': 1}

#----------------------------------------------------------------------------------------------------------------------------------------

# Example 7: Validate email address

import re

def is_valid_email(email):

    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    return re.match(pattern, email) is not None

# Calling the function
print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))  # Output: False
