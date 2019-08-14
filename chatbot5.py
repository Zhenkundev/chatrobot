bot_template = "BOT : {0}"
user_template = "USER : {0}"
import requests
import json
from chatbot0 import interpreter


message = "show me the tsla"
entities = interpreter.parse(message)["entities"]
ent_vals = [e["value"] for e in entities]
ent_ents = [e["entity"] for e in entities]
a = 'https://cloud.iexapis.com/stable/stock/{0}/quote?token=pk_77f74e3b59e54d43b48e72de351caaf0'
r = requests.get(a.format(ent_vals[0]))
e = r.text
data = json.loads(e)
