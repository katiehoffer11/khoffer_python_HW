#Open the file, cereal.csv and start by skipping the header row. See hints below for this.
#Read through the remaining rows and find the cereals that contain five grams of fiber or more
#printing the data from those rows to the terminal.


import os
import csv

cereal_csv = os.path.join("Resources", "cereal.csv")

# Open the CSV
with open(cereal_csv) as file:
    csvreader = csv.reader(file, delimiter=",")
    #skip first row
    next(csvreader, None)
    
    # Loop through looking fiber count
    for row in csvreader:
        fiber = float(row[7])
        cereal = row[0]
        
        if fiber >= 5.00:
            
            print(cereal)