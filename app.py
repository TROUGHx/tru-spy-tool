from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_api import status
import json
import csv

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = "Content-Origin"



@app.route("/")
def home():
	return render_template('index.html')

@app.route('/addsite/<name>')
def addsite(name):

	sitiFile = []

	with open("storex.txt", "r") as f:
		righe = f.readlines()
		for l in righe:
			sitiFile.append(l)
		
		if(name not in sitiFile):
			with open ("storex.txt", 'a') as f:
				f.write('\n')
				f.write(str(name))
				return "added: "+str(name)

		return "gia presente"


def removesite(name):

	sitiFile = []

	with open("storex.txt", "r+") as f:
		righe = f.readlines()
		for l in righe:
			if(l == name):
				sitiFile.append(l)
			else:
				print("")
			
		

		return "gia presente"


@app.route("/report/<sito>")	
def report(sito):
	report_print = []

	with open ("sales.csv") as f:
		csv_reader = csv.DictReader(f)

		for row in csv_reader:

			store = row['STORE']
			prod_id = row['PROD_ID']
			prod = row['PROD_NAME']
			time = row['TIME']
			if store == sito:
				report_json = {
					"Store": store,
					"Prodotto": prod,
					"ID Prodotto": prod_id,
					"Time": time
				}

				report_print.append(report_json)

		return jsonify(report_print)


		
		
		


	

if __name__ == "__main__":
	app.run()
