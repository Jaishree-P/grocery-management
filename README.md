Grocery Management System (Python + MySQL)

A simple terminal-based system to manage grocery products, generate bills, and track inventory using Python and MySQL.

Requirements

- Python 3.x
- XAMPP (includes MySQL/MariaDB)
- mysql-connector-python

1. Install XAMPP

1. Download XAMPP from [https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html)
2. Install it on your system.
3. Open XAMPP Control Panel and Start the MySQL module.
4. Open phpMyAdmin via `http://localhost/phpmyadmin`

2. Create Database & Tables

1. In phpMyAdmin, go to SQL tab.
2. Paste and run the following SQL code:


CREATE DATABASE IF NOT EXISTS grocery_db;
USE grocery_db;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE IF NOT EXISTS bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    items TEXT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

 3. Install Python Dependencies
    in vs code terminal :pip install mysql-connector-python
   4. Run the Program
      in vs code terminal : python main.py

Features
Add, view, update, and delete products
Generate customer bills with automatic stock update
View past bills with timestamp
