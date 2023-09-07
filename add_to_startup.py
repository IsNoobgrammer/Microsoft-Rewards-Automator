import os
import platform
import shutil

def add_to_startup(path):
    # Detect the current operating system
    system = platform.system()

    if system == 'Windows':
        # Get the Windows startup folder
        startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        script_path = os.path.abspath(path)
        script_name = os.path.basename(script_path)
        destination = os.path.join(startup_folder, script_name)

        try:
            # Copy the script to the startup folder
            if script_path != destination:
                shutil.copy2(script_path, destination)
            print(f"Added to startup on {system}.")
        except Exception as e:
            print(f"Error adding to startup on {system}: {e}")

# Specify the script directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Create a batch file (edge_rewards.bat) that runs your Python script
batch_file_path = os.path.join(script_directory, "edge_rewards.bat")
with open(batch_file_path, "w") as batch_file:
    batch_file.write(f'python "{os.path.join(script_directory, "main.py")}"')

# Add the batch file to startup
add_to_startup(batch_file_path)
