# Expense Manager

## Introduction
- This Expense Management Application is a web-based platform designed to help users manage their expenses efficiently. Built with Django and Django REST Framework, it offers a user-friend interface for tracking and organizing expenses.
- Skills: Python, Django, Django REST Framework, HTML, CSS, Git.
- You can check the Python OOP version [here](https://github.com/quynhnle135/expense-management-oop).

## Features
* User Account Management: Users can create an account, log in, and log out, ensuring that each user's data is private and secure.
* Expense Management: Users can easily add, update, and delete expenses. The application calculates and displays the total expense amount for quick reference.
* Search Functionality: Users can search for expenses by card, category, notes, date, and amount.

## Installation

1. Clone the repository: ```git clone https://github.com/quynhnle135/expense-manager.git```
2. Navigate to the project repository: ```cd expense-manager```
3. Install the required dependencies: ```pip install -r requirements.txt```
4. Run the server: ```python3 manage.py runserver```

## Screenshots
* Register an account
![expense-app-1.png](expense-app-screenshots%2Fexpense-app-1.png)

* User login
![expense-app-2.png](expense-app-screenshots%2Fexpense-app-2.png)

* User starts with an empty expense list
![expense-app-3.png](expense-app-screenshots%2Fexpense-app-3.png)

* Add an expense
![expense-app-4.png](expense-app-screenshots%2Fexpense-app-4.png)

* After adding some expenses.
![expense-app-5.png](expense-app-screenshots%2Fexpense-app-5.png)

* View expense's detail
![expense-app-6.png](expense-app-screenshots%2Fexpense-app-6.png)

* Delete an expense
![expense-app-13.png](expense-app-screenshots%2Fexpense-app-13.png)

* Search for expenses with card X1
![expense-app-7.png](expense-app-screenshots%2Fexpense-app-7.png)

* Search for expenses with card Amex
![expense-app-8.png](expense-app-screenshots%2Fexpense-app-8.png)

* Search for expenses with category Coffee
![expense-app-9.png](expense-app-screenshots%2Fexpense-app-9.png)

* Search for expenses with notes "reload"
![expense-app-10.png](expense-app-screenshots%2Fexpense-app-10.png)

* Search for expenses spent on Nov 23, 2023
![expense-app-11.png](expense-app-screenshots%2Fexpense-app-11.png)

* Search for expenses with amount $20
![expense-app-12.png](expense-app-screenshots%2Fexpense-app-12.png)

---

## API Features
- User-Specific Data Management: Every user can manage their own expense records, with each user's data kept private and secure.
- Create and Manage Expenses: Users can add new expenses, view their past expense records, update details, or delete records as needed.
- Search and Filter Capabilities: Users can easily find expenses based on various criteria such as card type, category, notes, date, and amount.
- Secure Access: All endpoints require user authentication, ensuring that data is protected and only accessible by the respective user.
- You can use ```curl``` to interact with the API or view it on your web browser because Django REST Framework provides a browsable API, which is a user-friendly web interface that allows users to interact with API directly.

## Endpoints
* List expenses: GET /api/expenses/
* Create expenses: POST /api/expenses/
* Retrieve expenses: GET /api/expenses/\<int:id>/
* Update expenses: PUT /api/expenses/\<int:id>/
* Delete expenses: DELETE /api/expenses/\<int:id>/

## Screenshots
* View all expenses
![expense-api-1.png](expense-api-screenshots%2Fexpense-api-1.png)

* Create new expenses
![expense-api-2.png](expense-api-screenshots%2Fexpense-api-2.png)

* View expense's detail
![expense-api-3.png](expense-api-screenshots%2Fexpense-api-3.png)

* Filter and search functionalites
![expense-api-4.png](expense-api-screenshots%2Fexpense-api-4.png)

* Expenses retrieved after filtering with card name "amex"
![expense-api-5.png](expense-api-screenshots%2Fexpense-api-5.png)