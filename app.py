import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
     
payload = json.dumps({
  "ime": "Magdalena",
  "prezime": "Vasic",
  "smer": "RI",
  "godina":3,
  "predmeti":[
   {
    "ime": "PDS",
    "espb": 6
   },
   {
     "ime": "NRS",
     "espb": 6
   } ]
})

headers = {
  'Content-Type': 'application/json'
}


def testFunction():
  print("testing...")



conn.request("POST", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data)

conn.request("POST", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data)

