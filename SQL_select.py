import sqlite3
import csv
import yaml

def SQL_printIndex():
    
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

def SQL_analysis_output():

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    # Select_Data = input ('Please Enter the selected data you want:')
    # Table_Names = input ('Please Enter the Table Name:')
    # Condition = input ('Please Enter the Condition for SQL Sentence:')
    # SQL_Sentence = rf'SELECT {Select_Data} FROM {Table_Names} WHERE {Condition}'
    # sql_result = cur.execute(SQL_Sentence)
    # sql_result = cur.execute('SELECT * FROM Index_Table,Guangzhou_20210924_RAM WHERE Index_Table.Key_ID = Guangzhou_20210924_RAM.Key_ID AND DRBD_Type = "drbd1001" AND Readwrite_type = "read" AND Number_of_Job = "8" AND IOdepth = "8"')

    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)
    SQL_Sentence = 'select'+' '+a['wanted data']+' '+'from'+' '+a['table'] +' '+'where'+' '+a['statement']
    sql_result = cur.execute((SQL_Sentence))
    
    columnlist = []
    for column in sql_result.description:
        columnlist.append(column[0])
    print (columnlist)

    for row in sql_result:
        print (row)

    Excel_filename = input ('Please Enter the name of the Excel file will be created:')
    
    cur.execute(SQL_Sentence)
    with open(f"{Excel_filename}.csv","w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)

    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
    SQL_printIndex()
    SQL_analysis_output()