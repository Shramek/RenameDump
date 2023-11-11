import os
from datetime import datetime
from tqdm import tqdm

def get_creation_date(file_path):
    # Get the creation time of the file
    stat_info = os.stat(file_path)
    return datetime.utcfromtimestamp(stat_info.st_ctime)

def rename_images(folder_path, start_number=0):
    # Get the list of PNG image files in the folder and sort them by creation date
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
    image_files.sort(key=lambda x: get_creation_date(os.path.join(folder_path, x)))

    # Calculate the number of digits needed for padding
    num_digits = len(str(len(image_files) + start_number - 1))

    # Format string for renaming
    format_string = "{:0" + str(num_digits) + "d}.png"

    # Rename each image file with a progress bar
    for i, old_name in tqdm(enumerate(image_files), desc="Renaming", unit="image"):
        new_name = format_string.format(i + start_number)
        os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))

    print("Renaming complete.")

# Example usage: Specify the folder path and starting number
folder_path = r'C:\PATH TO \RENAME DUMP'
start_number = 0
rename_images(folder_path, start_number)
