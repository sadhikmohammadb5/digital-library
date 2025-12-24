Digital Library Management System
CS50 Final Project
Project Title

Digital Library Management System

Video Demo

Video Demo URL: https://youtu.be/UVEBl7mF4wU

Description:

The Digital Library Management System is a web-based application developed as my Final Project for CS50 -Introduction to 
Computer Science. This project is built using Python, Flask, HTML, CSS, and SQLite, and it provides users with a secure platform 
to access and read digital books online.

The main objective of this project is to apply the programming concepts learned throughout CS50 to build a complete, real-world 
software application. Unlike the individual problem sets in the course, this project combines backend development, frontend 
design, database management, and authentication into a single cohesive system.

In many educational institutions and communities, access to physical libraries can be limited. Even when digital resources exist, 
they are often poorly organized or lack proper access control. This Digital Library attempts to solve that problem by offering a 
simple, organized, and secure platform where users can register, log in, and read books digitally.

What the Software Does :

The Digital Library Management System performs the following functions:

Allows users to create an account using a username and password

Enables registered users to log in securely

Maintains user login sessions across multiple pages

Restricts access to library content for unauthorized users

Displays available digital books

Allows users to read book content directly in the browser

Allows users to log out safely, ending their session

The system ensures that all sensitive content is protected and accessible only to authenticated users.

Features:
User Registration:

New users can create an account by providing a username and password. The system checks for valid input and securely stores user 
credentials in the database.

User Login :

Registered users can log in using their credentials. Passwords are verified using secure hashing methods rather than plain-text 
comparison.

Session Management:

Once logged in, the user remains authenticated using Flask sessions. This allows smooth navigation between pages without 
repeatedly logging in.

Digital Book Access:

Authenticated users can view and read digital book content within the application. The reading interface is simple and focused to 
ensure ease of use.

Security:

The application follows basic security practices such as:

Password hashing using Werkzeug

Session-based authentication

Protected routes that require login

Parameterized SQL queries to prevent SQL injection

Technologies Used:
Backend:

Python - Core programming language

Flask - Web framework used for routing and request handling

Frontend

HTML - Page structure

CSS - Styling and layout

Jinja2 - Template rendering

Database

SQLite - Stores user and book data

Security

Werkzeug - Password hashing and authentication support

Project File Structure and Explanation
```
digital-library/
│
├── app.py
│   ├── Main Flask application file
│   ├── Contains routes, authentication logic, and database queries
│
├── library.db
│   ├── SQLite database
│   ├── Stores user credentials and book information
│
├── templates/
│   ├── layout.html
│   │   └── Base template shared by all pages
│   │
│   ├── login.html
│   │   └── Login page for registered users
│   │
│   ├── register.html
│   │   └── Registration page for new users
│   │
│   ├── read.html
│   │   └── Displays book content for reading
│
├── static/
│   ├── style.css
│   │   └── Stylesheet for application design
│
└── README.md
    └── Project documentation

```
Each file has a specific purpose, making the project modular and easier to understand and maintain.

Design Decisions:
Choice of Flask:

Flask was chosen because it is lightweight, flexible, and easy to understand. It allows rapid development while giving full 
control over application logic.

Choice of SQLite:

SQLite was selected as the database because it is simple, lightweight, and does not require additional setup. It is ideal for 
small-to-medium-scale applications and aligns well with CS50's focus on SQL.

Authentication Design:

Session-based authentication was implemented because it is secure and widely used in web applications. Password hashing ensures 
that user credentials are protected even if the database is accessed.

How to Run the Project:

Install Python 3.8 or above

Install Flask using:

pip install flask


Run the application:

python app.py


Open a browser and visit:

http://127.0.0.1:5000/

Testing

The project was tested manually by:

Registering multiple users

Logging in with valid and invalid credentials

Attempting to access restricted pages without login

Reading book content after authentication

Logging out and confirming session termination

All core features worked as expected.

Limitations and Future Improvements
Current Limitations

No admin panel for book management

Books are static and preloaded

No search or filtering system

Future Improvements

Admin dashboard for managing books

Search and filter functionality

PDF upload and download support

Reading history tracking

Mobile-responsive design

What I Learned:

This project significantly improved my understanding of how web applications work. I learned how backend logic connects to 
frontend templates, how databases store and retrieve information, and how authentication systems protect user data. I also gained 
experience in debugging, structuring projects, and making design decisions.

Academic Honesty:

This project is entirely my own work and complies with CS50's Academic Honesty policy. Any external resources were used only for 
reference, and no unauthorized code was copied.

Conclusion:

The Digital Library Management System represents the culmination of my learning in CS50. It demonstrates my ability to design and 
implement a complete software application using multiple technologies. This project reflects my growth in programming and my 
ability to apply computer science concepts to solve real-world problems.