import os

# Set up the paths relative to the repo base
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
demo_vault_dir = os.path.join(base_dir, 'Demo-Vault')

# Function to add .gitkeep to every empty folder
def add_gitkeep_to_empty_folders(directory):
    for root, dirs, files in os.walk(directory):
        # If the folder is empty (no files and no subdirectories)
        if not dirs and not files:
            gitkeep_path = os.path.join(root, '.gitkeep')
            # Create .gitkeep file if it doesn't already exist
            if not os.path.exists(gitkeep_path):
                with open(gitkeep_path, 'w') as f:
                    pass
                print(f"Added .gitkeep to {root}")

# Run the function on the Demo-Vault directory
add_gitkeep_to_empty_folders(demo_vault_dir)