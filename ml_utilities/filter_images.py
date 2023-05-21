import os
import json
from shutil import copyfile

def move_matched_images(json_path: str, images_path: str, matched_images_path: str) -> None:
    """
    Moves images from the input image folder to the output matched images folder based on the JSON labels file.

    Args:
        json_path (str): Path to the JSON labels file.
        images_path (str): Path to the folder containing images.
        matched_images_path (str): Path to the folder where matched images will be saved.
    """
    # Load the JSON file
    with open(json_path) as f:
        data = json.load(f)

    # Iterate over each line in the JSON file
    for line in data['images']:
        # Get the image filename from the line in the JSON file
        image_filename = line['file_name']

        # Create the output directory if it doesn't exist
        os.makedirs(matched_images_path, exist_ok=True)

        # Construct the full path to the matched image file
        matched_image_path = os.path.join(matched_images_path, image_filename)

        # Look for the image in subfolders of the images path
        for root, dirs, files in os.walk(images_path):
            if image_filename in files:
                image_path = os.path.join(root, image_filename)
                # Copy the image file to the matched image folder
                copyfile(image_path, matched_image_path)
                print(f"Copied {image_filename} to {matched_images_path}")
                break
        else:
            print(f"Error: {image_filename} not found.")

