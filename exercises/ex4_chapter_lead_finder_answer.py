# Import the csv library
import csv

# Open the 'llc-chapters.csv' file
chapters = open('llc-chapters.csv', mode='r')

# Convert it to a csv_data structure

chapters_data = csv.DictReader(chapters)

# Loop through each of the rows
for chapter in chapters_data:
    # Compare the 'City' in the row with your city
    if chapter['City'] == 'Montreal':
        # Print "Thank you [[Chapter Lead(s)]]!"
        print('Thank you, ' + chapter['Chapter Lead(s)'] + '!!!')

# Don't forget to close your file when you're done!
chapters.close()




