import datetime
import subprocess as sp
import pymysql
import pymysql.cursors
import sys

colors_dict_1 = {
    "BLUE": "\033[1;34m",
    "RED": "\033[1;31m",
    "CYAN": "\033[1;36m",
    "GREEN": "\033[0;32m",
    "RESET": "\033[0;0m",
    "BOLD": "\033[;1m",
    "REVERSE": "\033[;7m",
    "ERROR":"\033[;7m"+"\033[1;31m"
}

def offload_commit(con):
    #con.commit()
    return

def debug_print(msg):
    decorate_output("REVERSE")
    #print(msg)
    decorate_output("RESET")

def error_print(msg):
    decorate_output("RED")
    print(msg)
    decorate_output("RESET")
    
def add_yes_print():
    decorate_output("GREEN")
    print("Insertion successful")
    decorate_output("RESET")

def success_print(msg):
    decorate_output("GREEN")
    print(msg)
    decorate_output("RESET")
    
def decorate_output(color_str):
    #print("Decorated")
    sys.stdout.write(colors_dict_1[color_str])

def part():
    print("-----------------------------------------------------------------")
    return


def part2():
    print("=====================================================================")
    return

def part3():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    return

def date_less_cur(date_str):
    today_date = datetime.date.today()
    today_date_str = today_date.strftime("%Y-%m-%d")

    if date_str < today_date_str:
        return 1
    else:
        return 0

def date_more_cur(date_str):
    today_date = datetime.date.today()
    today_date_str = today_date.strftime("%Y-%m-%d")

    if date_str > today_date_str:
        return 1
    else:
        return 0

def numeric_check(ch):
    
    if ch>='0' and ch<='9':
        return 1
    else:
        return 0

def dep_ahead_arv(arrival_str, depart_str):
    if len(arrival_str)!=5 or len(depart_str)!=5:
        error_print('Invalid format')
        return -1
    
    if numeric_check(arrival_str[0])+numeric_check(arrival_str[1])+numeric_check(arrival_str[3])+numeric_check(arrival_str[4])!=4:
        error_print("Error: Enter only digits for mm and hh in arrival time")
        return -1
    
    if numeric_check(depart_str[0])+numeric_check(depart_str[1])+numeric_check(depart_str[3])+numeric_check(depart_str[4])!=4:
        error_print("Error: Enter only digits for mm and hh in departure time")
        return -1

    arrival_hrs = int(arrival_str[0:2])
    arrival_min = int(arrival_str[3:5])
    depart_hrs = int(depart_str[0:2])
    depart_min = int(depart_str[3:5])

    
    if depart_hrs > arrival_hrs:
        error_print('Arrival time can not be ahead of departure time')
        return -1
    
    elif depart_hrs == arrival_hrs and depart_min > arrival_min:
        error_print('Arrival time can not be ahead of departure time')
        return -1
    
    else:
        return 0

# NOTE: This is a LEGACY/MONOLITHIC function with HIGH CYCLOMATIC COMPLEXITY
# CODE SMELL: God Method - Does too many things
# This function handles multiple responsibilities:
# 1. Data validation
# 2. User input
# 3. Database operations
# 4. Error handling
# Recommendation: Refactor into smaller, single-responsibility functions

def add_airline(cur, con):
    table_name = "`Airline`"
    attr = {}
    print('Enter details of the new airline:')
    attr['IATA airline designators'] = input('Enter 2-character IATA airline designator code * :')
    attr['Company Name'] = input('Enter airline name *: ')
    attr['num_aircrafts_owned'] = input('Enter number of aircrafts currently owned by the airline: ')
    tmp = input('Enter 1 if airline is active, 0 otherwise: ')
    if tmp == 1:
        attr['is_active'] = True
    elif tmp == 0:
        attr['is_active'] = False
    attr['country_of_ownership'] = input('Enter country of ownership of airline: ')
    keys_str = ", ".join([f"`{k}`" for k in attr.keys() if attr[k]])
    values_str = ", ".join([f'\'{v}\'' for v in attr.values() if v])
    query_str = f'INSERT INTO {table_name} ( {keys_str} ) VALUES ( {values_str} );'
    try:
        cur.execute(query_str)
        add_yes_print()
        con.commit()
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return