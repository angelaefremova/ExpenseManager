import os
import sqlite3
import datetime
from datetime import date
from functions import *

def reports_menu():
    menu_layout = """
    —————————————————————————————
    |                           |
    | 1 - Monthly report        |
    |                           |
    | 2 - Yearly report         |
    |                           |
    | 3 - Month/Year            |
    |     expenses comparison   |
    |                           |
    | 4 - Expenses %            |
    |                           |
    | 5 - Go back               |
    |                           |
    —————————————————————————————
                                      """
    os.system('cls')
    print(menu_layout)

    menu_choice = input("Select from the menu: ")
    return menu_choice

def monthly_report():
    os.system('cls')
    print("\n--- Monthly report ---\n")

    while True:
        e_day =  1
        e_month = int(input("Report for month (1-12): "))
        e_year = int(input("Report for year: "))
        try:
            e_datetime = datetime.datetime(e_year, e_month, e_day)
            e_timestamp = e_datetime.timestamp()
        except:
            print("This is not a proper date entry.")
            print("Please try again.")
        else:
            break

    conn = sqlite3.connect('expenses.sqlite')
    cur = conn.cursor()
    sql = '''SELECT Expenses.id, name, day, month, year, e_date, amount, comment 
            FROM Expenses INNER JOIN Categories ON Categories.id = Expenses.cat_id
            WHERE month = ? AND year = ?
            ORDER BY name, e_date'''
    cur.execute(sql, (e_month, e_year))
    expenses = cur.fetchall()
    show_expenses(expenses)
    print('\n')
    sql = '''SELECT Expenses.id, name, day, month, year, e_date, SUM(amount), comment 
            FROM Expenses INNER JOIN Categories ON Categories.id = Expenses.cat_id
            WHERE month = ? AND year = ?
            GROUP BY Categories.id'''
    cur.execute(sql, (e_month, e_year))
    cat_expenses = cur.fetchall()
    print('For month ', month_name(e_month), ' year ', str(e_year), 'expenses per category are:')
    print('————————————————————————————————————————————————————————————————————————————————————')
    for cat_expense in cat_expenses:
        print(cat_expense[1].ljust(15), ':', ('$ ' + str(cat_expense[6])).rjust(10))
    print('\n')
    cur.close()
    fnc_return = input("Press Enter to continue!")
    return fnc_return


def yearly_report():
    os.system('cls')
    print("\n--- Yearly report ---\n")
    fnc_return = input("Press Enter to continue!")
    return fnc_return


def m_y_comparison_report():
    os.system('cls')
    print("\n--- Month/Year comparison report ---\n")
    fnc_return = input("Press Enter to continue!")
    return fnc_return

def percent_report():
    os.system('cls')
    print("\n--- Percent report ---\n")
    fnc_return = input("Press Enter to continue!")
    return fnc_return