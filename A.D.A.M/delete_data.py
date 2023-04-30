import json

def delete_data():
    # prompt user for name of entry
    FirstName = input("Enter name of entry to delete: ")
    
    # load the existing data from the file
    with open("data.txt", "r") as file:
        existing_data = json.load(file)

    # search the data for matching information
    deleted = False 
    for i in range(len(existing_data)):
        if FirstName.lower() == existing_data[i]["FirstName"].lower():
            del existing_data[i]
            deleted = True
            break

    # write the data to the file
    with open("data.txt", "w") as file:
        json.dump(existing_data, file)

    if deleted:
        print(f"Entry for '{FirstName}' has been deleted.")
    else:
        print(f"No entry found for '{FirstName}'.")