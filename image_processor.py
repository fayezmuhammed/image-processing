import cv2
import numpy as np

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load the image.")
        return
    
    # Print size and shape of the image
    height, width, channels = image.shape
    print(f"Image Size: {width}x{height}")
    print(f"Image Shape: {image.shape}")
    
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Convert image to binary
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    
    # Scale the image by reducing its size using a different interpolation method for better scaling effect
    scaled_image = cv2.resize(image, (width // 3, height // 2), interpolation=cv2.INTER_AREA)
    
    # Remove noise using Gaussian Blur
    denoised_image = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Save images
    cv2.imwrite("grayscale.jpg", gray_image)
    cv2.imwrite("binary.jpg", binary_image)
    cv2.imwrite("scaled.jpg", scaled_image)
    cv2.imwrite("denoised.jpg", denoised_image)

    print("Processed images have been saved successfully.")

# Example usage
image_path = "sample.jpg"  # Replace with your image path
process_image(image_path)