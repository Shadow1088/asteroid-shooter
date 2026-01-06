from os import listdir
from variables import *
from pygame import image

def loadImages(path):
    for image_name in listdir(path):
        IMAGES[str(image_name[:-4])] = image.load("../media/images/" + image_name).convert_alpha()

def checkOutOfBounds():
    pass
