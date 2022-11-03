import copy
import csv
import json
import hashlib
import pandas as pd
from pathlib import Path
import os

jsonoutputlist=[]
#convert csv to json
def make_json(csvFilePath, jsonFilePath):
    # open csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
      csvReader = csv.DictReader(csvf, fieldnames=("No","Name","Hash","UUID"))
      #open json writer and use json.dumps() to dump data
      for row in csvReader:
        out=json.dumps(row, indent=4)
        n=json.loads(out)
        myData = {'format' : 'CHIP-0007'}
        myData.update(row)
        jsonoutput = open(jsonFilePath+'\\'+str(n['No'])+'.json','w')
        jsonoutput.write(out)
    jsonoutput.close()
    csvf.close()


csvFilePath=input('Enter the absolute path of the csv file')
jsonFilePath=input('Enter the absolute path of the json file')

  # calculate sha256
FilePath = "CHIP-0007.json"
sha256_hash = hashlib.sha256()
with open(FilePath,'rb')as f:
  for byte_block in iter(lambda: f.read(4096),b""):
    sha256_hash.update(byte_block)
  print (sha256_hash.hexdigest())

  # #append sha256 to csv line
  df = pd.read_csv(csvFilePath)
  df["sha256"] = (sha256_hash.hexdigest())
  df.to_csv(csvFilePath+ ".output.csv", index=False)

make_json(csvFilePath,jsonFilePath)









