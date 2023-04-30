import json

def display_data():
    #load the existing data from the file
    with open("data.txt", "r") as file:
        exisiting_data = json.load(file)

    print("Existing data:")
    if(exisiting_data) == 0:
        print("No data found")
    else:
        for item in exisiting_data:
                print(f"\nFirstName: {item.get('FirstName', 'N/A')}\nLastName: {item.get('LastName', 'N/A')}\nEmail: {item.get('Email', 'N/A')}\nPosition: {item.get('Position', 'N/A')}\nCompany: {item.get('Company', 'N/A')}\n\n")
                