# Py-MLUtils-vision

Py-MLUtils-vision library is a Python library that provides various functionalities for image processing and annotation manipulation. It includes functions to visualize annotations, convert annotations from COCO format to YOLO format, move images matched with annotations to a different folder, and apply common image augmentations.

## Installation

You can install the library using pip:

```bash
pip install Py-MLUtils-vision
```
# Usage
## Visualize Annotations
```python
from my_image_processing_library import visualize_annotations

# Example usage
annotation_file = "path/to/annotations.json"
image_folder = "path/to/images"
class_labels = ["cat", "dog", "bird"]
visualize_annotations(annotation_file, image_folder, class_labels)
```
This function visualizes the annotations on the images and displays them in a window. It requires an annotation file in COCO format, a folder containing the corresponding images, and a list of class labels.

## Convert COCO Annotations to YOLO Format
```python
from my_image_processing_library import coco2yolo

# Example usage
annotation_file = "path/to/annotations.json"
output_folder = "path/to/output"
coco2yolo(annotation_file, output_folder)
```
This function converts annotations in COCO format to YOLO format. It reads the annotation file, extracts the bounding box coordinates and class labels, and saves the YOLO-format labels in separate files.

## Move Matched Images
```python
from my_image_processing_library import move_matched_images

# Example usage
annotation_file = "path/to/annotations.json"
image_folder = "path/to/images"
output_folder = "path/to/output"
move_matched_images(annotation_file, image_folder, output_folder)
```
This function moves only the images that have matching annotations from the given image folder to the output folder.

## Apply Image Augmentation
```python
from my_image_processing_library import apply_augmentation

# Example usage
input_folder = "path/to/input"
output_folder = "path/to/output"

# Flip images horizontally
apply_augmentation(input_folder, output_folder, flip_image)

# Resize images
new_size = (640, 480)
apply_augmentation(input_folder, output_folder, lambda img: resize_image(img, new_size))

# Rotate images
angle = 45.0
apply_augmentation(input_folder, output_folder, lambda img: rotate_image(img, angle))
```
This function applies common image augmentations to images in the input folder and saves the augmented images in the output folder. You can specify different augmentation functions such as flipping, resizing, and rotating the images.

## Contributing
Contributions to Py-MLUtils-vision library are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request.
