# set is an unordered collection of unique elements enclosed in curly braces.

#create a Set

my_set={1,2,3,4,5,1}
print(my_set)  #o/p= {1, 2, 3, 4, 5} duplicates elements will be removed
print(type(my_set))  #o/p= <class 'set'>

#create empty set
my_empty_set=set()
print(my_empty_set) #o/p= set()  ,empty set
# ---------------------------------------------------------   #TYPE conversion  -----------------------------------------------------------------------------

my_set=set([1,2,3,4,5]) #list into a set
print(my_set) #o/p= {1, 2, 3, 4, 5}

# --------------------------------------------------------   #Basics SET operations  ---------------------------------------------------------------------------------------------------


# adding and removing elements

my_set={1,2,3,4,5,6}
my_set.add(7)
print(my_set) #o/p={1, 2, 3, 4, 5, 6, 7}

my_set.remove(3)
print(my_set) #o/p= {1, 2, 4, 5, 6, 7}

my_set.discard(10)  #remove an element from a set if it is a member .here 10 is not a member in the set.
print(my_set) # o/p= {1, 2, 4, 5, 6, 7}

#pop method  -removes a random item from the set.
removed_element=my_set.pop()
print(removed_element) #o/p=1  first element is removed
print(my_set) #o/p= {2, 4, 5, 6, 7}

#clear all the elements
my_set.clear()
print(my_set)  #o/p=set()  ie,a empty set
# ---------------------------------------------------------   # Set membership test   --------------------------------------------------------------------------------------------------
my_set={1,2,3,4,5}
print(3 in my_set)  #o/p=TRUE
print(10 in my_set)  #o/p=False
# ---------------------------------------------------------    #MATHEMATICAL operation --------------------------------------------------------------------------------------------------

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

# Union   -combining everything

union_set=set1.union(set2)
print(union_set) #o/p={1, 2, 3, 4, 5, 6, 7, 8, 9}

#Intersection - common elements in the both set

intersection_set=set1.intersection(set2)
print(intersection_set) #o/p={4, 5, 6}

#intersecte and update the set1
set1.intersection_update(set2)
print(set1) #o/p={4, 5, 6} ie, set 1 is updated with intersected values

print(set2) #o/p= {4, 5, 6, 7, 8, 9} ie set2 is not changed

#Difference
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

print(set1.difference(set2))  #o/p= {1, 2, 3} removed common elements from set1 and return remaining elements in set1
set1.difference_update(set2)
print(set1) #o/p= {1, 2, 3} ie set1 is updated with the remaining value

# Symmetric difference

print(set1.symmetric_difference(set2)) #o/p= {1, 2, 3, 4, 5, 6, 7, 8, 9}  unique elements from both the sets are combined remaining were removed
set1.difference_update(set2) 
print(set1) #o/p={1, 2, 3}
# -----------------------------------------------------------     Set methods ------------------------------------------------------------------------------------------------

# Set methods

set1={1,2,3,4,5}
set2={3,4,5}

#is subset  - all elements in set1 is available in set2 or not
print(set1.issubset(set2)) #o/p=False

#super set -
print(set1.issuperset(set2)) #o/p=True 3,4,5 is available in both

# -----------------------------------------------------------------------------------------------------------------------------------------------------------


#count unique words in text

text="in this tutorial we are discussing about the importance of the set datastructure"
word= text.split()
print(word)  #o/p= ['in', 'this', 'tutorial', 'we', 'are', 'discussing', 'about', 'the', 'importance', 'of', 'the', 'set', 'datastructure']
print(len(word)) #o/p=13

##convert list of word to set to get the unique words

unique_word=set(word)
print(unique_word) #o/p={'this', 'tutorial', 'datastructure', 'are', 'discussing', 'in', 'about', 'set', 'of', 'importance', 'the', 'we'}
print(len(unique_word)) #o/p=12
