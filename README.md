# hashing_script
The hashing script is a simple CLI tool for generating sha256 hashes for nfts. 

## General Information
The program intends to make it simple to prepare nfts for minting by quickly generating unique hashes for them. 
The program has been created as a fulfillment for HNG's bidding task for backend devs. 

## Technologies Used
Python 3

## Setup
Clone the project to get started: 

git clone https://github.com/AgnesMuita/hashing_script.git

To set up the project, 

Open the project on the root directory and install the required modules by running:


pip install -r requirements.txt

python scripts.py


This will prompt you to add the name of the CSV file. In this case, add "HNGi9 CSV FILE - Sheet1.csv".

A folder "nftjsonfiles" will be created where the json files for all the rows will be stored, 

and an output csv with the hashes appended will be generated. 

