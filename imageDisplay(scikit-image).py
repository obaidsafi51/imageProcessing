from skimage import io, transform

from main import resized_image

image = io.imread("004.jpg")

resized_image = transform.resize(image, (256, 256))

io.show(resized_image)
io.show