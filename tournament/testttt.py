import cloudinary.uploader

# Upload a test image
result = cloudinary.uploader.upload("path/to/your/test/image.jpg")

# Print the upload result
print(result)
