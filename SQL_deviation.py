import abc
import sqlite3
from sqlite3.dbapi2 import ProgrammingError
import numpy as np
import matplotlib as mpl
mpl.use ('TKAgg')
import matplotlib.pyplot as plt
import yaml

standard_values = []
example_values = []
ratio_per = []

# value = ""
# Standard_table_name = ""
# Standard_drbd = ""
# Standard_readwrite_Type = ""
# Example_table_name = ""
# Example_drbd = ""
# Example_readwrite_Type = ""

def SQL_printIndex():
    
    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    data = cur.execute('SELECT * From Index_Table')

    for column in data.description:
        print(column[0],end=" ")
    
    print()
    for row in data:
        print (row)

    cur.close()
    con.commit()
    con.close()

def SQL_pick_standard_values():

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    # value_1 = input('Please Enter the Standard value you want(IOPS / MBPS):')
    # Table_Names_1 = input ('Please Enter the Text Table Name(Standard):')
    # Readwrite_Type_1 = input ('Please Enter the readwrite type(Standard):')
    # DRBD_Type_1 = input ('Please Enter the drbd type(Standard):')

    # global value
    # value = value_1
    # global Standard_table_name
    # Standard_table_name = Table_Names_1
    # global Standard_readwrite_Type
    # Standard_readwrite_Type = Readwrite_Type_1
    # global Standard_drbd
    # Standard_drbd = DRBD_Type_1

    # sql_result_1 = cur.execute(rf'SELECT {value_1} From {Table_Names_1} WHERE Readwrite_type = "{Readwrite_Type_1}" AND DRBD_Type = "{DRBD_Type_1}"')
    # sql_result_1 = cur.execute('SELECT IOPS From Guangzhou_20210924_RAM WHERE Readwrite_type = "randwrite" AND DRBD_Type = "drbd1001"')

    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)
    SQL_Sentence = 'SELECT' + ' ' + a['Standard_Value'] + ' ' + 'From' + ' ' + a['Table_Name_devi_1'] \
                + ' ' + 'WHERE Readwrite_type = ' + ' ' + a['ReadWrite_Type_Stan'] \
                + ' ' + 'AND DRBD_Type = ' + ' ' + a['DRBD_Type_Stan']
    
    sql_result_1 = cur.execute(SQL_Sentence)
    
    for row in sql_result_1:
        # print (row)
        standard_values.append(row[0])
    print (standard_values)

    cur.close()
    con.commit()
    con.close()

def SQL_pick_example_values():
    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    # value_2 = input('Please Enter the Compared value you want(IOPS / MBPS):')
    # Table_Names_2 = input ('Please Enter the Text Table Name(Compared):')
    # Readwrite_Type_2 = input ('Please Enter the readwrite type(Compared):')
    # DRBD_Type_2 = input ('Please Enter the drbd type(Compared):')

    # global Example_table_name
    # Example_table_name = Table_Names_2
    # global Example_readwrite_Type
    # Example_readwrite_Type = Readwrite_Type_2
    # global Example_drbd
    # Example_drbd = DRBD_Type_2

    # sql_result_2 = cur.execute(rf'SELECT {value_2} From {Table_Names_2} WHERE Readwrite_type = "{Readwrite_Type_2}" AND DRBD_Type = "{DRBD_Type_2}"')
    # sql_result_2 = cur.execute('SELECT IOPS From Guangzhou_20210924_RAM WHERE Readwrite_type = "write" AND DRBD_Type = "drbd1002"')

    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)
    SQL_Sentence = 'SELECT' + ' ' + a['Example_Value'] + ' ' + 'From' + ' ' + a['Table_Name_devi_2'] \
                + ' ' + 'WHERE Readwrite_type = ' + ' ' + a['ReadWrite_Type_Ex'] \
                + ' ' + 'AND DRBD_Type = ' + ' ' + a['DRBD_Type_Ex']
    
    sql_result_2 = cur.execute(SQL_Sentence)
    
    for row in sql_result_2:
        # print (row)
        example_values.append(row[0])
    print (example_values)

    cur.close()
    con.commit()
    con.close()

def draw():
    a_yaml_file = open('sql_config.yml')
    ayaml = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    diffence = [example_values - standard_values for example_values, standard_values in zip (example_values, standard_values)]
    print (diffence)
    ratio = [diffence / standard_values for diffence, standard_values in zip (diffence, standard_values)]

    ratio_per = [round(i*100,2) for i in ratio]
    # print (ratio)
    print (ratio_per)

    blocksize_range = ['1k', '2k','4k','8k','16k','32k','64k','128k','256k','512k','1M','2M']
    
    plt.figure(figsize=(50,50), dpi = 100)
    bar_width = 0.3
    
    for i in range(len(blocksize_range)):
        # print (i)
        x_data = blocksize_range[i]
        # print (x_data)
        y_data = ratio_per[i]
        # print (y_data)
        plt.bar(x_data, y_data, width = bar_width)

    plt.xlabel ('Blocksize')
    plt.ylabel ('Rate of difference (Percentage)')
    plt.xticks (rotation = 30)
    for a,b in zip(blocksize_range,ratio_per):
        plt.text(a, b+0.05, '%.2f' % b, ha = 'center', va = 'bottom', fontsize = 11)
    
    plt.title(ayaml['Standard_Value'] + ' ' + 'difference(%)' + ' ' + ayaml['Table_Name_devi_1'] + '(' + ayaml['DRBD_Type_Stan']+','+ ayaml['ReadWrite_Type_Stan']+ ')'+ ' ' + 'vs.' + ayaml['Table_Name_devi_2'] + '(' + ayaml['DRBD_Type_Ex']+','+ayaml['ReadWrite_Type_Ex'] + ')')
    plt.grid()
    
    # file_name = ayaml['Standard_Value'] + ' ' + 'difference(%)' + ' ' + ayaml['Table_Name_devi_1'] + '(' + ayaml['DRBD_Type_Stan']+','+ ayaml['ReadWrite_Type_Stan']+ ')'+ ' ' + 'vs.' + ayaml['Table_Name_devi_2'] + '(' + ayaml['DRBD_Type_Ex']+','+ayaml['ReadWrite_Type_Ex'] + ')'
    # plt.savefig(file_name)
    plt.show()

if __name__ == '__main__':
    SQL_printIndex()
    SQL_pick_standard_values()
    SQL_pick_example_values()
    draw()