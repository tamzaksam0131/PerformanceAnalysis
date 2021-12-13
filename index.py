import sqlite3
from prettytable.prettytable import from_db_cursor

def sql_print_index():
    
    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    cur.execute('SELECT * From Index_Table')

    # column_list = []
    # for column in data.description:
    #     column_list.append(column[0])
    # print(column_list)
    
    # for row in data:
    #     print (row)
        
    x = from_db_cursor(cur)
    print (x)

    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
    sql_print_index()