import cv2
import os

def extract_patches(input_folder, output_folder, patch_size):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.JPG','.jpg', '.jpeg')):  # Add more image extensions if needed
            image_path = os.path.join(input_folder, filename)
            img = cv2.imread(image_path)

            # Determine the number of patches in each dimension
            num_patches_rows = img.shape[0] // patch_size
            num_patches_cols = img.shape[1] // patch_size

            # Extract non-overlapping patches
            for i in range(num_patches_rows):
                for j in range(num_patches_cols):
                    patch = img[i * patch_size:(i + 1) * patch_size, j * patch_size:(j + 1) * patch_size]

                    # Save each patch
                    patch_filename = f"{os.path.splitext(filename)[0]}_{i}_{j}.png"
                    patch_path = os.path.join(output_folder, patch_filename)
                    cv2.imwrite(patch_path, patch)

input_folder = "/home/sruthi/PycharmProjects/saliency_mmseg/video/images_4k/"
output_folder = "/home/sruthi/PycharmProjects/saliency_mmseg/video/patches_4k/"
patch_size = 256

extract_patches(input_folder, output_folder, patch_size)
