#!/usr/bin/python
import requests, sys
resp = 5
count = 0
#metrics = sys.argv[1]
r = requests.get(<...>,
                 headers={
                    "Content-Type": "application/json",
                    "X-Auth-Email": <...>,
                    "X-Auth-Key": "<...>}).json()
try:
    for resp1 in range(0, 10):
       for resp2 in range(0, 10):
           try:
#               print("5" + str(resp1) + str(resp2) + ": " + str(r['result']['totals']['requests']['http_status'][str(resp) + str(resp1) + str(resp2)]))
               count += r['result']['totals']['requests']['http_status'][str(resp) + str(resp1) + str(resp2)]
           except Exception:
               pass
except Exception:
    pass
print(count)
#print(r['result']['totals']['requests']['http_status'])
#print(r['result']['totals']['bandwidth']['all'])
#print(r['result']['totals']['pageviews']['all'])
#print(r['result']['totals']['uniques']['all'])



