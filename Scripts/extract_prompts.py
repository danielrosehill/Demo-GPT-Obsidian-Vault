import os
import glob
import re

# Set up the paths relative to the repo base
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
source_dir = os.path.join(base_dir, 'Demo-Vault/Outputs')
destination_dir = os.path.join(base_dir, 'Demo-Vault/Prompts/Autoextracted')

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Find all markdown files in the Outputs directory and its subdirectories
markdown_files = glob.glob(os.path.join(source_dir, '**', '*.md'), recursive=True)

# Verify that all markdown files are found correctly
if not markdown_files:
    print("No markdown files found.")
else:
    print(f"Found {len(markdown_files)} markdown files.")

# Process each markdown file
for file_path in markdown_files:
    try:
        # Create the new filename by adding "_prompt" suffix
        base_filename = os.path.basename(file_path)
        new_filename = os.path.splitext(base_filename)[0] + "_prompt.md"
        new_file_path = os.path.join(destination_dir, new_filename)
        
        # Skip processing if the file already exists (to avoid overwriting)
        if os.path.exists(new_file_path):
            print(f"File {new_file_path} already exists, skipping.")
            continue
        
        # Read the contents of the file
        with open(file_path, 'r') as f:
            content = f.read()

        # Extract the prompt by using regex to match possible headers
        # Match headers like "# Prompt", "## Prompt", "### **Prompt**", or "**Prompt**"
        prompt_match = re.search(r'(?i)^(?:#+\s*\**Prompt\**|^Prompt\s*\**)', content, re.MULTILINE)
        output_match = re.search(r'(?i)^(?:#+\s*\**Output\**|^Output\s*\**)', content, re.MULTILINE)

        if prompt_match and output_match:
            # Extract text between the matched "Prompt" and "Output" headers
            prompt_text = content[prompt_match.end():output_match.start()].strip()

            # Write the extracted prompt to the new file
            with open(new_file_path, 'w') as f_new:
                f_new.write("# Prompt\n\n" + prompt_text)
            print(f"Processed and saved prompt to {new_file_path}.")
        else:
            print(f"Could not find valid prompt and output sections in {file_path}.")
    
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

print(f"Total files processed: {len(markdown_files)}.")
