import sqlite3

def SQL_printIndex():
    
    con = sqlite3.connect ('sqldatabase_test.db') # create connection object and database file
    cur = con.cursor() # create a cursor for connection object

    data = cur.execute('SELECT * From Index_Table')

    column_list = []
    for column in data.description:
        column_list.append(column[0])
    print(column_list)
    
    for row in data:
        print (row)

    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
    SQL_printIndex()