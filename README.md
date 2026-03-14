# CSV to TSV ETL Pipeline (Python + Docker)

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline that converts a CSV file into a tab-delimited TSV file using Python and Docker.

The project simulates common ETL concepts used in tools like Informatica such as:

* Source → Transform → Target
* Column mapping
* Data filtering

## Technologies Used

* Python 3
* Docker
* Git
* CSV file processing

## Project Structure

```
csv_etl_project/
│
├── etl/
│   └── etl_mapping.py      # Python ETL script
│
├── input/
│   └── input.csv           # Source data
│
├── output/
│   └── output.tsv          # Generated output
│
├── Dockerfile              # Docker container configuration
├── .gitignore
└── README.md
```

## ETL Workflow

1. Read source CSV file
2. Apply transformations:

   * Rename columns
   * Filter rows (Age > 18)
3. Write results to a tab-delimited TSV file

## Sample Input

```
FirstName,LastName,Age,BirthDate
John,Doe,25,1998-02-15
Alice,Smith,17,2006-07-21
Bob,Johnson,32,1991-11-05
Eve,Adams,20,2003-05-12
```

## Sample Output

```
Name	LastName	Age	DOB
John	Doe	25	1998-02-15
Bob	Johnson	32	1991-11-05
Eve	Adams	20	2003-05-12
```

## Build Docker Image

```
docker build -t csv_etl_project .
```

## Run ETL Pipeline

```
docker run -v E:/csv_etl_project/output:/app/output csv_etl_project
```

## Key Learning Outcomes

* Containerizing ETL pipelines with Docker
* Processing CSV data using Python
* Managing projects using Git
* Understanding ETL mapping concepts similar to Informatica

## Author

Neeraj