# Batch rename all files in a given directory with today's date
from pathlib import Path
import os
import datetime

# Specify the directory containing the files
directory = "files"

# Current date and time
today = datetime.date.today()

# Loop through the files
for filename in os.listdir(directory):
    file_stem = Path(filename).stem
    # Construct new filename
    new_filename = f"{file_stem}-{today}.txt"
    # Construct full file paths
    old_file_path = os.path.join(directory, filename)
    new_file_path = os.path.join(directory, new_filename)
    # Rename the files
    os.rename(old_file_path, new_file_path)