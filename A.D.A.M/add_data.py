import json

#Need to Add First Name, Last Name, Email_Address, Company, Position, Connected on

def add_data():
   # prompt user for information
   FirstName = input("Enter First name: ")
   LastName = input("Enter Last name:  ")
   Email = input("Enter Email: ")
   Company = input("Enter Company: ")
   Position = input("Enter position: ")
   Connected_On = input("Enter Connected On: ")
   # create a dictionary with the user's information
   data = {"FirstName": FirstName, "LastName": LastName, "Email": Email,  "Position": Position, "Company": Company, "Connected_On": Connected_On}

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
