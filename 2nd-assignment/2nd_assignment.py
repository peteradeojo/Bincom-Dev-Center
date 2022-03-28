#!python

import os, re

# Question 1
# Create a text file that has your full name, and write code to read it 
# and extract first name, middle name and last name.

with open('full_name.txt', 'r') as f:
  # name_regex = re.compile(r'/[a-zA-Z-]{1,}/')
  name_regex = re.compile('([a-zA-Z-]+){1,}')
  text = f.read()
  matches = name_regex.findall(text)
  print(f"Firstname: {matches[0]}")
  print(f"Middlename: {matches[1]}")
  print(f"Lastname: {matches[2]}")


# Question 2
# Using the library os, print your local file path on screen.
print(os.path.abspath('.'))

# Question 3
# Extraction of baby name from file using regex 
# not using built-in libraries, 
# create a sort algorithm, implement binary search.

names = []
# Read baby names file
with open('baby2008.html', 'r') as f:
    # Regex for baby names inside td elements
    baby_name_regex = re.compile(r'<td>\d+</td><td>(\w+)</td><td>(\w+)</td>')
    text = f.read()
    matches = baby_name_regex.findall(text)
    for match in matches:
        # Add baby names to array
        names.append(f"{match[0]} {match[1]}")

# Sort array alphabetically
names.sort()

# Binary search function
def binary_search(arr, min, max, x='Boluwatife Ade-Ojo'):
    if max > min:
        mid = max + min

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, min, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, max, x)
    else:
      return -1

print(binary_search(names, 0, len(names) -1, 'Boluwatife Ade-Ojo'))
