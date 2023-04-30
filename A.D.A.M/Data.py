import json

print("Welcome to DMS")
# function to add new data to the file
def add_data():
   # prompt user for information
   name = input("Enter name: ")
   age = input("Enter age: ")
   occupation = input("Enter occupation: ")
   location1 = input("Enter City: ")
   location2 = input("Enter State: ")
   Email = input("Enter Email: ")
   PhoneNumber = input("Enter Phonenumber: ")
   Notes = input("Enter Notes: ")
   # create a dictionary with the user's information
   data = {"name": name, "age": age, "occupation": occupation, "location1": location1, "location2": location2, "Email": Email, "PhoneNumber": PhoneNumber, "Notes": Notes}

   # load the existing data from the file, if any
   try:
       with open("data.txt", "r") as file:
           existing_data = json.load(file)
   except FileNotFoundError:
       existing_data = []

   # add the new data to the existing data
   existing_data.append(data)

   # write the updated data to the file
   with open("data.txt", "w") as file:
       json.dump(existing_data, file)

   print("Data added successfully.")

# function to search for specific information within the stored data
def search_data():
   # prompt user for search term
   search_term = input("Enter name or keyword to search for: ")

   # load the existing data from the file
   with open("data.txt", "r") as file:
       existing_data = json.load(file)

   # search the data for matching information
   results = []
   for item in existing_data:
       if search_term.lower() in item["name"].lower() or search_term.lower() in item["occupation"].lower() or search_term.lower() in item["location"].lower():
           results.append(item)

   # display the results to the user
   print(f"Search results for '{search_term}':")
   if len(results) == 0:
       print("No results found.")
   else:
       for result in results:
        print(f"Name: {result['name']}\nAge: {result['age']}\nOccupation: {result['occupation']}\nLocation1: {result['location1']}\nLocation2: {result['location2']}\nNotes: {result['Notes']}\nEmail: {result['Email']}\nPhoneNumber: {result['PhoneNumber']}")

def delete_data():
    # prompt user for name of entry
    name = input("Enter name of entry to delete: ")
    
    # load the existing data from the file
    with open("data.txt", "r") as file:
        existing_data = json.load(file)

    # search the data for matching information
    deleted = False 
    for i in range(len(existing_data)):
        if name.lower() == existing_data[i]["name"].lower():
            del existing_data[i]
            deleted = True
            break

    # write the data to the file
    with open("data.txt", "w") as file:
        json.dump(existing_data, file)

    if deleted:
        print(f"Entry for '{name}' has been deleted.")
    else:
        print(f"No entry found for '{name}'.")

def edit_data():
    # prompt user for name of entry to edit
    name = input("Enter name of entry to edit: ")

    #load the existing data from the file
    with open("data.txt", "r") as file:
        exisiting_data = json.load(file)

    #find the entry to edit
    for item in exisiting_data:
        if name.lower() == item["name"].lower():
            #prompt user for updated information
            age = input(f"Enter new age for {item['name']}: ")
            occupation = input(f"Enter occupation for {item['name']}: ")
            location1 = input(f"Enter new City for {item['name']}: ")
            location2 = input(f"Enter new State for {item['name']}: ")
            Email = input(f"Enter new Email for {item['name']}: ")
            PhoneNumber = input(f"Enter new PhoneNumber for {item['name']}: ")
            notes = input(f"Enter new notes for {item['name']}: ")

            #update the entry
            item["age"] = age
            item["occupation"] = occupation
            item["location1"] = location1
            item["location2"] = location2
            item["Email"] = Email
            item["PhoneNumber"] = PhoneNumber
            item["notes"] = notes

            # write the udpated data to the file
            with open("data.txt", "w") as file:
                json.dump(exisiting_data, file)

            print("Data Updated Succesfully")
            return
    print(f"No entry found for {name}.")

# main loop
while True:
   print("\nPlease choose from the following Options")
   print("1. Add New Entry")
   print("2. Search Entries")
   print("3. Delete Entries")
   print("4. Edit Entries")
   print("5. Exit")
   choice = input("Enter choice (1-5): ")

   if choice == "1":
       add_data()
   elif choice == "2":
       search_data()
   elif choice == "3":
       delete_data()
   elif choice == "4":
       edit_data() 
   elif choice == "5": 
       break
   else:
       print("Invalid choice. Please try again.")