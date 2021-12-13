# Perform Operations Using Modules"

# import the math module and use help and dir to get information about its capabilities and attributes
import math
help(math)
print(dir(math)) # Узнать набор методов объекта

# Using the math module\n",
# Create a list with 5 numbers\n",
# Use the math module to find the square root of the numbers in the list\n",
# Use the math module to truncate the number 123.45\n",
# Use the math module to summarize the numbers in the list\n"

list1 = [2,4,6,8,10,12]
print("The square root of 9: ", math.sqrt(81))
print("Truncate 123.45: ", math.trunc(123.45))
print("Sum of the numbers in list1: ", math.fsum(list1))

# Help with the statistics module
# import the statistics module and use help and dir to get information about its capabilities and attributes
import statistics
help(statistics)
print(dir(statistics))

# Using the statistics module
# create a list that has 5 numbers
# Use the statistics module to find the average of the numbers
# Use the statistics module to find the median of the numbers
# Use the statistics module to find the standard deviation of the numbers

ages = [22,14,50,34,78,18,24]
print("Average age: ", statistics.mean(ages))
print("Median age: ", statistics.median(ages))
print("Standard Deviation: ", statistics.stdev(ages))

# Using the random module
# Also import the numpy module for this task
# Create a list with 10 numbers
# Use the random module to randomly rearrange the values in the list
# Use the random module to randomly choose 5 numbers from the list\n",
# Use the random module to generate a random number between 0 and 1\n",
# Use the random module to generate a random number between 1 and 100\n",
# Use the random module to generate a random even number between 1 and 1000\n",
# Use the random and numpy modules to create a list of 10 numbers that have a maximum of two decimal places\n"

##import random as ran, numpy as np
##list1 = [2,3,1,3,5,45,67,456,22,21,901,32,2,17]
##print("Random number between 0 and 1: ", ran.random())
##print("Random integer between 1 and 100: ", ran.randint(1,100))
##print("Random even number between 1 and 1000: ", ran.randrange(0,1001,2))
##print("Original list1: ", list1)
##print("Shuffle the values in list1: ", ran.shuffle(list1))
##print("Reshuffled list1: ", list1)
##print("Random list of 5 values from the list: ", ran.sample([2,3,1,3,5,45,67,456,22,21,901,32,2,17],5))
##prices = np.array([round(ran.uniform(20, 100),2) for _ in range(10)])
##print("Randomly generated array of 10 prices: ", prices)

# Using the os module
# Use os to get the current working directory
# Use os to create a new directory
# Use os to change the location to the new directory
# Use os to verify the new location on the file system
# Use os to change back to your original directory then verify your location again

import os
print("Current Working Directory is: ", os.getcwd())
# Create a new directory named dir1:
os.system('mkdir dir1')
#Change directory to dir:
os.chdir('dir1')
print("Current Working Directory is: ", os.getcwd())
#Go back to the parent directory:
os.chdir('..')
print("Current Working Directory is: ", os.getcwd())

# Using the sys module
# Use sys to find the python version
# Use sys to find the location of the python executable
# Use sys to list all folders in the path environment variable
# Use sys to find out what operating system you are running on
# Use sys to find the number of installed modules on your system

import sys
print("Python version: ", sys.version)
print("Operating System Path: ", sys.path)
print("Location of Python executable: ", sys.executable)
print("Platform: ", sys.platform)
print("Number of modules installed: ", len(sys.modules))

# Using the time module
# Use time to show the current date and time
# Use time to show only the current time without the date
# Use time to pause your session for 5 seconds

import time
print("Date and time: ", time.ctime())
print("Structured date and time: ", time.localtime())
print("Pause for 5 seconds: ")
time.sleep(5)
print("End.")

# Use the datetime module\n",
# Use datetime to show the current date and time\n",
# Use datetime to show only the current date without the time\n",
# Use datetime to show the date 60 days from today\n"

import datetime
datestring = datetime.datetime.today().strftime("%Y-%m-%d_%H:%M:%S")
dateplus60 = datetime.datetime.now() + datetime.timedelta(days=60)
now = datetime.datetime.today()
print("Today's date: ", now)
print("Date formatted as a string: ", datestring)
print("Add 60 days to today's date: ",dateplus60)

# Compare list and numpy array.  If necessary, install numpy on your system: \"pip install --user numpy\"\n",
# Create a list with 5 numbers\n",
# Append a 6th number to the list\n",
# Create a numpy array with 5 numbers\n",
# Append a 6th number to the array\n",
# Multiply the list and array by 2 and notice how the results differ.\n"

import numpy as np
list1 = [1,2,3,4,5]
list1.append(6)
print('list1: ',list1)
array1 = np.array([1,2,3,4,5])
array1 = np.append(array1,[6])
print('array1: ',array1)
print('list1 * 2 is: ',list1 * 2)
print('array1 * 2 is: ',array1 * 2)






































