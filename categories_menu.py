import os
import sqlite3
import datetime
from datetime import date
from functions import *

def categories_menu():
    menu_layout = """
    —————————————————————————————
    |                           |
    | 1 - Show all categories   |
    |                           |
    | 2 - Add new category      |
    |                           |
    | 3 - Edit category         |
    |                           |
    | 4 - Delete category       |
    |                           |
    | 5 - Go Back               |
    |                           |
    —————————————————————————————
                                      """
    os.system('cls')
    print(menu_layout)

    menu_choice = input("Select from the menu: ")
    return menu_choice

def show_all_categories():
    os.system('cls')
    print("\n","--- Show all categories ---".center(30),"\n")
    conn = sqlite3.connect('expenses.sqlite')
    cur = conn.cursor()
    sql = 'SELECT * FROM Categories'
    cur.execute(sql)
    categories = cur.fetchall()
    show_categories(categories)
    cur.close()
    fnc_return = input("Press Enter to continue!")
    return fnc_return

def add_new_category():
    os.system('cls')
    print("\n--- Add new category ---\n")
    conn = sqlite3.connect('expenses.sqlite')
    cur = conn.cursor()
    catName = input('Category name:')
    cur.execute('''INSERT INTO Categories
        (name) VALUES (?)''', (catName,)) 
    conn.commit()
    fnc_return = show_all_categories()
    return fnc_return

def edit_category():
    os.system('cls')
    print("\n--- Edit category ---\n")
    conn = sqlite3.connect('expenses.sqlite')
    cur = conn.cursor()
    sql = 'SELECT * FROM Categories'
    cur.execute(sql)
    categories = cur.fetchall()
    show_categories(categories)
    editID = input('What is the ID of the category to be edited? ')
    editName = input('What is the new edited name of the category? ')
    sql = '''UPDATE Categories
            SET name = ?
            WHERE id = ?'''
    cur.execute(sql, (editName, editID))
    conn.commit()
    print()
    fnc_return = show_all_categories()
    return fnc_return

def delete_category():
    os.system('cls')
    print("\n--- Delete category ---\n")
    conn = sqlite3.connect('expenses.sqlite')
    cur = conn.cursor()
    query = 'SELECT * FROM Categories'
    cur.execute(query)
    categories = cur.fetchall()
    show_categories(categories)
    delID = input('What is the ID of the category to be deleted? ')
    sql = '''DELETE FROM Categories
            WHERE id = ?'''
    cur.execute(sql, (delID,))
    conn.commit()
    print()
    fnc_return = show_all_categories()
    return fnc_return