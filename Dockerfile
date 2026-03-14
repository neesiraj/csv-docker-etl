# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY ./etl /app/etl
COPY ./input /app/input
COPY ./output /app/output

# Set working directory to /app
WORKDIR /app/etl

# Command to run the ETL script
CMD ["python", "etl_mapping.py"]