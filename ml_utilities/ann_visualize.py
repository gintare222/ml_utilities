import os
import cv2
from typing import List

def visualize_YOLO_labels(dataset_path: str, labels_path: str, classes: List[str]) -> None:
    """
    Visualizes YOLO labels on images and saves the images with bounding boxes.

    Args:
        dataset_path (str): Path to the folder containing the images.
        labels_path (str): Path to the directory where the YOLO labels are located.
        classes (List[str]): List of class labels.
    """
    OUTPUT_FOLDER = 'bbox_output'
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for image_file in os.listdir(dataset_path):
        if image_file.endswith('.jpg'):
            # Load the image
            image_path = os.path.join(dataset_path, image_file)
            image = cv2.imread(image_path)

            # Load the corresponding label file
            label_file = os.path.splitext(image_file)[0] + '.txt'
            label_path = os.path.join(labels_path, label_file)
            with open(label_path, 'r') as f:
                label_lines = f.readlines()

            # Loop over each line of the label file and draw a bounding box on the image
            for line in label_lines:
                class_id, x_center, y_center, width, height = map(float, line.split())
                x_min = int((x_center - width / 2) * image.shape[1])
                y_min = int((y_center - height / 2) * image.shape[0])
                x_max = int((x_center + width / 2) * image.shape[1])
                y_max = int((y_center + height / 2) * image.shape[0])
                cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

                # Add a text label to the bounding box
                class_label = classes[int(class_id)]
                label = "{}".format(class_label)
                cv2.putText(image, label, (x_min, y_min), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

            # Save the image with the bounding boxes
            output_path = os.path.join(OUTPUT_FOLDER, image_file)
            cv2.imwrite(output_path, image)

    print("Bounding boxes visualization completed. Images with bounding boxes saved in 'bbox_output' folder.")
