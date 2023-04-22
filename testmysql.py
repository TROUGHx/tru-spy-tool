import mysql.connector
from mysql.connector import errorcode


try:
    conn = mysql.connector.connect(
    host="db4free.net",
    user="truspytool",
    port="3306",
    password="Trucepro123.",
    database="truspytool",
    auth_plugin='mysql_native_password'
    )

    if(conn.is_connected()):
        print("Connesso!")

        mycursor = conn.cursor()
        mySql_insert_query = """INSERT INTO sales (store_name, prod_name, prod_id, sale_time) 
                                VALUES 
                                ('cinqo', 'zattera', 54546565, '2023-04-22 01:58:33') """
        mycursor.execute(mySql_insert_query)
        conn.commit()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("something is wrong with your username or  password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database does not exist")
    
    else:
        print(err)
else:
    conn.close()




# try:
#     mySql_insert_query = """INSERT INTO sales (store_name, prod_name, prod_id) 
#                            VALUES 
#                            ('cinqo', 'zattera', 54546565) """

#     cursor = conn.cursor()
#     cursor.execute(mySql_insert_query)
#     conn.commit()
#     print(cursor.rowcount, "Record inserted successfully into Laptop table")
#     cursor.close()

# except mysql.connector.Error as error:
#     print("Failed to insert record into Laptop table: {}".format(error))

# finally:
#     if conn.is_connected():
#         conn.close()
#         print("MySQL connection is closed")
    


