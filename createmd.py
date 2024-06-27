import os

chapters = [
    "01-introduction-to-data-engineering.md",
    "02-data-management-architectures-for-analytics.md",
    "03-the-aws-data-engineer's-toolkit.md",
    "04-data-cataloging-security-and-governance.md",
    "05-architecting-data-engineering-pipelines.md",
    "06-populating-data-marts-and-data-warehouses.md",
    "07-ingesting-streaming-data.md",
    "08-transforming-data-with-aws-glue-studio.md",
    "09-triggering-lambda-functions-with-s3-events.md",
    "10-running-complex-sql-queries-on-data-lake-data.md",
    "11-visualizing-data-with-amazon-quicksight.md",
    "12-extracting-sentiment-data-with-amazon-comprehend.md",
    "13-building-transactional-data-lakes.md",
    "14-implementing-a-data-mesh-approach.md"
]

# Directory to create the files in
directory = "data-engineering-on-aws"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create each file
for chapter in chapters:
    file_path = os.path.join(directory, chapter)
    with open(file_path, 'w') as f:
        f.write("")  # Writing a placeholder title in the file

print("Files created successfully!")