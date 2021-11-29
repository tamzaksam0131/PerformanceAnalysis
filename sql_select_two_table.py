import sqlite3
import csv
import matplotlib
matplotlib.use ('TKAgg')
import matplotlib.pyplot as plt
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

def sql_analysis_output():

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    # Select_Data_1 = input ('Please Enter the selected data you want for table 1:')
    # Table_Names_1 = input ('Please Enter the Table Name for table 1:')
    # Condition_1 = input ('Please Enter the Condition for SQL Sentence for table 1:')


    # Select_Data_2 = input ('Please Enter the selected data you want for table 2:')
    # Table_Names_2 = input ('Please Enter the Table Name for table 2:')
    # Condition_2 = input ('Please Enter the Condition for SQL Sentence for table 2:')
    
    # SQL_Sentence = rf'SELECT {Select_Data_1} FROM {Table_Names_1} WHERE {Condition_1} UNION ALL SELECT {Select_Data_2} FROM {Table_Names_2} WHERE {Condition_2}'
    # sql_result = cur.execute(SQL_Sentence)
    
    # sql_result = cur.execute('SELECT * FROM Guangzhou_20210924_RAM WHERE blocksize = "2k" UNION ALL SELECT * FROM Taiwan_20210922_SDD WHERE blocksize = "2k"')
    
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)
    sql_sentence = 'SELECT'+' '+a['wanted data1']+' '+'FROM'+' '+a['table1'] +' '+'where'+' '+a['statement1'] +' '+ 'UNION ALL' + ' ' + 'SELECT'+' '+a['wanted data2']+' '+'from'+' '+a['table2'] +' '+'where'+' '+a['statement2']
    sql_result = cur.execute(sql_sentence)
    
    columnlist = []
    for column in sql_result.description:
        columnlist.append(column[0])
    print (columnlist)
    
    for row in sql_result:
        print (row)

    excel_filename = input ('Please Enter the name of the Excel file will be created:')
    
    cur.execute(sql_sentence)
    with open(f"{excel_filename}.csv","w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)

    cur.close()
    con.commit()
    con.close()


if __name__ == '__main__':
    sql_print_index()
    sql_analysis_output()