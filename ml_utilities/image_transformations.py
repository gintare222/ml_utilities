import cv2
import os
import numpy as np
from typing import Callable

def apply_augmentation(input_folder: str, output_folder: str, augmentation_fn: Callable) -> None:
    """
    Apply the specified image augmentation function to images in the input folder and save the augmented images
    in the output folder.

    Args:
        input_folder (str): Path to the input folder containing images.
        output_folder (str): Path to the output folder where augmented images will be saved.
        augmentation_fn (Callable): Image augmentation function to apply.
    """
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image file using OpenCV
            img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_COLOR)

            # Apply the specified augmentation function
            augmented_img = augmentation_fn(img)

            # Save the augmented image in the output folder
            output_path = os.path.join(output_folder, f"n{filename}")
            cv2.imwrite(output_path, augmented_img)


def flip_image(img: np.ndarray) -> np.ndarray:
    """
    Flip the input image horizontally.

    Args:
        img (np.ndarray): Input image.

    Returns:
        np.ndarray: Flipped image.
    """
    return cv2.flip(img, 1)


def resize_image(img: np.ndarray, new_size: tuple) -> np.ndarray:
    """
    Resize the input image to the specified new size.

    Args:
        img (np.ndarray): Input image.
        new_size (tuple): Tuple representing the new size of the image (width, height).

    Returns:
        np.ndarray: Resized image.
    """
    return cv2.resize(img, new_size)


def rotate_image(img: np.ndarray, angle: float) -> np.ndarray:
    """
    Rotate the input image by the specified angle.

    Args:
        img (np.ndarray): Input image.
        angle (float): Angle of rotation in degrees.

    Returns:
        np.ndarray: Rotated image.
    """
    image_center = tuple(np.array(img.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    return cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)

