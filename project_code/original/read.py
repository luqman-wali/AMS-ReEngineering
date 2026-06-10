import datetime
import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate # pip install tabulate

def print_query(query, cur, con):
    try:
        cur.execute(query)
        con.commit()
        result = cur.fetchall()
        
        if len(result) != 0:
            header = result[0].keys()
            rows =  [x.values() for x in result]
            print(tabulate(rows, header, tablefmt = 'psql'))
        
        else:
            print("Not found!")

    except Exception as e:
        print(e)
        con.rollback()
        input("Press any key to continue")


def read_data(cur, con, table_name):
    query = "select * from `" + table_name +"`;"
    print_query(query, cur, con)