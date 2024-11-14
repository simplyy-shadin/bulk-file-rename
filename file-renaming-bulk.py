import os

def rename_files_in_directory(directory, new_name_pattern=""):
    """
    Renames all files in the specified directory based on a new name pattern, keeping the original file extension.
    
    :param directory: Directory where the files are located
    :param new_name_pattern: New name pattern to use for renaming (e.g., 'file1', 'document2', etc.)
    """
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # List all files in the specified directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Iterate over each file in the directory
    for index, filename in enumerate(files, start=1):
        old_file_path = os.path.join(directory, filename)

        # Extract the file name and extension
        name, ext = os.path.splitext(filename)

        # Generate the new file name based on the new name pattern and index
        if new_name_pattern:
            # Append the index and the original extension
            new_filename = f"{new_name_pattern}{index}{ext}"
        else:
            print("Error: You must provide a new name pattern.")
            return

        # Check if the new file name already exists to avoid overwriting
        new_file_path = os.path.join(directory, new_filename)
        if os.path.exists(new_file_path):
            print(f"Warning: The file '{new_filename}' already exists. Skipping renaming.")
            continue

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    # Get user input for directory and new name pattern
    directory = input("Enter the directory path where the files are located: ")
    new_name_pattern = input("Enter a new name pattern (e.g., 'file', 'document', etc.): ")

    # Call the function to rename the files
    rename_files_in_directory(directory, new_name_pattern)
