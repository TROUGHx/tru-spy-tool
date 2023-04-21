import requests
import json
import datetime
import csv
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
    with open ("storex.txt") as f:
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
                ora = datetime.datetime.strftime(date_time_obj, "%d/%m/%Y, %H:%M:%S")
                # print(Fore.BLUE+"Product: "+Style.RESET_ALL+prod_name+Fore.BLUE+" Last Sale: "+Style.RESET_ALL+ora)
                
                if(prod_id in product_change and product_change[prod_id] != data):
                    print("New Sale for Product: "+Fore.GREEN+prod_name+Style.RESET_ALL+" "+oraAttuale())
                    product_change[prod_id] = data

                    with open('sales.csv', 'a', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        data = [store,prod_id, prod_name, oraAttuale()]
                        writer.writerow(data)
                else:
                    product_change[prod_id] = data



                




        time.sleep(5)

