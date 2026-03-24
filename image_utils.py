import cv2
import numpy as np

def process_image(file):
    bytes_data = np.asarray(bytearray(file.read()), dtype=np.uint8)
    img = cv2.imdecode(bytes_data, 1)
    img = cv2.resize(img, (128,128))
    return img
