#!/usr/bin/env python
# coding: utf-8

# ### Homework 1
# 
# Skim this Homework before you do your reading assignments. It will help focus your attention. 
# 
# Provide written answers to questions with a `#comment`. 
# 
# Answer the following question **first**. The rest may be completed in any order.

# 1. How can you get more information about a function or an object from inside a jupyter cell? 

# In[ ]:


#comment To obtain more information about a function, press and hold the Shift + Tab keys until a box appear with function information


# 2. How can you determine the data type of an object? 

# In[ ]:


#comment. By using the function type()


# 3. Assign a variable named `foo` and give it a value of `'bar'`. Oh, and what is assignment?

# In[ ]:


#comment foo = 'bar' . Assignment refers to designating a meaning to variables via some value. Variable on the left = the value to the right


# 4. What is a data structure in another language that is not built into python? Does python have a similar data structure that may serve the same purpose? 

# In[ ]:


#comment. The array data structure is not built into python, but list is a similar data strutucure with the same purpose.


# 5. You have an assortment of items you will need to keep track of. What would be a good data structure to keep them in? Provide an example.

# In[ ]:


#comment. A dictionary structure will help to keep track of this. 
#comment. Example Name, Amount in an account, who has access 


# 6. You have an assortment of names and telephone numbers. What might be a good data structure to keep them in? Show an example. 

# In[ ]:


#comment. A dictionary structure will be the most ideal. 
#comment. Ex. p_dict: = {'Alex':6151234567, 'Amy':6152347765, 'Brittanie':9378564431}


# 7. You need to create a copy of an important list and alter the copy. Why is the following code a bad idea? 

# In[45]:


list1 = [1,2,3]
list2 = list1
list2[0]= 9


# In[46]:


#comment the code is bad because it will alter list one.


# 8. What is truthy and falsey? Provide a list example and a string example. 

# In[ ]:


#comment With use of Boolen, truthy and falsey are values that evaluate to truth or false, respectively. 


# 9. What is the difference between a dynamically typed and statically typed language? 
# 
# Which one is python? 
# 
# When is that a good thing? 
# 
# When is that a bad thing? 

# In[ ]:


#comment. A dynamically typed language is one where the program only type checking as a code is ran, but the value of a variable can change throughout its course. Whereas, a statically typed language are checked without running the program. Python is a dynamically typed language. This is good to use when you the variables will change over its lifetime. This is bad when you have a in depth code and wont be made aware of errors until aftr the program is ran.


# 10. Here is a [link](https://docs.python.org/3/library/functions.html) to the python `built-in functions`. Choose 2 and give an example of how to use them. 

# In[ ]:


#Hex
print (hex (30))
#Bin
print (bin (30))


# 11. I need to know if an integer is odd or even. What `operator` might help me do that? 

# In[ ]:


#comment. The modulo operator is beneficial for determining if a number is odd or even. If you set the modulo divisible by 2 and want 0 remainder, then the value is even, if this statement is true.


# 12. What is an operator? 

# In[ ]:


#comment Operators are symbols intended to carry out a specific arithmetic function or logical function


# 13. What is a data type in another language does not exist in python? Does python have a similar data type

# In[ ]:


#comment. An array is a data type that does not directly exists in python. Lists are similar data type to arrays.


# 14. What is a python expression? And what does it evalute to? 

# In[ ]:


#comment. An expression is a combination of variables, values, and operators. The expression is evaluated to produce the results.


# 15. Provide an expression that evaluates which variable is greater. (Hint: you can just test them and don't need to say which is greater)

# In[38]:


foo = 23
bar = 48
print (foo == bar)


# 16. Provide an if statement (inside the provided for loop) that prints 'even' if the number is even, 'odd' if the number is odd and 'three' if the number is 3.

# In[ ]:


my_list = [1,2,3,4,5,6,7,8,9]

for i in my_list:
   
    if (my_list%2 == 0):
        print ('even')
    else:
        print ('odd')
        print ('three')
    #Be sure to indent the statement
    #And delete the word 'pass'


# 17. What is the equal operator? `# comment it out`
# And show an example of how it is used. 

# In[ ]:


#comment. An equal operator is = . Example 2 = 2


# 18. What is the less than equal to operator? And show an example of how it is used. 

# In[ ]:


#comment. Less than equal to operator is <= Example 3 <= 5


# 19. What is the modulo remainder operator? And show an example of how it is used. 

# In[ ]:


#comment. A modulo operator is % . Example  11%5 = 1


# 20. What is the floored division operator? And show an example of how it is used. 

# In[ ]:


#comment. The floored division operator is // Example. 11//5 = 2


# 21. Why is this assigment not a good idea? (Hint: focus on the word hex)

# In[5]:


hex = 'some text value'
#comment. Hex is used to convert integers to hexidecimal. It cannot convert a text value.


# 22. Why does the following give an error? Show an example of how to fix it.

# In[ ]:


2cars = ('Ferarri', 'Mustang')


#comment.The error appears because the variable starts with a number. 


# In[ ]:


T2cars= ('Ferarri', 'Mustang')


# 23. Why does this if statement evaluate to true? 
# You will see this shortcut a lot and it can be confusing as to what is going on. 

# In[7]:


some_list = ['fizz','buzz',1,{'key':'value'}]

if some_list:
    print('Hooray!')


# In[ ]:


#comment. It evaluates to true since there are values in the list


# 24. Write an expression that adds two numbers. 

# In[4]:


# comment print (2 + 2)


# 25. Write an expression that divides two numbers. 

# In[ ]:


#comment print (2/2)


# 26. Write an expression that raises one number to the power of 3. 

# In[ ]:


#comment print (2**3)


# 27. You've been asked to do some semi-avanced mathematics and create a report. What module might you import to help make your job easier? 
# 
# Import this module below. (Hint: It's part of the Python Standard Library)

# In[ ]:


#comment. Import math


# 28. How can you change `my_var` form an `int` to a `str`?

# In[35]:


my_var = 42
my_var= str(my_var)
type(my_var)


# In[ ]:





# 29. Slice `some_string` to only include the words `lazy`. 

# In[21]:


some_string = "The quick brown fox jumped over the lazy dog."
print(some_string[36:40])


# In[15]:





# 30. Assign a new variable `sport` to the 3rd element in the list.

# In[13]:


my_favorite_teams= ['Chiefs', 'Cardinals', 'Blues', 'Lakers','Manchester United', 'Couch Surfing']


# In[14]:


my_favorite_teams= ['Chiefs', 'Cardinals', 'Blues', 'Lakers','Manchester United', 'Couch Surfing']
sport = my_favorite_teams[2]

print (sport)


# **Optional Questions:**

# Write a function that takes in a number and doubles it. 

# In[ ]:


x * 2


# What is the use case for the `dir()` method? 

# In[ ]:


#comment. dir() tell us attributes/properties and methods of a code


# Reverse the following string using only slicing methods.

# In[17]:


irreversible = "Can you reverse me?"
irreversible[len(irreversible)::-1]


# In[ ]:





# In[ ]:





# In[ ]:




