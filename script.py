import csv
import json
import hashlib
import pandas as pd
 
#convert csv to json
def make_json(csvFilePath, jsonFilePath):
    data_dict = {}
    # open csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
      csvReader = csv.DictReader(csvf)
      for rows in csvReader:
        key=rows['No']
        data_dict[key]=rows
    #open json writer and use json.dumps() to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
      jsonf.write(json.dumps(data_dict,indent=4))

csvFilePath=input('Enter the absolute path of the csv file')
jsonFilePath=input('Enter the absolute path of the json file')

make_json(csvFilePath,jsonFilePath)

#calculate sha256
filename = "CHIP-0007.json"
sha256_hash = hashlib.sha256()
with open(filename,'rb')as f:
  for byte_block in iter(lambda: f.read(4096),b""):
    sha256_hash.update(byte_block)
  print (sha256_hash.hexdigest())

#append sha256 to csv line
df = pd.read_csv(csvFilePath)
df["sha256"] = (sha256_hash.hexdigest())
df.to_csv(csvFilePath+ ".output.csv", index=False)





