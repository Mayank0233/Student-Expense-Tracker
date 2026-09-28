# Program Statement : Student Expense tracker

#  Overview
Managing daily personal finances is a common challenge for student. Without a structured method to log expenditures, students often exceed their budget.
# Introduction 
most of us struggle to keep track of our expenses and without having a proper accounting of our daily expenditures, the students can easily go out of budget and not have a view of where their enpenses are going.

This project aims to address the problem and provide a convenient budgeting tool for the tracking of daily school-related expenses in python.

# Features
Some of the features which will be implemented in order to achieve the goal are listed below:
Allow users to convenintly enter and view their daily expenses along with tags for categorization
provide dynamic budget tracking based on the user input value
save all the expenses in a local file in order to keep an up-to-date balance
structure the software in a way which demonstrates the principles of the object-oriented programming by dividing the program's functionalities into several modules

# Implementation Overview
The project would be structured into five seperate files and one directory for storing the generated files with the following purpose:
| File / Directory | Purpose |
|:--- |:--- |
| `inputs.py` | Define logic related to the inputs such as entering the desired budget, item name, item price, selection from menu options etc. |
| `categories.py` | Define several categories for better organization and budget tracking such as `FOOD`, `BOOKS`, `TRAVEL`, `OTHER` etc. |
| `calc.py` | Define logic related to the calculations such as calculating the budget balance, overall spent amount etc. |
| `storage.py` | Define logic related to the file storage such as saving the current state of the program into a file, loading the data from a file |
| `display.py` | Provide logic related to display such as printing the menu options, displaying receipts, budget tracking etc. |
| `main.py` | Entry point of the application |

# Additional Notes
The budget value can be changed at the start of the program
The program will recognize the input value and store them into the appropriate categories
The program does not require any external library and can be run simply executing the 'main.py' file
