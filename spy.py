import requests
import json
import datetime
import csv
import mysql.connector
from mysql.connector import errorcode
import time
from colorama import Fore, Style, init


init()
# goto = s.get("https://cinqo.de/products.json")

# print(goto.text)

# while True:
#     goto = s.get("https://cinqo.de/products.json")
#     print(goto.text)
#     time.sleep(5)

product_change = {}

print(Fore.LIGHTBLUE_EX+'>>>>> | Started Monitoring | <<<<<'+Style.RESET_ALL)

def oraAttuale():
    return datetime.datetime.strftime(datetime.datetime.now(), "%d/%m/%Y, %H:%M:%S")

while True:
    with open ("statis/file/storex.txt") as f:
        stores = f.readlines()
        for s in stores:
            try:
                goto = requests.get("https://"+s.replace("\n", "")+"/products.json")
            except Exception:
                continue

            try:
                j = json.loads(goto.text)
            except Exception as e:
                print(e)
                continue

            products = j['products']
            for p in products:
                data = p['updated_at']
                date_time_obj = datetime.datetime.fromisoformat(data)
                prod_id = p['id']
                store = s.replace("\n", "")
                prod_name = p['title']
                ora = datetime.datetime.strftime(date_time_obj, "%Y/%m/%d %H:%M:%S")
                # print(Fore.BLUE+"Product: "+Style.RESET_ALL+prod_name+Fore.BLUE+" Last Sale: "+Style.RESET_ALL+ora)
                
                if(prod_id in product_change and product_change[prod_id] != data):
                    print("New Sale for Product: "+Fore.GREEN+prod_name+Style.RESET_ALL+" "+oraAttuale())
                    product_change[prod_id] = data

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

                            mycursor = conn.cursor()
                            sql = "INSERT INTO sales (store_name, prod_name, prod_id, sale_time) VALUES (%s, %s, %s, %s)"
                            val = (store, prod_name, prod_id, ora)
                            mycursor.execute(sql,val)
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

                else:
                    product_change[prod_id] = data



                




        time.sleep(5)

