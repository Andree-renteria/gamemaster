import cv2
import os
import numpy as np

#Comment

def compare_images(image1, image2):

    # Convert images to HSV
    img1_hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    img2_hsv = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

    # CHistograms
    hist1 = cv2.calcHist([img1_hsv], [0, 1], None, [50, 60], [0, 180, 0, 256])
    hist2 = cv2.calcHist([img2_hsv], [0, 1], None, [50, 60], [0, 180, 0, 256])

    cv2.normalize(hist1, hist1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(hist2, hist2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    # Compare histograms (correlation method)
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity

def process_images(base_images, similarity_threshold=0.9): # Treshold adjustable for ppor quality camera pics

    # Init camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Fail to run camera.")
        return

    print("Start Process.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture pic.")
            break

        # Compare captured pic with jpgs
        for idx, base_image in enumerate(base_images):
            similarity = compare_images(base_image, frame)
            if similarity > similarity_threshold:
                print(f" Match found with Base Image {idx + 1} (Threshold: {similarity_threshold}).")
    cap.release()

def load_base_images(folder_path):

    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    base_images = []
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)
        if image is not None:
            base_images.append(image)
        else:
            print(f"Failed to load image: {image_file}")
    return base_images

# Folder path
input_folder = "Input_jpg"

# Load base images
base_images = load_base_images(input_folder)

if base_images:
    process_images(base_images, similarity_threshold=0.9)
else:
    print("No base images found for comparison.")
