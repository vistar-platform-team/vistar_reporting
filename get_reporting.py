
import json
import requests
import sys
import datetime
import time
import csv
import os
  
  
def get_session_cookie(options):
   session_url = options['session_url']
   payload = {k: options[k] for k in ["email", "password"]}
   r = requests.post(session_url, data=json.dumps(payload))
   return r.cookies
  
def get_report_with_options(options, cookie):
   url = options['url']
   data = options['report_data']
   print data
   # data = {
   #    "start": "2016-06-06T00:00:00-04:00",
   #    "end":  "2016-07-03T23:59:59-04:00",
   #    "metrics": ["impressions", "spots"],
   #    "timezone": "America/New_York",
   #    "filters": {
   #       "buy_type": ["direct","bonus"],
   #       "insertion_order":["YS-ShnAeQdiYqs035FJ6Rg"],
   #       "campaign":["1M1AvcRCQX-FSywWESxtKQ"]
   #    },
   #    "groups":["venue_name","zip","date","hour_of_day"]
   # }

   print "running report"
   r = requests.post(url,cookies=cookie, data=json.dumps(data))
   return r
  
def convert_to_csv(data):
   raw_results_json = data.json()['rows']
   numRows = len(raw_results_json['impressions'])

   rows = []
   
   headerRow = raw_results_json.keys()

   rows.append(headerRow)

   for i in range (0,numRows-1):
      rowCurr = []
      for column in raw_results_json:
         rowCurr.append(raw_results_json[column][i])
      rows.append(rowCurr)

   with open('results.csv', 'wb+') as f:
         writer = csv.writer(f, rows[0], quoting=csv.QUOTE_ALL)         
         for i in range (0,numRows-1):
            writer.writerow(rows[i])

def run_reports(options):
   cookie = get_session_cookie(options)
   data = get_report_with_options(options, cookie)
   convert_to_csv(data)
  
def init():
   try:
    file_name = sys.argv[1]
   except:
      print "USAGE: python get_reporting.py JSON_FILE"
      sys.exit(1)
   
   run_reports(json.load(open(file_name)))
  
  
if __name__ == "__main__":
   init()