import sqlite3
import numpy as np
import matplotlib as mpl
mpl.use ('TKAgg')
import matplotlib.pyplot as plt
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

def decide_number():
    number = input ("Please Enter the number of Text Table (2 or 3):")
    if number == "2":
        SQL_graph_output_2()
    if number == "3":
        SQL_graph_output_3()

def SQL_graph_output_2():

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    # Select_Data = input ('Please Enter the selected data you want(IOPS or MBPS):')
    # Table_Names_1 = input ('Please Enter the Text Table Name 1:')
    # Table_Names_2 = input ('Please Enter the Text Table Name 2:')
    # Block_Size = input ('Please Enter the Block Size (4k or 1M):')
    
    # SQL_Sentence = rf'''SELECT Text_Table_Name, DRBD_Type, {Select_Data} FROM Index_table, {Table_Names_1}
    #                         WHERE Readwrite_type = "randwrite"
    #                         AND Number_of_Job = "8"
    #                         AND IOdepth = "8"
    #                         AND blocksize = "{Block_Size}"
    #                         AND Index_table.Key_ID = {Table_Names_1}.Key_ID
    #                         UNION ALL
    #                         SELECT Text_Table_Name, DRBD_Type, {Select_Data} FROM Index_table, {Table_Names_2}
    #                         WHERE Readwrite_type = "randwrite"
    #                         AND Number_of_Job = "8"
    #                         AND IOdepth = "8"
    #                         AND blocksize = "{Block_Size}"
    #                         AND Index_table.Key_ID = {Table_Names_2}.Key_ID
                            #  '''

    # SQL_Sentence = '''SELECT Text_Table_Name, DRBD_Type, MBPS FROM Index_table, Guangzhou_20210924_RAM
    #                     WHERE Readwrite_type = "randwrite"
    #                     AND Number_of_Job = "8"
    #                     AND IOdepth = "8"
    #                     AND blocksize = "4k"
    #                     AND Index_table.Key_ID = Guangzhou_20210924_RAM.Key_ID
    #                     UNION ALL
    #                     SELECT Text_Table_Name, DRBD_Type, MBPS FROM Index_table, Taiwan_20210922_SDD
    #                     WHERE Readwrite_type = "randwrite"
    #                     AND Number_of_Job = "8"
    #                     AND IOdepth = "8"
    #                     AND blocksize = "4k"
    #                     AND Index_table.Key_ID = Taiwan_20210922_SDD.Key_ID
    #                     '''
    
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    SQL_Sentence = 'SELECT Text_Table_Name, DRBD_Type,' + ' ' + a['Select_Data_2hist'] + ' ' + 'FROM Index_table,' +  a['Table_Name_2hist_1'] \
                + ' ' + 'WHERE Readwrite_type = "randwrite"'\
                + ' ' + 'AND Number_of_Job = "8"'\
                + ' ' + 'AND IOdepth = "8"'\
                + ' ' + 'AND blocksize =' + a['Blocksize_2hist'] \
                + ' ' + 'AND Index_table.Key_ID =' + a['Table_Name_2hist_1'] + '.Key_ID' \
                + ' ' + 'UNION ALL' \
                + ' ' + 'SELECT Text_Table_Name, DRBD_Type,' + a['Select_Data_2hist'] + ' ' + 'FROM Index_table,' + a['Table_Name_2hist_2'] \
                + ' ' + 'WHERE Readwrite_type = "randwrite"' \
                + ' ' + 'AND Number_of_Job = "8"' \
                + ' ' + 'AND IOdepth = "8"' \
                + ' ' + 'AND blocksize =' + a['Blocksize_2hist'] \
                + ' ' + 'AND Index_table.Key_ID =' + a['Table_Name_2hist_2'] + '.Key_ID'
                         
    sql_result = cur.execute(SQL_Sentence)
    
    Text_Table = []
    drbd = []
    values = []

    for row in sql_result:
        Text_Table.append(row[0])
        drbd.append(row[1])
        values.append(row[2])
        print(row)
    # print (Text_Table)    
    # print (values)
    # print (drbd)

    
    plt.figure(figsize=(20,20), dpi = 100)
    bar_width = 0.3

    for i in range(len(drbd)):
        x_data = drbd[i]
        y_data = values[i]
        plt.bar(x_data, y_data, label = Text_Table[i], width = bar_width)
    
    plt.xlabel ('DRBD Type')
    plt.ylabel (a['Select_Data_2hist'])
    plt.xticks (rotation = 30)
    plt.title(a['Select_Data_2hist'] + ' ' + 'under Different DRBD Type (Blockszie =' + a['Blocksize_2hist'] + ')')
    plt.legend()
    plt.grid()
    
    # plt.savefig(a['Table_Name_2hist_1']-a['Table_Name_2hist_1']-a['Select_Data_2hist'].png)
    # plt.savefig('{Table_Names_1}-{Table_Names_2}-{Select_Data}.png', dpi = 200)
    plt.show()

    cur.close()
    con.commit()
    con.close()

def SQL_graph_output_3():

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

#     # Select_Data = input ('Please Enter the selected data you want(IOPS or MBPS):')
#     # Table_Names_1 = input ('Please Enter the Text Table Name 1:')
#     # Table_Names_2 = input ('Please Enter the Text Table Name 2:')
#     # Table_Names_3 = input ('Please Enter the Text Table Name 3:')
#     # Block_Size = input ('Please Enter the Block Size (4k or 1M):')
    
#     # SQL_Sentence = rf'''SELECT Text_Table_Name, DRBD_Type, {Select_Data} FROM Index_table, {Table_Names_1}
#     #                     WHERE Readwrite_type = "randwrite"
#     #                     AND Number_of_Job = "8"
#     #                     AND IOdepth = "8"
#     #                     AND blocksize = "{Block_Size}"
#     #                     AND Index_table.Key_ID = {Table_Names_1}.Key_ID
#     #                     UNION ALL
#     #                     SELECT Text_Table_Name, DRBD_Type, {Select_Data} FROM Index_table, {Table_Names_2}
#     #                     WHERE Readwrite_type = "randwrite"
#     #                     AND Number_of_Job = "8"
#     #                     AND IOdepth = "8"
#     #                     AND blocksize = "{Block_Size}"
#     #                     AND Index_table.Key_ID = {Table_Names_2}.Key_ID
#     #                     UNION ALL
#     #                     SELECT Text_Table_Name, DRBD_Type, {Select_Data} FROM Index_table, {Table_Names_3}
#     #                     WHERE Readwrite_type = "randwrite"
#     #                     AND Number_of_Job = "8"
#     #                     AND IOdepth = "8"
#     #                     AND blocksize = "{Block_Size}"
#     #                     AND Index_table.Key_ID = {Table_Names_3}.Key_ID
#                         '''

#     # SQL_Sentence = '''SELECT Text_Table_Name, DRBD_Type, MBPS FROM Index_table, Guangzhou_20210924_RAM
#     #                     WHERE Readwrite_type = "randwrite"
#     #                     AND Number_of_Job = "8"
#     #                     AND IOdepth = "8"
#     #                     AND blocksize = "1M"
#     #                     AND Index_table.Key_ID = Guangzhou_20210924_RAM.Key_ID
#     #                     UNION ALL
#     #                     SELECT Text_Table_Name, DRBD_Type, MBPS FROM Index_table, Taiwan_20210922_SDD
#     #                     WHERE Readwrite_type = "randwrite"
#     #                     AND Number_of_Job = "8"
#     #                     AND IOdepth = "8"
#     #                     AND blocksize = "1M"
#     #                     AND Index_table.Key_ID = Taiwan_20210922_SDD.Key_ID
#     #                     UNION ALL
#     #                     SELECT Text_Table_Name, DRBD_Type,MBPS FROM Index_table, Chengdu_20210928_RAM
#     #                     WHERE Readwrite_type = "randwrite"
#     #                     AND Number_of_Job = "8"
#     #                     AND IOdepth = "8"
#     #                     AND blocksize = "1M"
#     #                     AND Index_table.Key_ID = Chengdu_20210928_RAM.Key_ID
#     #                     '''
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)
    
    SQL_Sentence = 'SELECT Text_Table_Name, DRBD_Type,' + ' ' + a['Select_Data_3hist'] + ' ' + 'FROM Index_table,' +  a['Table_Name_3hist_1'] \
                + ' ' + 'WHERE Readwrite_type = "randwrite"'\
                + ' ' + 'AND Number_of_Job = "8"'\
                + ' ' + 'AND IOdepth = "8"'\
                + ' ' + 'AND blocksize =' + a['Blocksize_3hist'] \
                + ' ' + 'AND Index_table.Key_ID =' + a['Table_Name_3hist_1'] + '.Key_ID' \
                + ' ' + 'UNION ALL' \
                + ' ' + 'SELECT Text_Table_Name, DRBD_Type,' + a['Select_Data_3hist'] + ' ' + 'FROM Index_table,' + a['Table_Name_3hist_2'] \
                + ' ' + 'WHERE Readwrite_type = "randwrite"' \
                + ' ' + 'AND Number_of_Job = "8"' \
                + ' ' + 'AND IOdepth = "8"' \
                + ' ' + 'AND blocksize =' + a['Blocksize_3hist'] \
                + ' ' + 'AND Index_table.Key_ID =' + a['Table_Name_3hist_2'] + '.Key_ID' \
                + ' ' + 'UNION ALL' \
                + ' ' + 'SELECT Text_Table_Name, DRBD_Type,' + a['Select_Data_3hist'] + ' ' + 'FROM Index_table,' + a['Table_Name_3hist_3'] \
                + ' ' + 'WHERE Readwrite_type = "randwrite"' \
                + ' ' + 'AND Number_of_Job = "8"' \
                + ' ' + 'AND IOdepth = "8"' \
                + ' ' + 'AND blocksize =' + a['Blocksize_3hist'] \
                + ' ' + 'AND Index_table.Key_ID =' + a['Table_Name_3hist_3'] + '.Key_ID'
    
    sql_result = cur.execute(SQL_Sentence)
    
    Text_Table = []
    drbd = []
    values = []
    
    for row in sql_result:
        Text_Table.append(row[0])
        drbd.append(row[1])
        values.append(row[2])
        print(row)
#     # print (Text_Table)    
#     # print (values)
#     # print (drbd)

    plt.figure(figsize=(50,50), dpi = 100)
    bar_width = 0.3
    
    for i in range(len(drbd)):
        x_data = drbd[i]
        y_data = values[i]
        plt.bar(x_data, y_data, label = Text_Table[i], width = bar_width)
    
    plt.xlabel ('DRBD Type')
    plt.ylabel (a['Select_Data_3hist'])
    plt.xticks (rotation = 30)
    plt.title(a['Select_Data_3hist'] + ' ' + 'under Different DRBD Type (Blockszie =' + a['Blocksize_3hist'] + ')')
    plt.legend()
    plt.grid()

    # file_name = a['Table_Name_3hist_1'] + '-' + a['Table_Name_3hist_2'] + '-' + a['Table_Name_3hist_3'] + '-' + a['Select_Data_2hist']
    # plt.savefig(file_name)
    # plt.savefig(f'{Table_Names_1}-{Table_Names_2}-{Table_Names_3}-{Select_Data}.png', dpi = 00)
    plt.show()

    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
    SQL_printIndex()
    decide_number()
    # SQL_graph_output_2()
    # SQL_graph_output_3()