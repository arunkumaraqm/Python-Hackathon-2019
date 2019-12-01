## B4) Resize some huge size photos and add some text to all the images.

## Due to time trouble, this was only done for one photo and there was an error using ImageFont.truetype. 

## Please include "SomePicture.jpg" in the pwd.

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

basewidth = 300
img = Image.open('SomePicture.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img2 = img.resize((basewidth,hsize), Image.ANTIALIAS)


ImageDraw.Draw(
    img  # Image
).text(
    (0, 0),  # Coordinates
    'Hello world!',  # Text
    (0, 0, 0),  # Color
)

img2.save('SomePictureResized.jpg') 


font = ImageFont.truetype("Arial", size = 36) 

ImageDraw.Draw(
    img  # Image
).text(
    (0, 0),  # Coordinates
    'Hello world!',  # Text
    (0, 0, 0),  # Color
	font = font
)
img.save('SomePictureWithText.jpg')

