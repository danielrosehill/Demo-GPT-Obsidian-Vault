import os
import subprocess

# Set up the path to the /Scripts folder relative to the repo base
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Scripts'))

# Function to run every script in the /Scripts folder
def run_all_scripts(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return
    for script in os.listdir(directory):
        script_path = os.path.join(directory, script)
        # Skip running this script itself to prevent infinite loop
        if os.path.abspath(script_path) == os.path.abspath(__file__):
            continue
        # Check if the file is a Python or Bash script
        if os.path.isfile(script_path):
            if script.endswith('.py'):
                try:
                    print(f"Running {script}...")
                    subprocess.run(['python', script_path], check=True)
                    print(f"Successfully ran {script}.")
                except subprocess.CalledProcessError as e:
                    print(f"Error while running {script}: {e}")
            elif script.endswith('.sh'):
                try:
                    print(f"Running {script}...")
                    subprocess.run(['bash', script_path], check=True)
                    print(f"Successfully ran {script}.")
                except subprocess.CalledProcessError as e:
                    print(f"Error while running {script}: {e}")

# Run all scripts in the /Scripts directory
run_all_scripts(scripts_dir)