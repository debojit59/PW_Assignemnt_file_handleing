#!/usr/bin/env python
# coding: utf-8

# In[3]:


# How can you open a file for writing in Python and write a string to it


# In[5]:


file_name="Test_file"+".txt"
file=open(file_name,"w")
file.write("My Name is Debojit")
file.close()


# In[9]:


file=open(file_name,"r")
file.readlines()


# In[10]:


#Write a Python program to read the contents of a file and print each li


# In[18]:


file_name="Test_file"+".txt"
file=open(file_name,"w")
file.write(" My Name is Debojit.\n"
          " My name is Don. \n"
        " My name is Khan")
file.close()
file=open(file_name,"r")
for read in file:
    print(read)


# In[23]:


#How would you handle a case where the file doesn't exist while trying to open it for reading


# In[24]:


try:
    file_name = "Python_file"
    file = open(file_name, "r")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' is not available.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# In[25]:


# Write a Python script that reads from one file and writes its content to another file


# In[36]:


file_name="file_1"
file=open(file_name+".txt","w")
file.write(" My Name is Debojit.\n"
          " My name is Don. \n"
        " My name is Khan")
file.close()


# In[42]:


new_file=open("file_2.txt","w")
file=open("file_1"+".txt","r")
for read in file.readlines():
    new_file.write(read)
new_file.close()
    


# In[46]:


new_file=open("file_2.txt","r")
for i in new_file.readlines():
    print(i)


# In[49]:


#How would you catch and handle division by zero error in Python


# In[ ]:


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Please enter valid integers.")

 Write a Python program that logs an error message to a log file when a division by zero exception occurs
# In[1]:


import logging

# Configure logging to log error messages to a file
logging.basicConfig(
    filename="error_log.log",
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        logging.error(f"Division by zero error: {e}")
        print("Cannot divide by zero. Please check the inputs.")

# Test the function
divide_numbers(10, 0)


# In[2]:


#How do you log information at different levels (INFO, ERROR, WARNING) in Python using the logging module


# In[3]:


import logging

# Configure the logging system
logging.basicConfig(
    filename='example_log.log',
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Logging at different levels
logging.debug("This is a DEBUG message: Useful for troubleshooting.")
logging.info("This is an INFO message: Program started successfully.")
logging.warning("This is a WARNING message: Disk space running low.")
logging.error("This is an ERROR message: Failed to open file.")
logging.critical("This is a CRITICAL message: Application crash imminent.")


# In[4]:


#Write a program to handle a file opening error using exception handling


# In[ ]:


import logging

# Configure logging to log error messages
logging.basicConfig(
    filename="file_error_log.log",
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def open_file(filename):
    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {e}")
        print("Error: The file does not exist. Please check the file name or path.")
    except PermissionError as e:
        logging.error(f"PermissionError: {e}")
        print("Error: You do not have permission to access this file.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred.")

# Test the function with a non-existent file
open_file("non_existent_file.txt")


# In[51]:


#9  How can you read a file line by line and store its content in a list in Python


# In[57]:


new_file=open("file_2.txt","r")
lines=new_file.readlines()
list_of_lines=[line.strip() for line in lines]
print(list_of_lines)


# In[5]:


#How can you append data to an existing file in Python


# In[6]:


filename = "example.txt"

# Create the file and write initial content
with open(filename, 'w') as file:
    file.write("This is the initial content.\n")
print("File created and initial data written.")


# In[7]:


# Append data to the file
with open(filename, 'a') as file:
    file.write("This is additional content added later.\n")
print("Data successfully appended to the file.")


# In[22]:


# Define a sample dictionary
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

student_name=input("Enter the name of the student")

try:
    student_number=student_scores.get(student_name)
    if student_number is None:
        raise KeyError("Student number is not found")
    print(f"Here is the score of the student named {student_name} : {student_number}")
except Exception  as e:
    print(e)


# In[24]:


#Write a program that demonstrates using multiple except blocks to handle different types of exceptionsF


# In[23]:


##### try:
    # User inputs for demonstration
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Attempt division
    result = num1 / num2
    print(f"The result of division is: {result}")

except ValueError:
    # Handle invalid integer input
    print("Error: Please enter valid integer numbers.")

except ZeroDivisionError:
    # Handle division by zero
    print("Error: Division by zero is not allowed.")

except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")


# In[25]:


#How would you check if a file exists before attempting to read it in Python


# In[ ]:


import os

file_path = "example.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
else:
    print("File does not exist.")


# In[27]:


#Write a program that uses the logging module to log both informational and error messagesF


# In[28]:


import logging

# Configure logging with a file handler and custom format
logging.basicConfig(
    filename='application.log',  # Log file name
    level=logging.DEBUG,  # Set logging level to capture all messages
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def divide_numbers(num1, num2):
    """Function to divide two numbers with logging"""
    logging.info(f"Attempting to divide {num1} by {num2}")
    try:
        result = num1 / num2
        logging.info(f"Division successful: {num1} / {num2} = {result}")
        return result
    except ZeroDivisionError as e:
        logging.error("Division by zero error occurred", exc_info=True)
        return "Error: Division by zero is not allowed"
    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)
        return "An unexpected error occurred"

# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = divide_numbers(num1, num2)
print(f"Result: {result}")


# In[29]:


# Write a Python program that prints the content of a file and handles the case when the file is empty


# In[31]:


def read_file(file_path):
    """Reads and prints the content of a file, handling empty file cases."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
            if content.strip():  # Check if content is non-empty after stripping whitespace
                print("File Content:")
                print(content)
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Input file path from the user
file_path = input("Enter the file path: ")
read_file(file_path)


# In[32]:


#Write a Python program to create and write a list of numbers to a file, one number per lineF


# In[33]:


def write_numbers_to_file(file_path, numbers):
    """Writes a list of numbers to a file, one number per line."""
    try:
        with open(file_path, "w") as file:
            for number in numbers:
                file.write(f"{number}\n")
        print(f"Numbers successfully written to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example list of numbers
numbers = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]

# Specify the file path
file_path = "numbers.txt"

# Write numbers to file
write_numbers_to_file(file_path, numbers)


# In[34]:


#How would you implement a basic logging setup that logs to a file with rotation after 1MB


# In[35]:


import logging
from logging.handlers import RotatingFileHandler

# Configure logging
log_file = "app.log"

# Create a logger
logger = logging.getLogger("RotatingLog")
logger.setLevel(logging.DEBUG)

# Create a handler that rotates logs after they reach 1MB
handler = RotatingFileHandler(
    log_file, maxBytes=1 * 1024 * 1024, backupCount=3  # 1MB per file, keep 3 backups
)

# Create a formatter and add it to the handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Sample log messages to demonstrate rotation
for i in range(10000):
    logger.debug(f"Debug log entry {i}")


# In[36]:


#Write a program that handles both IndexError and KeyError using a try-except block


# In[37]:


def access_data():
    my_list = [10, 20, 30]
    my_dict = {"Alice": 85, "Bob": 92}

    try:
        # Attempt to access an invalid list index
        print("Accessing list element:", my_list[5])

        # Attempt to access a non-existent dictionary key
        print("Accessing dictionary key:", my_dict["Charlie"])
        
    except IndexError:
        print("Error: List index out of range.")
    except KeyError:
        print("Error: Dictionary key not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
access_data()


# In[38]:


#How would you open a file and read its contents using a context manager in Python


# In[39]:


file_path = "example.txt"

# Use context manager to open and read file contents
try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except IOError:
    print(f"Error: Unable to read the file '{file_path}'.")


# In[40]:


#Write a Python program that reads a file and prints the number of occurrences of a specific word


# In[41]:


def count_word_occurrences(file_path, target_word):
    """Counts the occurrences of a specific word in a file."""
    try:
        with open(file_path, "r") as file:
            content = file.read().lower()  # Convert content to lowercase for case-insensitive matching
            words = content.split()  # Split content into words
            word_count = words.count(target_word.lower())
            print(f"The word '{target_word}' appears {word_count} times in the file.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Input file path and target word from the user
file_path = input("Enter the file path: ")
target_word = input("Enter the word to count: ")

# Count occurrences
count_word_occurrences(file_path, target_word)


# In[42]:


#How can you check if a file is empty before attempting to read its content


# In[43]:


import os

file_path = "example.txt"

# Check if the file is empty using os.stat().st_size
if os.path.exists(file_path) and os.stat(file_path).st_size == 0:
    print(f"The file '{file_path}' is empty.")
else:
    print(f"The file '{file_path}' has content.")


# In[ ]:


#Write a Python program that writes to a log file when an error occurs during file handling


# In[ ]:


import logging

# Configure logging to write to a file
logging.basicConfig(
    filename="file_handling_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def read_file(file_path):
    """Reads the content of a file and logs errors if they occur."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        logging.error(f"File not found: '{file_path}'")
        print("Error: The specified file does not exist.")
    e

