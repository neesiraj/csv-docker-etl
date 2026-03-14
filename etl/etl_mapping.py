import csv

# Input and output paths
input_file = "../input/input.csv"
output_file = "../output/output.tsv"

# Open source CSV
with open(input_file, "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Open target TSV
    with open(output_file, "w", newline="") as tsvfile:
        # Define target columns
        fieldnames = ["Name", "LastName", "Age", "DOB"]
        writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        
        # Transformation: rename columns + filter rows
        for row in reader:
            if int(row["Age"]) > 18:   # Filter
                writer.writerow({
                    "Name": row["FirstName"],
                    "LastName": row["LastName"],
                    "Age": row["Age"],
                    "DOB": row["BirthDate"]
                })

print("ETL completed. Output written to output/output.tsv")