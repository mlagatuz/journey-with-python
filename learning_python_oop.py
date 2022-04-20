'''
Created on Apr 16, 2022

@author: mlagatuz

Coming from C-based programming languages (C/C++, Java), this is my attempt on
learning the differences in OOP versus languages I've worked in

"Account" and "Time" modules came from "Python Fundamentals LiveLessons" by Paul Deitel,
and can be accessed by going to his github repo:

https://github.com/pdeitel/PythonFundamentalsLiveLessons.git

'''
#from python_file import python_class
from account import Account
from decimal import Decimal
from timewithproperties import Time

my_account_object = Account('Mark Lagatuz', Decimal('50.00'))
print(f'{type(my_account_object)}')
print(f'{my_account_object.name}')
print(f'{my_account_object.balance}')
my_account_object.deposit(Decimal("25.25"))
print(f'{my_account_object.balance}')
# my_account_object.deposit(Decimal("-225.25"))

# Class Definition

# class ClassName:
#    """ Normally place doc-string here """

#    class attributes : defined/declared outside of all methods
#                       persistent across all instances of class objects
#                       similar to 'static' in C++/Java?

#    CONSTANTS: naming convention, upper case to signal variables are constants

#    initializing method, similar to Java constructor classname()
#    'this' in c-based languages == 'self' in Python
#    def __init__(self, ...):

#    instance variables, declaration outside of constructor (Java/C++)
#    instance variables, inside class definition, inside methods (Python)
#    self.attribute 

#    end_init_method

#    'self': when an instance method is called, the calling object will implicitly
#    receive a reference to an object, which is itself ('self')
#    def method(self, ...)

#    end_method

# Encapsulation is not direct in Python, must use naming conventions
# _variable/method_ name == internal use only ... similar to 'private' in C++/Java

# @property == creates properties (@ notation is a decorator), attribute-style access
# if not creating properties, then 'self.attribute = value', otherwise
# properties are searched within the class (for 'setters'/'getters')

# by default, @property is 'getter', read-only property
# assign.setter for r/w capability  

# __repr__ : used for object evaluations

# __str__ : similar to Objects toString() functions in C++/Java
#           presents objects in string format

# _variable_name : alerts developers/users of code, this is a 'private' variable

# keyword arguments
wake_up = Time(hour=6, minute=30)
print(f'{type(wake_up)}')
print(f'{wake_up}')
wake_up.hour # access properties
wake_up.set_time(hour=7, minute=45) # setters in Java/C++
print(f'{wake_up}')
wake_up.hour = 6
print(f'{wake_up}')
#wake_up.hour = 100 # properties can define validity checking code