import os

chapters = [
    "01-breaking-the-surface-a-quick-dip.md",
    "02-a-trip-to-objectville.md",
    "03-know-your-variables.md",
    "04-how-objects-behave.md",
    "05-extra-strength-methods.md",
    "06-using-the-java-library.md",
    "07-better-living-in-objectville.md",
    "08-serious-polymorphism.md",
    "09-life-and-death-of-an-object.md",
    "10-numbers-matter.md",
    "11-risky-behavior.md",
    "12-a-very-graphic-story.md",
    "13-work-on-your-swing.md",
    "14-saving-objects.md",
    "15-make-a-connection.md",
    "16-data-structures.md",
    "17-release-your-code.md",
    "18-distributed-computing.md",
    "19-the-power-of-java.md",
    "appendix-a-welcome-to-the-jvm.md",
    "appendix-b-coding-for-fun.md",
    "appendix-c-java-8-lambdas-and-streams.md",
    "appendix-d-final-mock-exam.md"
]

# Directory to create the files in
directory = "head-first-java"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create each file
for chapter in chapters:
    file_path = os.path.join(directory, chapter)
    with open(file_path, 'w') as f:
        f.write("")  # Writing a placeholder title in the file

print("Files created successfully!")