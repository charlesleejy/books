import os

# Specify the output file
output_file = 'big-data.md'
book_name = 'big-data'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Loop through all files in the current directory
    for filename in sorted(os.listdir('./{}'.format(book_name))):
        # Check if the file has a .md extension
        if filename.endswith('.md'):
            filepath = os.path.join('./{}'.format(book_name), filename)
            # Open and read the content of the .md file
            with open(filepath, 'r') as infile:
                content = infile.read()
                # Write the content to the output file
                outfile.write(content)
                outfile.write('\n\n')  # Add a newline between files for separation

print(f'All .md files have been combined into {output_file}')