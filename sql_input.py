import re
import os
import os.path
import sys
import sqlite3
import yaml

LIST_DATA = []
TABLE_NAME = ""
KEY_ID = ""

def inputfile():
    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)
    
    # file_input = input('Please Enter the name of the txt file:')    # Input the file name of fio test
    file_input = a['file input']
    # 07_27_18_06_results.txt
    # 08_04_05_17_results.txt
    # 08_06_05_23_results.txt
    # 1.log
    # 08_11_08_03_results.txt
    if not os.path.exists (file_input):
        print ("The file is not existed. Please Enter the right txt file in yaml configuration.")
        sys.exit()

    file = open(file_input,'r')
    results = file.read()
    re_=r'([a-zA-Z0-9_]+)_([a-zA-Z0-9]+)_([a-zA-Z0-9]+)_(\d+)_(\d+).*\s*.*IOPS=([a-zA-Z0-9.]+).*\s*.*B/s\s\((.+/s)\)' # Regular Expression
    re_pattern = re.compile(re_)
    re_result = re_pattern.findall(results)

    for i in re_result:
        LIST_DATA.append(list(i))
    # for data in list_data:
    #     print(data)
    
    file.close()

def handle_iops():
    for data in LIST_DATA:
        # print (data)
        iops_value = data[5]
        # print (iops_value)
        if iops_value == '':
            data[5]= ''
        elif iops_value[-1]=='k': 
            IOPS_k = float(float(iops_value[:-1]) * 1000)
            data[5] = IOPS_k
        else:
            IOPS_r = float(iops_value)
            data[5] = IOPS_r
        # print (data)
        # print (data[5])
        # print (type(data[5]))

def handle_mbps():
    for data in LIST_DATA:
        mbps_value = data[6]
        if mbps_value == '':
            data[6]= ''
            # print (mbps_value)
        elif mbps_value[3:][-4:] == 'kB/s': 
            MBPS_k = float(mbps_value[:-4]) / 1000
            MBPS_k = float("%.2f" % MBPS_k)
            data[6]= MBPS_k
        elif mbps_value[3:][-4:] == 'GB/s':
            MBPS_g = float((mbps_value[:-4]))*1.07
            MBPS_g = float("%.1f" % MBPS_g)
            MBPS_g = int(MBPS_g*1000)
            data[6]= MBPS_g
        else:
            MBPS_r = float(mbps_value[:-4]) 
            data[6]= MBPS_r
        # print (data)
        # print (data[6])
        # print (type(data[3]))

def sql_index_input():

    a_yaml_file = open('sql_config.yml')
    a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    try:
        cur.execute('''CREATE TABLE Index_Table
                        (Key_ID integer,
                        Client_Name text,
                        Date text,
                        Disk_Type text,
                        Text_Table_Name text
                        )''')
    except:
        print('Table already exist！')

    query = '''INSERT INTO Index_Table (Key_ID, Client_Name, Date, Disk_Type, Text_Table_Name) values (?, ?, ?, ?, ?)'''

    # Key_ID = input ('Please enter a Key ID:')
    # Client_Name = input ('Please enter the Client Name:')
    # Date = input('Please enter the date:(format example:20210101):')
    # Disk_Type = input ('Please enter the Disk Type:')
    
    try:
        key_ID = int(a['Key ID'])
    except ValueError:
        print ("Please enter a NUMBER for Key ID")
        sys.exit()
    
    client_name = a['Client Name']
    date = a['Date']
    disk_type = a['Disk Type']
    text_table_name = (client_name + '_' + date + '_' + disk_type)

    global TABLE_NAME 
    TABLE_NAME = text_table_name
    global KEY_ID
    KEY_ID = key_ID

    values = (key_ID, client_name, date, disk_type, text_table_name)

    try: 
        cur.execute (query,values)
    except sqlite3.IntegrityError:
        print ("The key ID is repeated. Please check the Index Table and re-enter.")
        sys.exit()
    
    sql_result = cur.execute('SELECT * FROM Index_Table')

    columnlist = []
    for column in sql_result.description:
        columnlist.append(column[0])
    print (columnlist)
    
    for row in sql_result:
        print (row)

    cur.close()
    con.commit()
    con.close()


def sql_text_input():
    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object
    
    try:
        cur.execute(f'''CREATE TABLE {TABLE_NAME}
                        (Key_ID integer,
                        DRBD_type text,
                        Readwrite_type text,
                        blocksize text,
                        Number_of_Job text,
                        IOdepth text,
                        IOPS real,
                        MBPS real
                        )''')
        
        print(TABLE_NAME)
    
        query = f'''INSERT INTO {TABLE_NAME} (Key_ID, DRBD_type, Readwrite_type, blocksize, Number_of_Job, IOdepth, IOPS, MBPS) values (?,?,?,?,?,?,?,?)'''

        for data in LIST_DATA:      
            Key_ID = KEY_ID
            DRBD_type = data[0]
            Readwrite_type = data[1]
            blocksize = data[2]
            Number_of_Job = data[3]
            IOdepth = data[4]
            IOPS = data[5]
            MBPS = data[6]

            values = (Key_ID, DRBD_type, Readwrite_type, blocksize, Number_of_Job, IOdepth, IOPS, MBPS)

            cur.execute(query, values)

            sql_result = cur.execute(f'SELECT * FROM {TABLE_NAME}')
            

        columnlist = []
        for column in sql_result.description:
            columnlist.append(column[0])
        print (columnlist)

        for row in sql_result:
            print (row)

        cur.close()
        con.commit()
        con.close()

    except:
        print('Table already exist！')

if __name__ == '__main__':
    inputfile()
    handle_iops()
    handle_mbps()
    sql_index_input()
    sql_text_input()
