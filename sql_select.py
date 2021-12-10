import sqlite3
import csv
from prettytable.prettytable import from_db_cursor
import yaml

def sql_print_index():
    
    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    cur.execute('SELECT * From Index_Table')
    
    x = from_db_cursor(cur)
    print (x)

    cur.close()
    con.commit()
    con.close()

def sql_analysis_output():

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
    sql_sentence = 'select'+' '+a['wanted data']+' '+'from'+' '+a['table'] +' '+'where'+' '+a['statement']
    # sql_result = cur.execute((sql_sentence))

    cur.execute((sql_sentence))
    
    x = from_db_cursor(cur)
    print(x)

    # columnlist = []
    # for column in sql_result.description:
    #     columnlist.append(column[0])
    # print (columnlist)

    # for row in sql_result:
    #     print (row)

    Excel_filename = input ('Please Enter the name of the Excel file will be created:')
    
    cur.execute(sql_sentence)
    with open(f"{Excel_filename}.csv","w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)

    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
    sql_print_index()
    sql_analysis_output()