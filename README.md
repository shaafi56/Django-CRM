**Overview**

This Django CRUD (Create, Read, Update, Delete) application is a complete user management system that allows you to:

Create new user records

Read and view existing records

Update existing user information

Delete records from the system

**Key Features**

1. User Management
Add new users with comprehensive details including:

First and last name

Email address

Phone number

Complete address (street, city, state, zipcode)

View all users in a clean, sortable table format

Edit existing user information

Remove users from the system

2. Authentication System
   
Secure user login/logout functionality

Registration system for new administrators

Protected routes that require authentication

3. Modern Interface
   
Responsive design that works on all devices

Bootstrap-styled components for professional appearance

Modal dialogs for adding/editing users

Action buttons for each record (View, Edit, Delete)



**Installation**

Clone the repository

Create and activate a virtual environment

Install requirements: pip install -r requirements.txt

Run migrations: python manage.py migrate

Create a superuser: python manage.py createsuperuser

Run the development server: python manage.py runserver

Usage Guide
Login:

Access the system at http://localhost:8000

Use your admin credentials to log in

View Records:

All records display in the main table

Sort by clicking column headers

Add New User:

Click "Add User" button

Fill in the modal form

Submit to create the record

Edit User:

Click "Edit" button on any record

Modify information in the form

Submit to update the record

Delete User:

Click "Delete" button

Confirm the action

Record will be permanently removed

Security Features
Password hashing for secure authentication

CSRF protection on all forms

Login-required decorators for protected views

Form validation to ensure data integrity

Customization Options
The application can be easily extended to:

Add more user fields

Implement search/filter functionality

Add user roles/permissions

Export data to CSV/Excel

Add pagination for large datasets

This Django CRUD application provides a solid foundation for any user management system with complete create, read, update, and delete functionality in a secure, modern interface.

**read database records**

![image](https://github.com/user-attachments/assets/710fba69-b5d2-4ed6-8ccd-596440335514)

**Add user**

![image](https://github.com/user-attachments/assets/69902c46-372f-4333-99f4-cf9020ce007d)

**Login**

![image](https://github.com/user-attachments/assets/017a2e4a-adbd-4459-8ba6-0e1c29f83178)

**registration new user**

![image](https://github.com/user-attachments/assets/8c030889-5d9d-4ccf-8ad2-54dce0c7ba05)

**view record**

![image](https://github.com/user-attachments/assets/176014cc-ff45-4117-abb5-b4f609c9cdaf)

**update record**

![image](https://github.com/user-attachments/assets/0a9cab74-a651-46d8-9308-42597d815ed5)

