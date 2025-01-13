import os

# Specify the directory
directory = r"F:\OBS Recordings"

# Check if the directory exists
if not os.path.exists(directory):
    print(f"The directory {directory} does not exist.")
else:
    # Iterate through all files in the directory
    for file in os.listdir(directory):
        # Check if the file ends with .mkv
        if file.endswith(".mkv"):
            file_path = os.path.join(directory, file)
            try:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    print("Operation completed.")
