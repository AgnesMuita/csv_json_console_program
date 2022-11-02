import csv
import json

 
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


