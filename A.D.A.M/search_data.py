import json
import csv
def search_data():
   # prompt user for search term
    search_term = input("Enter name or keyword to search for: ")

   # load the existing data from the file
    with open("data.txt", "r") as file:
        existing_data = json.load(file)

   # search the data for matching information
    results = []
    for item in existing_data:
        if 'FirstName' in item and search_term.lower() in item["FirstName"].lower() \
              or 'Position' in item and search_term.lower() in item["Position"].lower() \
              or 'Company' in item and search_term.lower() in item["Company"].lower():
                results.append(item)

   # display the results to the user
    print(f"Search results for '{search_term}':")
    if len(results) == 0:
       print("No results found.")
    else:
       for result in results:
           print(f"FirstName: {result.get('FirstName', 'N/A')}\nLastName: {result.get('LastName', 'N/A')}\nEmail: {result.get('Email', 'N/A')}\nPosition: {result.get('Position', 'N/A')}\nCompany: {result.get('Company', 'N/A')}\n\n\n")
