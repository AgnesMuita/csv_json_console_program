import copy
import csv
import json
import hashlib
import pandas as pd
from pathlib import Path
import os

#create a directory to store the generate the json files
def create_directory(directory):
  parent_dir = os.getcwd()
  if not os.path.exists("nftjsonfiles"):
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
create_directory("nftjsonfiles")


#convert csv rows to json
def make_json(csvFilePath):
    jsonFilePath=os.getcwd() + "\\nftjsonfiles"

    with open(csvFilePath, encoding='utf-8') as csvf:
      csvReader = csv.DictReader(csvf, fieldnames=("No","Name","Hash","UUID"))
      for row in csvReader:
        out=json.dumps(row, indent=4)
        n=json.loads(out)
        if n['No'] != 'No':
          jsonoutput = open(jsonFilePath+'\\'+str(n['No'])+'.json','w')
          jsonoutput.write(out)
          jsonoutput.close()
      csvf.close()


csvFilePath=input('Enter the absolute path of the csv file')
make_json(csvFilePath)


# calculate sha256 for each json file and append
def calculate_hash():
  FilePath = os.getcwd() + "\\nftjsonfiles"
  for filename in os.listdir(FilePath):
    f=os.path.join(FilePath, filename)
    if os.path.isfile(f):
      sha256_hash = hashlib.sha256()
      with open(f,'rb')as f:
        for byte_block in iter(lambda: f.read(4096),b""):
          sha256_hash.update(byte_block)
          print (sha256_hash.hexdigest())

      # append sha256 to csv line
      df = pd.read_csv(csvFilePath)
      df["sha256"] = (sha256_hash.hexdigest())
      df.to_csv(csvFilePath+ ".output.csv", index=False)
calculate_hash()










