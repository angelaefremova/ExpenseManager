import os
import sqlite3
import datetime
from datetime import date

def show_categories(categories):
    print('————————————————————————————————————')
    print('|', 'Cat. ID'.center(10),'|', 'Cat. Name'.center(20),'|')
    print('————————————————————————————————————')
    for category in categories:
        print('|',str(category[0]).center(10), '|', category[1].center(20), '|')
    print('————————————————————————————————————','\n')

def show_expenses(expenses):
    print('————————————————————————————————————————————————————————————————————————————————————————————————————————————————————')
    print('|', 'Exp.ID'.center(10),'|', 'Category'.center(20),'|', 'Date'.center(20),'|', 'Amount'.center(20),'|', 'Comment'.center(30),'|')
    print('————————————————————————————————————————————————————————————————————————————————————————————————————————————————————')
    for expense in expenses:
        amount = '$ ' + str(expense[6])
        e_date = str(expense[4]) + '-' + str(expense[3]) + '-' + str(expense[2])
        print('|',str(expense[0]).center(10), '|', expense[1].ljust(20), '|', e_date.center(20), '|', amount.rjust(20), '|', expense[7].ljust(30), '|')
    print('————————————————————————————————————————————————————————————————————————————————————————————————————————————————————','\n')

def create_cat_dic(categories):
    cat_dic = {}
    for category in categories:
        cat_dic[category[0]] = category[1]
    return cat_dic

def input_date():
    while True:
        date_day =  int(input('Day (1-31):'))
        date_month =  int(input('Month (1-12):'))
        date_year =  int(input('Year:'))
        try:
            date_datetime = datetime.datetime(date_year, date_month, date_day)
            date_timestamp = date_datetime.timestamp()
        except:
            print("This is not a proper date entry.")
            print("Please try again.")
        else:
            break
    e_date = [date_day, date_month, date_year, date_timestamp]
    return e_date

def month_name(month_num):
    months = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December', 
    }
    return months[month_num]