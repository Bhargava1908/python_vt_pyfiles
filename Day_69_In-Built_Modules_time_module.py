"""
In Built Modules in Python

Examples:
1. time
2. os
3. random
4. math
5. datetime
6. re
7. sys
"""
# Time Module
"""
Getting the current time:
time.time(): Returns the current time as a floating-point number representing the seconds since the epoch (January 1, 1970, 00:00:00 UTC for most systems). 
time.ctime(): Converts a time expressed in seconds since the epoch to a string representing local time. If no argument is provided, it returns the current local time.
Pausing program execution:
time.sleep(seconds): Suspends the execution of the current thread for the specified number of seconds. 
Formatting and parsing time:
time.strftime(format, t): Converts a struct_time object (or a tuple representing time) to a string according to the specified format directives.
time.strptime(string, format): Parses a time string according to a specified format and returns a struct_time object.
Working with struct_time objects:
The time module often uses struct_time objects to represent time data in a structured way (e.g., year, month, day, hour, minute, second). These objects can be accessed by index or by attribute name. 
Example usage:
Python

import time

# Get current time in seconds since the epoch
current_seconds = time.time()
print(f"Seconds since epoch: {current_seconds}")

# Get current local time as a formatted string
local_time_string = time.ctime()
print(f"Current local time: {local_time_string}")

# Pause execution for 2 seconds
print("Pausing for 2 seconds...")
time.sleep(2)
print("Resumed.")

# Format a specific time
# Example: a struct_time object for a specific date and time
# (You can get this from other time functions like time.localtime())
specific_time_struct = time.localtime(1678886400) # Example timestamp
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", specific_time_struct)
print(f"Formatted time: {formatted_time}")
"""
import time
# from time import time, sleep
# time - it will give the unix timestamp
t1 = time.time()
print(type(t1))
print(t1)

for i in range(5):
    # time.sleep(3)
    print(i, end=' ')

t1 = time.ctime()
print(type(t1))
print(t1)

t1 = time.strftime("%d-%m-%Y %H:%M:%S")
print(t1)

t1 = time.strftime("%m/%d/%y %H:%M:%S")
print(type(t1))
print(t1)

t1 = time.strptime("15-10-2025 09:40:00", "%d-%m-%Y %H:%M:%S")
print(type(t1))
print(t1)


t1 = time.strptime("10/15/25 09:40:00", "%m/%d/%y %H:%M:%S")
print(type(t1))
print(t1)

print(time.gmtime(0))
obj = time.localtime()
print(obj)
