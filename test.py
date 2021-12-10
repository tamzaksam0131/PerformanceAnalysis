import sqlite3
import yaml
from prettytable import from_db_cursor

def sql_test():
    
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    # print (a['table view'])
    # print (a['wanted data view'])

    for i in range(len(a['table view'])):
        # print (i)
        # print (a['table view'][i])
        sql_sentence = 'SELECT' + ' ' +  a['wanted data view'] + ' ' + 'From' + ' ' + a['table view'][i]
        # print (sql_sentence)

        cur.execute(sql_sentence)
        # print (data)

        # column_list = []
        # for column in data.description:
        #     column_list.append(column[0])
        # print(column_list)

        # for row in data:
            # print (row)
        x = from_db_cursor(cur)
        print (x)

    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
    sql_test()