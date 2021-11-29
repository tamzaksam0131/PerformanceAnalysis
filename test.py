import sqlite3
import yaml

def sql_test():
    
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    SQL_sentence = 'SELECT' + ' ' + a['wanted data'] + ' ' + 'From' + ' ' + a['table view']
    print (SQL_sentence)
    
    data = cur.execute(SQL_sentence)

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
    sql_test()