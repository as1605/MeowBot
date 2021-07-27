from dnn_app_utils_v3 import L_model_forward
#from PIL import Image
import numpy as np
import json
import sys

parameters = json.load(open("parameters.json"))
for p in parameters:
    parameters[p] = np.array(parameters[p])

def check_img(img, num_px=64):
    image = np.array(img.resize((num_px, num_px)))
    image = image / 255.
    image = image.reshape((1, num_px * num_px * 3)).T
    p, _ = L_model_forward(image, parameters)
    return np.squeeze(p)

#print(check_img(Image.open(sys.argv[1])))