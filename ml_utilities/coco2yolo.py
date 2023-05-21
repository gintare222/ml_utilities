import json
import os


def coco2yolo(json_path: str, output_path: str, image_folder: str) -> None:
    """
    Converts COCO annotations to YOLO format for images in a specified folder.

    Args:
        json_path (str): The path to the COCO annotations JSON file.
        output_path (str): The path to the directory where the YOLO-format files will be saved.
        image_folder (str): The path to the folder containing the images.
    """
    # Load the COCO annotations file
    with open(json_path, 'r') as f:
        coco = json.load(f)

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Create a dictionary to group annotations by image ID
    annotations_by_image = {}
    for annotation in coco['annotations']:
        image_id = annotation['image_id']
        if image_id not in annotations_by_image:
            annotations_by_image[image_id] = []
        annotations_by_image[image_id].append(annotation)

    # Iterate through the images and generate a YOLO-format .txt file for each image
    for image in coco['images']:
        image_filename = image['file_name']
        image_path = os.path.join(image_folder, image_filename)
        if os.path.isfile(image_path):
            image_id = image['id']
            yolo_filename = os.path.splitext(image_filename)[0] + '.txt'
            yolo_path = os.path.join(output_path, yolo_filename)
            with open(yolo_path, 'w') as yolo_file:
                if image_id in annotations_by_image:
                    for annotation in annotations_by_image[image_id]:
                        x, y, width, height = annotation['bbox']
                        x_center = x + width / 2
                        y_center = y + height / 2
                        x_center /= image['width']
                        y_center /= image['height']
                        width /= image['width']
                        height /= image['height']
                        class_id = annotation['category_id'] - 1
                        yolo_line = f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
                        yolo_file.write(yolo_line + '\n')

    print('COCO label file converted to YOLO succesfully.')