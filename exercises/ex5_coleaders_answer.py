# Import the csv library
import csv

# Open the 'llc-chapters.csv' file
chapters = open('llc-chapters.csv', mode='r')

# Convert it to a csv_data structure

chapters_data = csv.DictReader(chapters)

count = 0
# Loop through each of the rows
for chapter in chapters_data:
    # Find out who the chapter lead(s) are in the chapter
    leads = chapter["Chapter Lead(s)"]
    # Find out if there is more than one Chapter lead
    if leads.find('&') >= 0:
        # Print the city
        print(chapter['City'])
        count += 1

# Print the number of cities with co-leads!
print("There are " + str(count) + " cities with co-leads.")
# Don't forget to close your file when you're done!
chapters.close()
