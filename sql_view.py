import sqlite3
import yaml
import prettytable

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

def sql_test():
    
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    for i in range(len(a['table view'])):

        sql_sentence = 'SELECT' + ' ' +  a['wanted data view'] + ' ' + 'From' + ' ' + a['table view'][i]
        # print (sql_sentence)
    
        # x = prettytable
        data = cur.execute(sql_sentence)

        column_list = []
        for column in data.description:
            column_list.append(column[0])
        print(column_list)
        # x.field_names = column_list

        for row in data:
            print (row)
            # x.add_rows(row)
            # x = row
        # print (x)
  

    cur.close()
    con.commit()
    con.close()


if __name__ == '__main__':
    sql_print_index()
    sql_test()