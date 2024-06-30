# In-built functions...already exist in pythonnand we use
# eg. int(), str(), bool()

# Module Function...stored in files
# import math
# print(dir(math)) # pprint all math module functions and we can use

# can import specific function
from math import sqrt
print (sqrt(16))

# can use all functions
from math import * #can use all functions
print (sin(90))


# #user defined function
# syntax: def function_name(parameters):

def print_sum (first, second):
    print (first + second)

print_sum (2,4)

# can define any parameter like second = 3 and if only one parameter is aded as input second one os by default taken as 3
