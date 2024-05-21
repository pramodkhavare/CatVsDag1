import base64


def decodeImage(imgstring, fileName):
    """
    This function will help to convert base64 into image
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """
    This function will help to convert image into base64
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())