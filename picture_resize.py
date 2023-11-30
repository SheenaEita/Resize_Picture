from PIL import Image
import os

# Set your input and output path
input_path = ''
output_path = ''

# Set the width and height of the picture
width = 640
height = 480

# Get the file list
file_list = os.listdir(input_path)

# Counter for the file names
counter = 1

# Traverse all the files in the folder
for file_name in file_list:
    if file_name.startswith("IMG_") and file_name.endswith(".JPG"):  # Change the file extension to .jpg
        # Open the picture
        image_path = os.path.join(input_path, file_name)
        image = Image.open(image_path)

        # Resize the picture
        resized_image = image.resize((width, height))

        # Format the new file name with leading zeros
        new_file_name = f"{counter:03}.png"

        # Save the picture and close it
        new_image_path = os.path.join(output_path, new_file_name)
        resized_image.save(new_image_path)
        image.close()

        # Increment the counter
        counter += 1
print("Done.")