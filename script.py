import csv
import hashlib
import json
import os

create_csv = 'HNGi9 CSV FILE - Sheet1.output.csv'
f = open(create_csv, 'w')
writer = csv.writer(f)

#create new directory to store the generated json
def create_directory(directory):
  parent_dir = os.getcwd()
  if not os.path.exists("nftjsonfiles"):
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
create_directory("nftjsonfiles")

#convert csv to json
def csv_to_json():
  with open('HNGi9 CSV FILE - Sheet1.csv', 'r') as csvf:
      read_csv = csv.reader(csvf, delimiter=',')
      next(read_csv)
      csvReader = [a for a in read_csv]
    # create a json file for each row in the csv file.
      for row in csvReader:
        if row[1] and row[2]:
            series_number = row[0]
            file_name = row[1]
            name = row[2]
            description = row[3]
            gender = row[4]
            attributes = row[5]
            uuid = row[6]

            json_file = {
                'format': 'CHIP-0007',
                'name': file_name.replace('-', ' ').title(),
                'description': description,
                'minting_tool': '',
                'series_number': series_number,
                'sensitive_content': False,
                'series_total': csvReader[-1][0],
                "attributes": [
                    {
                        "trait_type": "gender",
                        "value": gender
                    }
                ],
                "collection": {
                    "name": "Zuri NFT tickets for free lunch",
                    "id": uuid,
                    "attributes": [
                        {
                            "type": "description",
                            "value": "Rewards for accomplishments during HNGi9"
                        }
                    ]
                },
            }

            # Convert the json file to a string.
            jsonoutput = json.dumps(json_file, indent=4)
            with open(f'nftjsonfiles/{name}.json', 'w') as output:
                output.write(jsonoutput)
            output.close()

          # Create a hash of the json file and append it to the csv file.
            hashString = hashlib.sha256(jsonoutput.encode()).hexdigest()
            row.append(hashString)
            writer.writerow(row)

  # Closing the file.
  f.close()

csv_to_json()
