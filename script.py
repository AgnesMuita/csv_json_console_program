import csv
import hashlib
import json
import os
# This is creating a csv file and writing the header to it.
create_csv = 'filename.csv'
f = open(create_csv, 'w')
writer = csv.writer(f)
# create new directory to store the generated json


def create_directory(directory):
  parent_dir = os.getcwd()
  if not os.path.exists("nftjsonfiles"):
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)


create_directory("nftjsonfiles")


def make_json():
    csvFilePath = "HNGi9 CSV FILE - Sheet1.csv"
    jsonFilePath = os.getcwd() + "\\nftjsonfiles"

    with open(csvFilePath, encoding='utf-8') as csvf:
      csvReader = csv.DictReader(csvf, fieldnames=(
          'TEAM NAMES', "Series Number", 'Filename', 'Name', 'Description', 'Gender', 'attributes', "UUID"))
      for row in csvReader:
        out = json.dumps(row, indent=4)
        n = json.loads(out)
        if n['Filename'] != 'Filename':
          jsonoutput = open(jsonFilePath+'\\'+str(n['Filename'])+'.json', 'w')
          jsonoutput.write(out)
          jsonoutput.close()
      csvf.close()


make_json()

FilePath = os.getcwd() + "\\nftjsonfiles"
for filename in os.listdir(FilePath):
    f = os.path.join(FilePath, filename)
    with open(f) as json_output:
      csvReader = json_output.read()
      for row in csvReader:
        print(row)

# Reading the csv file and skipping the first row.
with open(csvReader, encoding='utf-8') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    # next(read_csv)
    csvRead = [a for a in read_csv]
   # Creating a json file for each row in the csv file.
for row in read_csv:
    # print(row)
    currentteamname = ""
    outerkeycounter = 0
    seriestotal = len(csvReader)
    itemobject = {'format': 'CHIP-0007',
                  "sensitive_content": False, "series_total": seriestotal}
    for innerkey in csvReader:
        if innerkey == "attributes":
            itemobject["attributes"] = []
            existingattributes = innerkey['attributes'].split(";")
            for attribute in existingattributes:
                attributeproperties = attribute.split(":")
                if len(attributeproperties) == 2 and attributeproperties[0] and attributeproperties[1]:
                    newattribute = {
                        "trait_type": attributeproperties[0], "value": attributeproperties[1]}
                    itemobject['attributes'].append(newattribute)
        elif innerkey == 'TEAM NAMES':
            itemobject['minting_tool'] = currentteamname
        elif innerkey == "UUID":
            itemobject['collection'] = {"name": "Zuri NFT Tickets for Free Lunch", "id": row['UUID'], "attributes": [{
                "type": "description",
                "value": "Rewards for accomplishments during HNGi9."
            }]}
        # else:
            # pass
            # itemobject[row] = csvReader
        outerkeycounter += 1

    # Creating a json file for each row in the csv file.
    # Converting the json file to a string.
    jsonObject = json.dumps(itemobject, indent=4)
    print(jsonObject)
    with open(f'nftjsonfiles/{jsonObject.format}.json', 'w') as output:
        output.write(jsonObject)
    output.close()

    # Creating a hash of the json file and appending it to the csv file.
    hashString = hashlib.sha256(jsonObject.encode()).hexdigest()
    # Appending the file name to the csv file.
    row.append(hashString)
    writer.writerow(row)

# Closing the file.
f.close()
