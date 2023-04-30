from add_data import add_data
from search_data import search_data
from import_csv import import_csv
from delete_data import delete_data
from update_data import update_data
from edit_data import display_data
from analyze_data import analyze_data
from export_data import export_data
import dash_display

print("=" * 50)
print("Welcome to A.D.A.M.S \n\n      | - Atribute   \n      | - Data  \n      | - Analysis   \n      | - Management  \n      | - System            \n\nCreated By: AT")
print("=" * 50)
# main loop
while True:
        print("\nChoose from the following\n")
        print(" 1) Add data")
        print(" 2) Search data")
        print(" 3) Import CSV")
        print(" 4) Update Data")
        print(" 5) Delete Data")
        print(" 6) Analyze Data")
        print(" 7) Display Data")
        print(" 8) Export Data")
        print(" 9) DataSphere")
        print(" 10) Exit\n")
        choice = input("Enter choice (1-10): ")

        if choice == "1":
            add_data()
        elif choice == "2":
            search_data()
        elif choice == "3":
            file_name = input("Enter filename: ")
            import_csv(file_name)
        elif choice == "4":
            update_data()
        elif choice =="5":
            delete_data()
        elif choice =="6":
             analyze_data(ouptut_file = input("Enter New Filename"))
        elif choice == '7':
             #print("Placeholder")
             display_data()
        elif choice == '8':
             export_data()
        elif choice == '9':
             dash_display.app.run_server()
        elif choice == "10" or "Exit":
            print("Exiting Program.....Goodbye")
            break
        else:
            print("Invalid choice. Please another selection.")