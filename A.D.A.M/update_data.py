import json

def update_data():
    # prompt user for name to update
    FirstName = input("Enter name of the record you want to update:  ")

    # load the existing data from the file
    with open("data.txt", "r") as file:
        existing_data = json.load(file)

    # find the record with the matching name
    found = False
    for item in existing_data:
        if 'FirstName' in item and FirstName.lower() == item['FristName'].lower():
            found = True
            # Prompt user for New Data
            new_lastname = input("Enter new age (press Enter to keep existing age):  ")
            new_email = input("Enter new occupation (press Enter to keep existing occupation):  ")
            new_position = input("Enter new city (press Enter to keep existing city):  ")
            new_company = input("Enter new state (press Enter to keep existing state):  ")
            # update the record with the new data
            if new_lastname:
                item['LastName'] = new_lastname
            if new_email:
                item['Email'] = new_email
            if new_position:
                item['Position'] = new_position
            if new_company:
                item['Company'] = new_company


# write the updated dat back to the file
    with open("data.txt", "w") as file:
        json.dump(existing_data, file)

    if found:
        print(f"Record for {FirstName} succesfully udpated")
    else:
        print(f"No record found for {FirstName}")
