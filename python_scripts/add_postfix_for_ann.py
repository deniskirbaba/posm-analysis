import os
import re

def rename_files_in_folder(folder_path):
    # Define the pattern to match files ending with .jpg.json
    pattern = re.compile(r'(.+)\.jpg\.json$')
    
    # Loop over all files in the specified folder
    for filename in os.listdir(folder_path):
        # Match the pattern
        match = pattern.match(filename)
        if match:
            # Extract the base name (without .jpg.json)
            base_name = match.group(1)
            # Construct the new filename
            new_filename = f"{base_name}_1.jpg.json"
            # Get the full paths for the old and new filenames
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} -> {new_file}")

# Example usage
folder_path = 'C:/Work/Learning Lab 2024/datasets/295411_posm/dataset 2024-04-10 16_46_46/datasets/dataset 2024-04-16 12_47_22/ann'  # Change this to your folder path
rename_files_in_folder(folder_path)
