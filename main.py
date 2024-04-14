from PIL import Image

# Load the image
image_path = r'C:\Users\mirsu\Downloads\MyArt.jpg'
original_image = Image.open(image_path)

# Convert the image to RGBA if it is not already in that mode
image = original_image.convert("RGBA")

# Generate a new image with a transparent background
datas = image.getdata()

new_image_data = []
for item in datas:
    # Change all white (also shades of whites)
    # pixels to transparent
    if item[0] > 160 and item[1] > 150 and item[2] > 150:
        new_image_data.append((255, 255, 255, 0))
    else:
        new_image_data.append(item)

# Update image data
image.putdata(new_image_data)

# Save the new image with a transparent background
transparent_image_path = r'C:\Users\mirsu\Downloads\MyArtNOBACk.jpg'
image.save(transparent_image_path, "PNG")

transparent_image_path