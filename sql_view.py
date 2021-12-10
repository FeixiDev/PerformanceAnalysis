import sqlite3
from prettytable.prettytable import from_db_cursor
import yaml
from prettytable import PrettyTable

def sql_print_index():
    
    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    cur.execute('SELECT * From Index_Table')

    x = from_db_cursor(cur)
    print(x)

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
        cur.execute(sql_sentence)
        
        x = from_db_cursor(cur)

        print (a['table view'][i])
        print (x)

    cur.close()
    con.commit()
    con.close()


if __name__ == '__main__':
    sql_print_index()
    sql_test()