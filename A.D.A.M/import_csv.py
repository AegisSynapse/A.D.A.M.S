import csv
import json
from tqdm import tqdm
import time

def import_csv(file_name):

# Open CSV File
  
    with open( file_name, "r", encoding="utf8") as file:
        # read the CSV data into a list of dictionaries
        reader = csv.DictReader(file)
        data = [row for row in reader]
        
        print(data)
# Load the existing data from the file, if any
    try:
        with open("data.txt", "r", encoding="utf8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.extend(data)
    
    with open("data.txt", "w", encoding="utf8") as file:
        json.dump(existing_data, file)

print("=" * 50)
print("\n\nSUCCESS! Data File imported.\n\nA.D.A.M. is now Loading....\n\n*ATTENTION*: Approx Load Time: 83 Seconds\n\n")
print("=" * 50)
print("\n")

bar = tqdm(range(10), colour="#00ffff", desc="Progress")
for i in bar:
  time.sleep(2)


