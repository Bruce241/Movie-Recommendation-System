import csv

# Get movie IDs from movies.csv
movie_ids = set()
with open('movies.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row:
            movie_ids.add(row[0])

# Filter genome-tags.csv based on movie IDs
filtered_rows = []
with open('genome-scores.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row and row[0] in movie_ids:
            filtered_rows.append(row)

# Write the filtered data to a new CSV file or overwrite genome-tags.csv
with open('filtered-genome-scores.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(filtered_rows)

print("Filtered genome-tags.csv created with matching movie IDs.")
