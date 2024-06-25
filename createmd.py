import os

chapters = [
    "01-introduction-to-snowflake.md",
    "02-getting-started-with-snowflake.md",
    "03-architecting-snowflake-solutions.md",
    "04-loading-and-unloading-data.md",
    "05-querying-data.md",
    "06-working-with-semi-structured-data.md",
    "07-security-and-access-control.md",
    "08-data-sharing.md",
    "09-performance-optimization.md",
    "10-data-governance.md",
    "11-advanced-features.md",
    "12-integrating-with-other-tools.md",
    "13-best-practices.md",
    "14-case-studies.md",
    "15-future-directions.md",
    "16-troubleshooting-and-support.md"
]

chapters = [
    "01-what-is-software-architecture.md",
    "02-architecture-evolution.md",
    "03-decision-making.md",
    "04-services.md",
    "05-communication.md",
    "06-data-management.md",
    "07-design-for-performance-and-scalability.md",
    "08-resilience-and-reliability.md",
    "09-security.md",
    "10-managing-complexity.md",
    "11-architecture-evaluation.md",
    "12-the-role-of-the-architect.md",
    "13-microservices-and-architecture.md",
    "14-architecture-in-the-cloud.md",
    "15-conclusion.md"
]

# Directory to create the files in
directory = "software-architecture-the-hard-parts"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create each file
for chapter in chapters:
    file_path = os.path.join(directory, chapter)
    with open(file_path, 'w') as f:
        f.write("")  # Writing a placeholder title in the file

print("Files created successfully!")