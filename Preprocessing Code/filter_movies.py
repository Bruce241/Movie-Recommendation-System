import csv

# Get movie IDs from movies.csv
movies_csv_ids = set()
movies_data = []

with open('movies.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row and row[0].strip():
            movie_id = row[0].strip()
            movies_csv_ids.add(movie_id)
            movies_data.append(row)

# Get movie IDs from filtered-genome-tags.csv
filtered_genome_tags_ids = set()
with open('filtered-genome-scores.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row and row[0].strip():
            filtered_genome_tags_ids.add(row[0].strip())

# Find missing movie IDs
missing_movie_ids = sorted(movies_csv_ids - filtered_genome_tags_ids)

# Remove movies with missing IDs from movies_data
filtered_movies_data = [row for row in movies_data if row[0].strip() not in missing_movie_ids]

# Write the filtered data to a new CSV file
with open('filtered-movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(filtered_movies_data)

print("Filtered movies.csv created without movies with missing IDs.")
