from PIL import Image, ImageOps
import os

input_folder = "input"
output_folder = "output"

max_width = 1920
max_height = 1080

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(input_folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, file)

        img = Image.open(img_path)
        img = ImageOps.exif_transpose(img)  # fix phone rotation

        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)  # high quality

        save_path = os.path.join(output_folder, file)
        img.save(save_path, quality=95, optimize=True)

        print("Resized:", file)
