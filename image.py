# import required module
import os
from PIL import Image
# assign directory
directory = 'images'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    
    # checking if it is a file
    if os.path.isfile(f):
        
        #open

        im = Image.open(f)
        

        #rotate

        im = im.rotate(90)

        #resize

        im = im.resize((128,128))

        #convert

        f, e = os.path.splitext(f)

        im = im.save("icons" , "JPEG")
        
