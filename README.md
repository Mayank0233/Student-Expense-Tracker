# Student-Expense-Tracker
A simple Python-based Student Expense Tracker that helps students manage their daily expenses, set budgets, track spending, and calculate their remaining balance. Designed to make money management easy and efficient for students.


Student Expense Tracker

Description:

It is a lightweight console application focused on modularity to track student's expense. The software is designed to help the users keep track of the spent and remaining amount of money, store the data on the disk, and categorize into Food, Books, Travel,Other Categories.

Overview:

Student Expense Tracker is applicable to manage student's expenses. It can help them avoid using complex spreadsheet software and replace it with an easy-to-use command-line interface. Student Expense Tracker assits the users in tracking the money they spend on different expenses and the amount of money they have left. The application allows the users to store their data in files, define the categories, and manage their budgets.

This application was built using modular programming principles, single_responsibility Python modules and orchestrated by the main file.

Features:

Customizable budget setting on start-up. The users can set the desired amount of money that they want to track

Categorization of expenses. It defines the expenses into several categories to help see where the money was spent.

live tracking of money. Student Expense Tracker allows spending and remaining amounts of money to be known

Storage system. The application can save the user's data in files

Student Expense Tracker is written in Python. Thus, the users will not have to install any additional libraries separately.


Technologies and Tool Used:

Language Python 3.8+
Standard Libraries: os(file system verification)
Data Storage: Plain txt file (expenses.txt)
Version Control: Git and GitHUB

Project Structure:

student_expense_tracker/
|
|-- inputs.py  #Module1. Direct user input collection
|-- Categories.py #Module2. Category mapping and selection
|-- calc.py #Module3. Arithmetic and Balance calculation
|-- Storage.py  #Module4. File Operation
|-- display.py #Module5. console formatting and receipt
|-- main.py  #Main application entry point
|-- statement.md #Project problem statement and design rationale
|--README.md #Project documentation and setup guide

STEP TO INSTALL AND RUN THE PROJECT:

Make sure to install python 3.8 or higher in your computer
Clone or download the repository or download the .py files into a local directory
This no need of installing any extra external packages.
Running the application 
Type in your terminal python main.py

Intructions for testing:

Test case1 : Initial launch and Budget Setup

1. Run python main.py.
2. When prompted Enter you total budget 
Enter your respected budget for futher process
And press Enter
3. Expected Result: The program accepts the input and display the main menu
   - Add
   - View
   - Balance
   - exit

Test case2 : Reading an Empty Log File 

1. If running for the first time(no expenses.txt)
choose option 2

2. Expected Result: The console should safely output NO Expenses found!
without raising an unhandled FileNOtFoundError .


Test case3. Adding Expenses and Auto-Categorization

1. Choose option 1
2. When prompted Enter Item Name: Enter Notebook
3. Select Category 2 (Books)
4. Enter cost: 200
5. Expected Result: A receipt confirmation is printed:
         Saved: Notebook | Books | 200

Test case4. Verifying Storage Persistence

1. Choose option 2 from the menu
2. Expected Result: The list output
3. A local file name expenses.txt should now exist in your project folder with the corresponding entry

Test case5. Balance Calculation

1. Choose option 3 from the menu
2. Expected Result: Output Display the remaining balance 
Budget - Spent = Left Balance

Test case6. Graceful Program Exit

1. Choose option 4 from the menu 
2. Expected result: The console print Bye! and terminates with exit code 0 
RUN the program again; your balance and records will be presevered in expenses.txt











                        [ STUDENT / CONSOLE ]
                                 │
                 (1) Budget input: "100.0"
                                 ▼
                     ┌───────────────────────┐
                     │       inputs.py       │ ── float("100.0")
                     └───────────┬───────────┘
                                 │ budget: 100.0 (float)
                                 ▼
                     ┌───────────────────────┐
                     │        main.py        │
                     │  total = 0.0 (float)  │
                     └───────────┬───────────┘
                                 │
     ┌───────────────────────────┴───────────────────────────┐
     │ [OPTION 1: ADD EXPENSE]                               │ [OPTION 3: CHECK BALANCE]
     ▼                                                       ▼
┌─────────────────────────┐                             ┌─────────────────────────┐
│        inputs.py        │                             │         calc.py         │
│ "Notebook", "2", "15.5" │                             │ remaining(100.0, 15.5)  │
└────────────┬────────────┘                             └────────────┬────────────┘
             │                                                       │
             ├──────────────────────┐                                │ rem: 84.5 (float)
             │ "Notebook", "15.5"   │ choice: "2"                    ▼
             ▼                      ▼                           ┌─────────────────────────┐
┌─────────────────────────┐ ┌─────────────────────────┐        │       display.py        │
│       inputs.py         │ │      categories.py      │        │ balance(100, 15.5, 84.5)│
│ item: "Notebook" (str)  │ │ dict lookup: "2"        │        └────────────┬────────────┘
│ cost: 15.5 (float)      │ │ cat: "Books" (str)      │                     │
└────────────┬────────────┘ └───────────┬─────────────┘                     ▼
             │                          │                       "Budget: 100.0 |
             └───────────┬──────────────┘                        Spent: 15.5 | Left: 84.5"
                         │
                         ▼
             ┌─────────────────────────┐
             │       storage.py        │
             │ save("Notebook",        │
             │      "Books", 15.5)     │
             └───────────┬─────────────┘
                         │ formatted text: "Notebook,Books,15.5\n"
                         ▼
             ┌─────────────────────────┐
             │      expenses.txt       │ ◄── Persistent Flat File on Disk
             └─────────────────────────┘
