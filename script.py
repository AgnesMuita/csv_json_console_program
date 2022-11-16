import csv
import hashlib
import json
import os
import pandas as pd



# create new directory to store the generated json
def create_directory():
  parent_dir = os.getcwd()
  list = ('nftjsonfiles', 'newjsonfiles')
  for item in list:
    if not os.path.exists(item):
        path = os.path.join(parent_dir, item)
        os.mkdir(path)
create_directory()




def make_json():
    csvFilePath = "HNGi9 CSV FILE - Sheet1.csv"
    jsonFilePath = os.getcwd() + "\\nftjsonfiles"


    with open(csvFilePath, encoding='utf-8') as csvf:
      csvReader = csv.DictReader(csvf, fieldnames=(
          'TEAM NAMES', "Series Number", 'Filename', 'Name', 'Description', 'Gender', 'attributes', "UUID"))
      for row in csvReader:
        #load python object to json string using dumps
        out = json.dumps(row, indent=4)
        #load json string to python object using loads
        n = json.loads(out)
        if n['Filename'] != 'Filename':
          jsonoutput = open(jsonFilePath+'\\'+str(n['Filename'])+'.json', 'w')
          jsonoutput.write(out)
          jsonoutput.close()
      csvf.close()
make_json()

def generate_CHIP_json():
    FilePath = os.getcwd() + "\\nftjsonfiles"
    for filename in os.listdir(FilePath):
        f = os.path.join(FilePath, filename)
    with open(f) as json_output:
        data = json.load(json_output)
    # with open('newcsv.csv','w') as file:
    #     json.dump(data, file)
        currentteamname = ""
        outerkeycounter = 0
        seriestotal = len(data)
        itemobject = {'format': 'CHIP-0007',"sensitive_content": False, "series_total": seriestotal}
        for innerkey in data.keys():
            if innerkey == "attributes":
                itemobject["attributes"] = []
                existingattributes = data[innerkey].split(";")
                for attribute in existingattributes:
                    attributeproperties = attribute.split(":")
                    if len(attributeproperties) == 2 and attributeproperties[0] and attributeproperties[1]:
                        newattribute = {"trait_type": attributeproperties[0], "value": attributeproperties[1]}
                        itemobject['attributes'].append(newattribute)
            elif innerkey == 'TEAM NAMES':
                itemobject['minting_tool'] = currentteamname
            elif innerkey == "UUID":
                itemobject['collection'] = {"name": "Zuri NFT Tickets for Free Lunch", "id": data[innerkey], "attributes": [{
                    "type": "description",
                    "value": "Rewards for accomplishments during HNGi9."
                }]
            }
            else:
                itemobject[innerkey]=data[innerkey]
        outerkeycounter += 1

        # Creating a json file with the CHIP-0007 JSON and create a hash for it
        jsonObject = json.dumps(itemobject, indent=4)
        newJsonFilePath = os.getcwd() + "\\newjsonfiles"
        FilePathNew = os.getcwd() + "\\nftjsonfiles"

        with open(newJsonFilePath+'\\'+filename+'.json', 'w') as newjsonoutput:
            newjsonoutput.write(jsonObject)

        for filenames in os.listdir(FilePathNew):
            f = os.path.join(FilePath, filenames)
        with open(f) as newchipjson:
            bytes = newchipjson.read()
            readable_hash=hashlib.sha256(bytes.encode('utf-8')).hexdigest()  

            # create new csv file
            with open("newcsv.csv",'w') as csvfile:
                writer=csv.writer(csvfile)
                writer.writerows(newchipjson)


generate_CHIP_json()

# Closing the file.
