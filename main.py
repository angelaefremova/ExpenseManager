import sqlite3

from functions import *
from main_menu import *
from categories_menu import *
from expenses_menu import *
from reports_menu import *

import os

os.system('cls')

conn = sqlite3.connect('expenses.sqlite')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS Categories
    (id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL)''')
cur.execute('''
    CREATE TABLE IF NOT EXISTS Expenses
    (id INTEGER NOT NULL PRIMARY KEY,
    cat_id INTEGER NOT NULL,
    day INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    e_date REAL NOT NULL,
    amount REAL NOT NULL,
    comment TEXT,
    FOREIGN KEY (cat_id) REFERENCES Categories(id) ON DELETE CASCADE ON UPDATE NO ACTION)
    ''')
conn.commit()
cur.close()

while True:
    menu_choice = main_menu()
    if menu_choice == "1":
        while True:
            categories_menu_choice = categories_menu()
            if categories_menu_choice == "1":
                show_all_categories()
            if categories_menu_choice == "2":
                add_new_category()
            if categories_menu_choice == "3":
                edit_category()
            if categories_menu_choice == "4":
                delete_category()
            if categories_menu_choice == "5":
                break

    if menu_choice == "2":
        while True:
            expenses_menu_choice = expenses_menu()
            if expenses_menu_choice == "1":
                show_all_expenses()
            if expenses_menu_choice == "2":
                add_new_expense()
            if expenses_menu_choice == "3":
                edit_expense()
            if expenses_menu_choice == "4":
                delete_expense()
            if expenses_menu_choice == "5":
                break

    if menu_choice == "3":
        while True:
            reports_menu_choice = reports_menu()
            if reports_menu_choice == "1":
                monthly_report()
            if reports_menu_choice == "2":
                yearly_report()
            if reports_menu_choice == "3":
                m_y_comparison_report()
            if reports_menu_choice == "4":
                percent_report()
            if reports_menu_choice == "5":
                break

    if menu_choice == "4":
        os.system('cls')
        print("\n\n\nThank you for using the application!\n\n\n")
        exit()
