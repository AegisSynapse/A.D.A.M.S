import json
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(ouptut_file=None):
    #Load the exisitng data from the file
    with open("data.txt", "r") as file:
        existing_data = json.load(file)

    # Create Pandas dataframe from the data
    df = pd.DataFrame(existing_data, columns=['FirstName', 'LastName', 'Email', 'Position', 'Company'])

    # Calculate the number of entries for each occupation 
    Company_counts = df['Company'].value_counts()

    # Calculate the number of entires for each state
    Position_counts = df['Position'].value_counts()

    # Calculate the number of entries for each city
    FirstName_counts = df['FirstName'].value_counts()

    # Plot the results
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,4))
    ax1.barh(Company_counts.index, Company_counts.values)
    ax1.set_xlabel('Number of Entries')
    ax1.set_ylabel('Company')
    ax1.set_title('Entries by Company')
    ax2.barh(Position_counts.index, Position_counts.values)
    ax2.set_xlabel('Number of Entries')
    ax2.set_ylabel('Position')
    ax2.set_title('Entries by position')
    ax3.barh(FirstName_counts.index, FirstName_counts.values)
    ax3.set_xlabel('Number of Entries')
    ax3.set_ylabel('FirstName')
    ax3.set_title('Entries by FirstName')
    plt.tight_layout()

    if ouptut_file is not None:
        plt.savefig(ouptut_file)
    else:
        plt.show