#install package "pip install pillow"
from PIL import Image

# present image location 
path = 'python.jpeg' 

# opening the path where the image is stored
pdf = Image.open(path)

# converting the image to pdf
pdf.save('python.pdf')

# closing the image
pdf.close()

