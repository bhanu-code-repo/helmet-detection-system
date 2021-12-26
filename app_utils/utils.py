# Importing required packages
import base64


# Function to decode image string
def decodeImage(imgString, fileName):
    imgdata = base64.b64decode(imgString)
    with open("object_detection/images/"+fileName, 'wb') as f:
        f.write(imgdata)
        f.close()