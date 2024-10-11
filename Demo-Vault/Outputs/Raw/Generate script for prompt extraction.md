# Prompt

Could you write me  script please It should glob over every markdown file within /Demo-Vault/Outputs and recurse into subfolders)

The files will look like this:

# Prompt

{Prompt text}

# Output 

{Output text}

Please extract {Prompt text} and copy it to a new file in 

/Prompts/Autoextracted with the same filename as the original file but _prompt added as a suffix.

Example:

The output is called dogfacts.md

Copy the prompt and save it as dogfacts_prompt.md in /Prompts/Autoextracted

# Output

 
 Thank you for the clarification! Given the paths, here’s the updated version of the script that fits exactly with the folder structure you provided:

- **Script location**: `/Scripts`
- **Source files**: `/Demo-Vault/Outputs`
- **Destination for extracted prompts**: `/Demo-Vault/Prompts/Autoextracted`

Here's the revised script:

```python
import os
import glob

# Set up the paths relative to the repo base
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
source_dir = os.path.join(base_dir, 'Demo-Vault/Outputs')
destination_dir = os.path.join(base_dir, 'Demo-Vault/Prompts/Autoextracted')

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Find all markdown files in the Outputs directory and its subdirectories
markdown_files = glob.glob(os.path.join(source_dir, '**', '*.md'), recursive=True)

# Process each markdown file
for file_path in markdown_files:
    # Read the contents of the file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract the prompt (assuming it's between "# Prompt" and "# Output")
    prompt_start = content.find("# Prompt")
    output_start = content.find("# Output")
    
    if prompt_start != -1 and output_start != -1:
        prompt_text = content[prompt_start + len("# Prompt"):output_start].strip()
        
        # Create the new filename by adding "_prompt" suffix
        base_filename = os.path.basename(file_path)
        new_filename = os.path.splitext(base_filename)[0] + "_prompt.md"
        new_file_path = os.path.join(destination_dir, new_filename)
        
        # Write the extracted prompt to the new file
        with open(new_file_path, 'w') as f_new:
            f_new.write("# Prompt\n\n" + prompt_text)

print(f"Processed {len(markdown_files)} files.")
```

### Key Changes:
1. **Relative paths**: The paths are set relative to the repo base.
   - **Source Directory**: `/Demo-Vault/Outputs`
   - **Destination Directory**: `/Demo-Vault/Prompts/Autoextracted`
   
2. **Folder Creation**: The script ensures the destination folder (`Prompts/Autoextracted`) exists, creating it if necessary.

### Instructions:
1. Place the script in the `/Scripts` folder.
2. Run the script, and it will:
   - Recursively search for all Markdown files in `/Demo-Vault/Outputs`.
   - Extract the **Prompt** section.
   - Save the extracted prompt to `/Demo-Vault/Prompts/Autoextracted`, appending `_prompt` to the filename.

Let me know if you need any further adjustments!