# coding: utf-8
import Index as index
import SQL_input as sqlin
import SQL_select as sqlsel
import SQL_select_two_table as sqlsel2
import SQL_chart as sqlchart
import SQL_histogram as sqlhis
import SQL_deviation as sqldevi
import SQL_deviation_1standard as sqldevi1
import yaml

# typein = input("(input/analysis/graph/deviation):")

def main():
    # a_yaml_file = open('sql_config.yml')
    # a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)

    index.SQL_printIndex()
    
    typein = input("What kind of function do you want to use? (input/analysis/graph/deviation):")
    # typein = a['typein']
    if typein == "input":
        sqlin.inputfile()
        sqlin.handle_mbps()
        sqlin.handle_iops()
        sqlin.SQL_index_input()
        sqlin.SQL_text_input()
    
    elif typein == "analysis":
        number_of_table = input("How many tables do you want to analyze with? (1 or 2):")
        # number_of_table = a['number of table']
        if number_of_table  == "1":
            sqlsel.SQL_printIndex()
            sqlsel.SQL_analysis_output()
        if number_of_table  == "2":
            sqlsel2.SQL_printIndex()
            sqlsel2.SQL_analysis_output()()
    
    elif typein == "graph":
        graph = input("What kind of graph do you want to create? (chart or histogram):")
        if graph == "chart":
            sqlchart.SQL_printIndex()
            sqlchart.SQL_graph_output()
        if graph == "histogram":
            sqlhis.SQL_printIndex()
            graph_number = input ("How many table do you want to create histogram with? (2 or 3):")
            if graph_number == "2":
                sqlhis.SQL_graph_output_2()
            if graph_number == "3":
                sqlhis.SQL_graph_output_3()
    
    elif typein == "deviation":
        deviation = input("What kind of deviation do you want to create? (multiple standards or 1 standard)")
        if deviation == "multiple standards":
            sqldevi.SQL_printIndex()
            sqldevi.SQL_pick_standard_values()
            sqldevi.SQL_pick_example_values()
            sqldevi.draw()
        if deviation == "1 standard":
            sqldevi1.SQL_printIndex()
            sqldevi1.SQL_pick_standard_values()
            sqldevi1.SQL_pick_example_values()
            sqldevi1.draw()
    
    elif typein not in ["input", "analysis", "graph", "deviation"]:
        print("Not a vaild keyword. Please Enter again.")
        main()

if __name__ == '__main__':
    main()