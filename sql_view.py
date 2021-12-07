import sqlite3
import yaml

def sql_print_index():
    
    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    sql_result = cur.execute('SELECT * From Index_Table')

    columnlist = []
    for column in sql_result.description:
        columnlist.append(column[0])
    print (columnlist)
    
    for row in sql_result:
        print (row)

    cur.close()
    con.commit()
    con.close()

def num_test():
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)
    
    number = a['number of view']
    
    if number == '1':
        sql_test()
    if number == '2':
        sql_test_2()
    if number == '3':
        sql_test_3()


def sql_test():
    
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    sql_sentence = 'SELECT' + ' ' + a['wanted data view'] + ' ' + 'From' + ' ' + a['table view']
    data = cur.execute(sql_sentence)

    column_list = []
    for column in data.description:
        column_list.append(column[0])
    print(column_list)
    
    for row in data:
        print (row)

    cur.close()
    con.commit()
    con.close()

def sql_test_2():
    
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    sql_sentence = 'SELECT' + ' ' + a['wanted data view'] + ' ' + 'From' + ' ' + a['table view'] \
                + ' ' + 'UNION ALL' + ' ' + 'SELECT' + ' ' + a['wanted data view 2'] + ' ' + 'From' + ' ' + a['table view 2']
    data = cur.execute(sql_sentence)

    column_list = []
    for column in data.description:
        column_list.append(column[0])
    print(column_list)
    
    for row in data:
        print (row)

    cur.close()
    con.commit()
    con.close()

def sql_test_3():
    
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    sql_sentence = 'SELECT' + ' ' + a['wanted data view'] + ' ' + 'From' + ' ' + a['table view'] \
                    + ' ' + 'UNION ALL' + ' ' +'SELECT' + ' ' + a['wanted data view 2'] + ' ' + 'From' + ' ' + a['table view 2'] \
                    + ' ' + 'UNION ALL' + ' ' + 'SELECT' + ' ' + a['wanted data view 3'] + ' ' + 'From' + ' ' + a['table view 3']
    data = cur.execute(sql_sentence)

    column_list = []
    for column in data.description:
        column_list.append(column[0])
    print(column_list)
    
    for row in data:
        print (row)

    cur.close()
    con.commit()
    con.close()


if __name__ == '__main__':
    sql_print_index()
    num_test()