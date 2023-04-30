import csv
import json

def export_data():
    # load the exisitng data from the file
    with open("data.txt", "r") as file:
        existing_data = json.load(file)
    
    # Open a CSV file for writing
    with open("data.csv", "w", newline="") as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        #Write the header row
        writer.writerow(['FirstName', 'LastName', 'Email', 'Company', 'Position', 'Email', 'Connect_On'])

        # Write each data item to a new ro win the CSV file
        for item in existing_data:
            writer.writerow([item.get('FirstName', ''), item.get('LastName', ''), item.get('Email', ''), item.get('Company', ''), item.get('Position', ''), item.get('email', ''), item.get('connect_on', '')])

        print("Data exported to data.csv")