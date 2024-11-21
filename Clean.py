import re
def clean_and_format_articles(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        lines = infile.readlines()
        formatted_lines = []
        
        for line in lines:
            # Clean up the line
            line = line.strip()
            line = re.sub(r"\s+", " ", line)  # Remove extra spaces

            if not line:  # Skip empty lines
                continue

            # Check if the line starts with a number
            match = re.match(r"^(\d+)\s+(.+)", line)
            if match:
                topic_number, content = match.groups()  # Extract number and content
            else:
                continue  # Skip lines without a number at the start

            # Format line as: <topic_number> <tab> <content>
            formatted_line = f"{topic_number}\t{content}"
            formatted_lines.append(formatted_line)

        # Write formatted lines to the output file
        outfile.write("\n".join(formatted_lines))



# File paths
input_file = "C:/Users/prabh/OneDrive/Desktop/AI project/articles.txt"  # Replace with the path to your file
output_file = "C:/Users/prabh/OneDrive/Desktop/AI project/formatted_articles.txt"

# Process the file
clean_and_format_articles(input_file, output_file)

print(f"File processed and saved to {output_file}")
