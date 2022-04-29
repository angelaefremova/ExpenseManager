import os
import sqlite3
import datetime
from datetime import date
from functions import *

def expenses_menu():
    menu_layout = """
    —————————————————————————————
    |                           |
    | 1 - Show all expenses     |
    |                           |
    | 2 - Add new expense       |
    |                           |
    | 3 - Edit expense          |
    |                           |
    | 4 - Delete expense        |
    |                           |
    | 5 - Go back               |
    |                           |
    —————————————————————————————
                                      """
    os.system('cls')
    print(menu_layout)

    menu_choice = input("Select from the menu: ")
    return menu_choice

def show_all_expenses():
    os.system('cls')
    print("\n--- Show all expenses ---\n")
    conn = sqlite3.connect('expenses.sqlite')
    cur = conn.cursor()
    sql = '''SELECT Expenses.id, name, day, month, year, e_date, amount, comment 
            FROM Expenses INNER JOIN Categories ON Categories.id = Expenses.cat_id
            ORDER BY e_date'''
    cur.execute(sql)
    expenses = cur.fetchall()
    show_expenses(expenses)
    cur.close()
    fnc_return = input("Press Enter to continue!")
    return fnc_return

def add_new_expense():
    os.system('cls')
    print("\n--- Add new expense ---\n")
    conn = sqlite3.connect('expenses.sqlite')
    cur = conn.cursor()
    
    sql = 'SELECT * FROM Categories'
    cur.execute(sql)
    categories = cur.fetchall()
    show_categories(categories)
    cat_dic = create_cat_dic(categories)
    while True:
        catID = input('Category name ID:')
        if int(catID) in cat_dic:
            break
        else:
            print('It is not valid category ID.')

    print("What is the date of the expense?")
    e_date = input_date()
    amount = float(input('Amount: '))
    comment = input('Comment: ')
    cur.execute('''INSERT INTO Expenses (cat_ID, day, month, year, e_date, amount, comment) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (catID, e_date[0], e_date[1], e_date[2], e_date[3], amount, comment)) 
    conn.commit()
    fnc_return = show_all_expenses()
    return fnc_return

def edit_expense():
    os.system('cls')
    print("\n--- Edit expense ---\n")
    print('The expense that you want to edit is between dates:')
    print('Start date:')
    startDate = input_date()
    print('End date:')
    endDate = input_date()
    conn = sqlite3.connect('expenses.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT Expenses.id, name, day, month, year, e_date, amount, comment
        FROM Expenses INNER JOIN Categories ON Categories.id = Expenses.cat_id 
        WHERE (e_date BETWEEN ? AND ?)
        ORDER BY year, month, day''', (startDate[3], endDate[3]))
    expenses = cur.fetchall()
    show_expenses(expenses)
    
    editID = input('What is the ID of the expense to be edited? ')
    cur.execute('''SELECT Expenses.id, name, day, month, year, e_date, amount, comment, cat_id 
        FROM Expenses INNER JOIN Categories ON Categories.id = Expenses.cat_id 
        WHERE Expenses.id = ?''', (editID,))
    expenses = cur.fetchall()
    show_expenses(expenses)
    for expense in expenses:
        catID_old = expense[8]
        day_old = expense[2]
        month_old = expense[3]
        year_old = expense[4]
        e_date_old = expense[5]
        amount_old = expense[6]
        comment_old = expense[7]
    
    sql = 'SELECT * FROM Categories'
    cur.execute(sql)
    categories = cur.fetchall()
    show_categories(categories)
    cat_dic = create_cat_dic(categories)

    while True:
        question = 'If category ID is ' + str(catID_old) + ' hit \"Enter\" or put differnet category ID.'
        catID = input(question)
        if catID == "":
            catID = catID_old
            break
        if int(catID) in cat_dic:
            break
        else:
            print('It is not valid category ID.')

    question = "Date of the expense: " + str(year_old) + "-" + str(month_old) + "-" + str(day_old) + "? (y/n) "
    if input(question) == 'y':
        day = day_old
        month = month_old
        year = year_old
        e_date = e_date_old
        e_date_list = [day, month, year, e_date_old]
    else:
        print('New date of the expense:\n')
        e_date_list = input_date()

    question = 'Amount: ' + str(amount_old) + '? (y/n) '
    if input(question) == 'y':
        amount = amount_old
    else:
        amount = float(input('New amount: '))

    question = 'Comment: ' + comment_old + '? (y/n) '
    if input(question) == 'y':
        comment = comment_old
    else:
        comment = input('New comment: ')

    cur.execute('''UPDATE Expenses
        SET cat_ID = ?,
            day = ?,
            month = ?,
            year = ?,
            e_date = ?,
            amount = ?,
            comment = ?
        WHERE 
            Expenses.id = ?''', (catID, e_date_list[0], e_date_list[1], e_date_list[2], e_date_list[3], amount, comment, editID)) 
    conn.commit()
    cur.close()
    fnc_return = show_all_expenses()
    return fnc_return

def delete_expense():
    os.system('cls')
    print("\n--- Delete expenses ---\n")
    print('The expense that you want to delet is between dates:')
    print('Start date:')
    startDate = input_date()
    print('End date:')
    endDate = input_date()
    conn = sqlite3.connect('expenses.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT Expenses.id, name, day, month, year, e_date, amount, comment 
        FROM Expenses INNER JOIN Categories ON Categories.id = Expenses.cat_id 
        WHERE (e_date BETWEEN ? AND ?)
        ORDER BY e_date''', (startDate[3], endDate[3]))
    expenses = cur.fetchall()
    show_expenses(expenses)
    delID = input('What is the ID of the expense to be deleted? ')
    sql = '''DELETE FROM Expenses
            WHERE id = ?'''
    cur.execute(sql, (delID,))
    conn.commit()
    cur.close()
    fnc_return = show_all_expenses()
    return fnc_return