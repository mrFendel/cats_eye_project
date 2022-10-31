from PIL import Image
import numpy as np
import pandas as pd
from math import atan

left_eye = Image.open("left_eye.png")
right_eye = Image.open("right_eye.png")


def process_photo(photo_data_path, left_coordinates, right_coordinates):

    image = Image.open(photo_data_path)
    size_of_left_eye = (left_coordinates["xmax"] - left_coordinates["xmin"], left_coordinates["ymax"] - left_coordinates["ymin"])
    size_of_right_eye = (right_coordinates["xmax"] - right_coordinates["xmin"], right_coordinates["ymax"] - right_coordinates["ymin"])

    MULT = 2

    x_place_left = left_coordinates["xmin"] - int((1/2) * (MULT - 1) * (left_coordinates["xmax"] - left_coordinates["xmin"]))
    y_place_left = left_coordinates["ymin"] - int((1/2) * (MULT - 1) * (left_coordinates["ymax"] - left_coordinates["ymin"]))

    x_place_right = right_coordinates["xmin"] - int((1/2) * (MULT - 1) * (right_coordinates["xmax"] - right_coordinates["xmin"]))
    y_place_right = right_coordinates["ymin"] - int((1/2) * (MULT - 1) * (right_coordinates["ymax"] - right_coordinates["ymin"]))


    size_of_right_eye = tuple([int(element * MULT) for element in size_of_right_eye])
    size_of_left_eye = tuple([int(element * MULT) for element in size_of_left_eye])

    angle = atan((right_coordinates["x0"] - left_coordinates["x0"]) / (right_coordinates["y0"] - left_coordinates["y0"]))
    _left_eye = left_eye.copy().resize(size_of_left_eye)
    _right_eye = right_eye.copy().resize(size_of_right_eye)
    _right_eye = _right_eye.rotate(int(angle), Image.NEAREST, expand=1)
    image.paste(_right_eye, (x_place_right, y_place_right), _right_eye)
    image.paste(_left_eye, (x_place_left, y_place_left), _left_eye)

    image.save("BruhCat.jpeg")

df = pd.read_csv('coord.csv', sep='  ')
df = df.drop('name', axis=1)
left_df = df[df.x0 == min(df.x0)]

right_df = df[df.x0 == max(df.x0)]



process_photo("catImage.jpg", left_df.squeeze().astype(int), right_df.squeeze().astype(int))
