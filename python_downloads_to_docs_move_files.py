import os
import shutil

# Set the path of the directory containing the files to be moved
source_dir = r'C:\Users\BobvanSchaik\Downloads'

# Set the path of the destination directory where the files will be moved to
destination_dir = r'C:\Users\BobvanSchaik\Documents'

# Loop through all the files in the source directory
for filename in os.listdir(source_dir):
    # Check if the file is a regular file (i.e. not a directory)
    if os.path.isfile(os.path.join(source_dir, filename)):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()
        # Define the destination directory based on the file extension
        if file_ext == '.pdf':
            dest_dir = os.path.join(destination_dir, 'PDFs')
        elif file_ext in ['.doc', '.docx']:
            dest_dir = os.path.join(destination_dir, 'Word Documents')
        elif file_ext in ['.xls', '.xlsx']:
            dest_dir = os.path.join(destination_dir, 'Excel Spreadsheets')
        else:
            dest_dir = os.path.join(destination_dir, 'Other Files')
        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        # Move the file to the destination directory
        shutil.move(os.path.join(source_dir, filename), os.path.join(dest_dir, filename))
