import os
import shutil

# Define a function to get the file extension
def get_file_extension(filename):
    return os.path.splitext(filename)[1].lower()

# Specify the source directory containing your 138,000 files
source_directory = '/path/to/source_directory'

# Create a dictionary to map file extensions to destination folders
file_extension_to_folder = {
    '.txt': '/path/to/text_files_folder',
    '.jpg': '/path/to/image_files_folder',
    '.mp3': '/path/to/audio_files_folder',
    # Add more file extensions and corresponding folders as needed
}

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)

    # Check if it's a file
    if os.path.isfile(file_path):
        file_extension = get_file_extension(filename)

        # Check if the file extension is in the dictionary
        if file_extension in file_extension_to_folder:
            destination_folder = file_extension_to_folder[file_extension]

            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the file to the destination folder
            shutil.move(file_path, os.path.join(destination_folder, filename))

print("File sorting completed.")
