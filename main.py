# coding: utf-8
import index as index
import sql_input as sqlin
import sql_select as sqlsel
import sql_select_two_table as sqlsel2
import sql_chart as sqlchart
import sql_histogram as sqlhis
import sql_deviation as sqldevi
import sql_deviation_1standard as sqldevi1
import sql_view as sqlview
import sql_manage as sqlman
import yaml
import sqlite3

# typein = input("(input/analysis/graph/deviation):")

def main():
    # a_yaml_file = open('sql_config.yml')
    # a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    try:
        index.sql_print_index()
    except sqlite3.OperationalError:
        print("Please input FIO result text file name and other information in Yaml configuraion for input.py first AND THEN ENTER input in the next question")

    typein = input("What kind of function do you want to use? (view/input/analysis/graph/deviation/manage):")
    # typein = a['typein']
    if typein == "input":
        sqlin.inputfile()
        sqlin.handle_mbps()
        sqlin.handle_iops()
        sqlin.sql_index_input()
        sqlin.sql_text_input()
    
    elif typein == "analysis":
        number_of_table = input("How many tables do you want to analyze with? (1 or 2):")
        # number_of_table = a['number of table']
        if number_of_table  == "1":
            sqlsel.sql_print_index()
            sqlsel.sql_analysis_output()
        if number_of_table  == "2":
            sqlsel2.sql_print_index()
            sqlsel2.sql_analysis_output()
    
    elif typein == "graph":
        graph = input("What kind of graph do you want to create? (chart or histogram):")
        if graph == "chart":
            sqlchart.sql_print_index()
            sqlchart.sql_graph_output()
        if graph == "histogram":
            sqlhis.sql_print_index()
            graph_number = input ("How many table do you want to create histogram with? (2 or 3):")
            if graph_number == "2":
                sqlhis.sql_graph_output_2()
            if graph_number == "3":
                sqlhis.sql_graph_output_3()
    
    elif typein == "deviation":
        deviation = input("What kind of deviation do you want to create? (multiple standards or 1 standard)")
        if deviation == "multiple standards":
            sqldevi.sql_print_standard_drbd()
            sqldevi.sql_pick_standard_values()
            sqldevi.sql_print_example_drbd()
            sqldevi.sql_pick_example_values()
            sqldevi.draw()
        if deviation == "1 standard":
            sqldevi1.sql_print_standard_drbd()
            sqldevi1.sql_pick_standard_values()
            sqldevi1.sql_print_example_drbd()
            sqldevi1.sql_pick_example_values()
            sqldevi1.draw()

    elif typein == "view":
        sqlview.sql_print_index()
        sqlview.num_test()
    
    elif typein == "manage":
        sqlman.drop_table()
        sqlman.drop_row()
    
    elif typein not in ["input", "analysis", "graph", "deviation", "view", "manage"]:
        print("Not a vaild keyword. Please Enter again.")
        main()

if __name__ == '__main__':
    main()