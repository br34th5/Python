import requests
from io import BytesIO
from PIL import Image


r = requests.get("https://wallpaperplay.com/walls/full/8/0/c/132643.jpg")
print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image" + image.format

try:
    image.save(path, image.format)
except IOError:
    print("IOError, cannot save image.")