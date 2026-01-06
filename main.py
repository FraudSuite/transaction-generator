from fastapi import FastAPI, WebSocket
import asyncio
import numpy as np
import time
from pathlib import Path
import pandas as pd
import random
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()



origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)




df = pd.read_csv("test.csv")

indexs = df[df['Class'] == 1].index.tolist() + df[df['Class'] == 0].head(60).index.tolist()

data = [
{"country":"USA","city":"New York","merchant":"Coffee Shop","card_last4":4532},
{"country":"USA","city":"Chicago","merchant":"Grocery Store","card_last4":8891},
{"country":"UAE","city":"Dubai","merchant":"Electronics Store","card_last4":3321},
{"country":"UK","city":"London","merchant":"Restaurant","card_last4":7712},
{"country":"USA","city":"Los Angeles","merchant":"Gas Station","card_last4":5521},
{"country":"Japan","city":"Tokyo","merchant":"Online Store","card_last4":6612},
{"country":"France","city":"Paris","merchant":"Coffee Shop","card_last4":9021},
{"country":"Canada","city":"Toronto","merchant":"Bookstore","card_last4":1256},
{"country":"Australia","city":"Sydney","merchant":"Pharmacy","card_last4":6182},
{"country":"Germany","city":"Berlin","merchant":"Clothing Store","card_last4":4419},

{"country":"USA","city":"New York","merchant":"Cinema","card_last4":5591},
{"country":"USA","city":"Los Angeles","merchant":"Restaurant","card_last4":8231},
{"country":"UAE","city":"Dubai","merchant":"Hotel","card_last4":4441},
{"country":"Japan","city":"Tokyo","merchant":"Online Store","card_last4":2278},
{"country":"USA","city":"Chicago","merchant":"Gas Station","card_last4":7712},
{"country":"France","city":"Paris","merchant":"Grocery Store","card_last4":9090},
{"country":"UK","city":"London","merchant":"Electronics Store","card_last4":6812},
{"country":"Germany","city":"Berlin","merchant":"Coffee Shop","card_last4":9081},
{"country":"Japan","city":"Tokyo","merchant":"Pharmacy","card_last4":3231},
{"country":"Australia","city":"Sydney","merchant":"Restaurant","card_last4":5521},

{"country":"Canada","city":"Toronto","merchant":"Subscription Service","card_last4":2109},
{"country":"USA","city":"New York","merchant":"Bookstore","card_last4":8712},
{"country":"USA","city":"Los Angeles","merchant":"Coffee Shop","card_last4":4492},
{"country":"USA","city":"Chicago","merchant":"Grocery Store","card_last4":5520},
{"country":"UAE","city":"Dubai","merchant":"Electronics Store","card_last4":6612},
{"country":"France","city":"Paris","merchant":"Pharmacy","card_last4":1234},
{"country":"Japan","city":"Tokyo","merchant":"Clothing Store","card_last4":1129},
{"country":"Germany","city":"Berlin","merchant":"Cinema","card_last4":9981},
{"country":"Australia","city":"Sydney","merchant":"Online Store","card_last4":7211},
{"country":"UK","city":"London","merchant":"Gas Station","card_last4":8911},

{"country":"USA","city":"New York","merchant":"Hotel","card_last4":4410},
{"country":"USA","city":"Los Angeles","merchant":"Coffee Shop","card_last4":3222},
{"country":"Germany","city":"Berlin","merchant":"Clothing Store","card_last4":1144},
{"country":"Canada","city":"Toronto","merchant":"Bookstore","card_last4":5421},
{"country":"USA","city":"Chicago","merchant":"Grocery Store","card_last4":1881},
{"country":"France","city":"Paris","merchant":"Restaurant","card_last4":6610},
{"country":"UAE","city":"Dubai","merchant":"Electronics Store","card_last4":8812},
{"country":"UK","city":"London","merchant":"Coffee Shop","card_last4":2345},
{"country":"Japan","city":"Tokyo","merchant":"Pharmacy","card_last4":9982},
{"country":"Australia","city":"Sydney","merchant":"Cinema","card_last4":2267},

{"country":"Germany","city":"Berlin","merchant":"Online Store","card_last4":1120},
{"country":"Canada","city":"Toronto","merchant":"Coffee Shop","card_last4":4421},
{"country":"USA","city":"Los Angeles","merchant":"Restaurant","card_last4":5612},
{"country":"USA","city":"New York","merchant":"Gas Station","card_last4":7234},
{"country":"France","city":"Paris","merchant":"Clothing Store","card_last4":8811},
{"country":"Australia","city":"Sydney","merchant":"Pharmacy","card_last4":8821},
{"country":"USA","city":"Chicago","merchant":"Bookstore","card_last4":3312},
{"country":"Japan","city":"Tokyo","merchant":"Coffee Shop","card_last4":5551},
{"country":"UAE","city":"Dubai","merchant":"Electronics Store","card_last4":9912},
{"country":"UK","city":"London","merchant":"Restaurant","card_last4":1123},

{"country":"USA","city":"Boston","merchant":"Coffee Shop","card_last4":4021},
{"country":"USA","city":"Miami","merchant":"Gas Station","card_last4":5523},
{"country":"USA","city":"Houston","merchant":"Grocery Store","card_last4":7721},
{"country":"USA","city":"Dallas","merchant":"Pharmacy","card_last4":9901},
{"country":"USA","city":"Seattle","merchant":"Bookstore","card_last4":8112},
{"country":"USA","city":"San Francisco","merchant":"Tech Store","card_last4":2211},
{"country":"USA","city":"Atlanta","merchant":"Clothing Store","card_last4":3344},
{"country":"USA","city":"Detroit","merchant":"Coffee Shop","card_last4":4423},
{"country":"USA","city":"Philadelphia","merchant":"Restaurant","card_last4":7833},
{"country":"USA","city":"Phoenix","merchant":"Gas Station","card_last4":9122},

{"country":"USA","city":"Denver","merchant":"Online Store","card_last4":6677},
{"country":"USA","city":"Portland","merchant":"Grocery Store","card_last4":5566},
{"country":"USA","city":"Las Vegas","merchant":"Hotel","card_last4":4433},
{"country":"Canada","city":"Vancouver","merchant":"Coffee Shop","card_last4":7344},
{"country":"Canada","city":"Montreal","merchant":"Restaurant","card_last4":8842},
{"country":"Canada","city":"Calgary","merchant":"Gas Station","card_last4":1198},
{"country":"Canada","city":"Ottawa","merchant":"Pharmacy","card_last4":5213},
{"country":"Canada","city":"Quebec City","merchant":"Bookstore","card_last4":7452},
{"country":"Canada","city":"Winnipeg","merchant":"Clothing Store","card_last4":6614},
{"country":"Canada","city":"Edmonton","merchant":"Electronics Store","card_last4":9321},

{"country":"UK","city":"Manchester","merchant":"Coffee Shop","card_last4":4311},
{"country":"UK","city":"Liverpool","merchant":"Grocery Store","card_last4":8941},
{"country":"UK","city":"Birmingham","merchant":"Restaurant","card_last4":1201},
{"country":"UK","city":"Bristol","merchant":"Gas Station","card_last4":7841},
{"country":"UK","city":"Leeds","merchant":"Pharmacy","card_last4":9342},
{"country":"UK","city":"Nottingham","merchant":"Clothing Store","card_last4":2314},
{"country":"UK","city":"Sheffield","merchant":"Online Store","card_last4":6723},
{"country":"UK","city":"Newcastle","merchant":"Cinema","card_last4":5561},
{"country":"UK","city":"Oxford","merchant":"Bookstore","card_last4":8123},
{"country":"UK","city":"Cambridge","merchant":"Coffee Shop","card_last4":3341},

{"country":"Germany","city":"Hamburg","merchant":"Restaurant","card_last4":8911},
{"country":"Germany","city":"Munich","merchant":"Gas Station","card_last4":9981},
{"country":"Germany","city":"Frankfurt","merchant":"Bookstore","card_last4":2213},
{"country":"Germany","city":"Stuttgart","merchant":"Pharmacy","card_last4":6123},
{"country":"Germany","city":"Düsseldorf","merchant":"Clothing Store","card_last4":7842},
{"country":"Germany","city":"Dresden","merchant":"Online Store","card_last4":9921},
{"country":"Germany","city":"Leipzig","merchant":"Grocery Store","card_last4":1233},
{"country":"Germany","city":"Cologne","merchant":"Coffee Shop","card_last4":6781},
{"country":"Germany","city":"Hannover","merchant":"Restaurant","card_last4":4412},
{"country":"Germany","city":"Bonn","merchant":"Gas Station","card_last4":8731},

{"country":"France","city":"Lyon","merchant":"Bookstore","card_last4":2221},
{"country":"France","city":"Marseille","merchant":"Restaurant","card_last4":3241},
{"country":"France","city":"Nice","merchant":"Coffee Shop","card_last4":9980},
{"country":"France","city":"Toulouse","merchant":"Pharmacy","card_last4":4852},
{"country":"France","city":"Nantes","merchant":"Grocery Store","card_last4":1132},
{"country":"France","city":"Bordeaux","merchant":"Clothing Store","card_last4":5541},
{"country":"France","city":"Cannes","merchant":"Hotel","card_last4":2212},
{"country":"France","city":"Strasbourg","merchant":"Coffee Shop","card_last4":8732},
{"country":"France","city":"Lille","merchant":"Restaurant","card_last4":9911},
{"country":"France","city":"Grenoble","merchant":"Gas Station","card_last4":4488},

{"country":"Japan","city":"Osaka","merchant":"Coffee Shop","card_last4":3322},
{"country":"Japan","city":"Nagoya","merchant":"Bookstore","card_last4":5611},
{"country":"Japan","city":"Sapporo","merchant":"Pharmacy","card_last4":2209},
{"country":"Japan","city":"Fukuoka","merchant":"Restaurant","card_last4":4502},
{"country":"Japan","city":"Kyoto","merchant":"Grocery Store","card_last4":7722},
{"country":"Japan","city":"Kobe","merchant":"Gas Station","card_last4":9821},
{"country":"Japan","city":"Hiroshima","merchant":"Electronics Store","card_last4":6681},
{"country":"Japan","city":"Sendai","merchant":"Coffee Shop","card_last4":3311},
{"country":"Japan","city":"Yokohama","merchant":"Clothing Store","card_last4":9983},
{"country":"Japan","city":"Kawasaki","merchant":"Restaurant","card_last4":5527},

{"country":"Australia","city":"Melbourne","merchant":"Pharmacy","card_last4":2281},
{"country":"Australia","city":"Brisbane","merchant":"Grocery Store","card_last4":6671},
{"country":"Australia","city":"Perth","merchant":"Gas Station","card_last4":8841},
{"country":"Australia","city":"Adelaide","merchant":"Bookstore","card_last4":4415},
{"country":"Australia","city":"Gold Coast","merchant":"Restaurant","card_last4":1299},
{"country":"Australia","city":"Canberra","merchant":"Coffee Shop","card_last4":4312},
{"country":"Australia","city":"Darwin","merchant":"Clothing Store","card_last4":5581},
{"country":"Australia","city":"Hobart","merchant":"Electronics Store","card_last4":9917},
{"country":"Australia","city":"Geelong","merchant":"Gas Station","card_last4":3291},
{"country":"Australia","city":"Townsville","merchant":"Online Store","card_last4":7741},

{"country":"UAE","city":"Abu Dhabi","merchant":"Restaurant","card_last4":2291},
{"country":"UAE","city":"Sharjah","merchant":"Coffee Shop","card_last4":6615},
{"country":"UAE","city":"Ajman","merchant":"Clothing Store","card_last4":2201},
{"country":"UAE","city":"Fujairah","merchant":"Bookstore","card_last4":6677},
{"country":"UAE","city":"Ras Al Khaimah","merchant":"Grocery Store","card_last4":1127},
{"country":"UAE","city":"Al Ain","merchant":"Gas Station","card_last4":8975},
{"country":"UAE","city":"Dubai","merchant":"Electronics Store","card_last4":5511},
{"country":"UAE","city":"Abu Dhabi","merchant":"Cinema","card_last4":7231},
{"country":"UAE","city":"Sharjah","merchant":"Pharmacy","card_last4":9123},
{"country":"UAE","city":"Dubai","merchant":"Restaurant","card_last4":4882}
]




def generate_tx():
	# row = df.sample(1).iloc[0].to_dict()
	row = df.iloc[random.choice(indexs)].to_dict()
	row_data = random.choice(data)
	row["merchant"] = row_data["merchant"]
	row["country"] = row_data["country"]
	row["city"] = row_data["city"]
	row["card_last4"] = row_data["card_last4"]
	row["txn_id"] = f"TXN-{random.randint(10000, 99999)}"
	row["amount"] = random.randint(50, 1000000)
	row["stream_time"] = int(time.time())
	return row


@app.websocket("/stream")
async def stream(ws: WebSocket):
	await ws.accept()
	print("Fraud service connected to generator")

	while True:
		tx = generate_tx()
		await ws.send_json(tx)
		await asyncio.sleep(20)