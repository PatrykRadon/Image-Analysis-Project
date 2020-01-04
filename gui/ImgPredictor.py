import os
from PIL.ImageQt import ImageQt
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as  tf
import IPython.display as display
from PIL import Image
import os
import io
import pathlib
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
import pandas as pd
import seaborn as sns
import warnings

IMG_WIDTH, IMG_HEIGHT = (128, 128)
loaded_model = load_model('./../new_model_1')


def load_image(file_name):
    img = Image.open(file_name)
    img.load()
    img = img.resize((IMG_WIDTH, IMG_HEIGHT))
    data = np.asarray(img, dtype="int32")
    data = data.reshape(1, IMG_WIDTH, IMG_HEIGHT, 3)
    data = tf.cast(data, tf.float32)
    data /= 255

    return data


def load_file(PATH):

    image_gen = ImageDataGenerator(rescale=1. / 255)
    img = load_image(PATH)

    plt.tight_layout()
    figsize = (17, 7)
    fig, axes = plt.subplots(1, 2, figsize=figsize)

    predictions = loaded_model.predict_on_batch(img)

    axes[0].imshow(Image.open(PATH))
    classes = ['dog', 'cat', 'elephant', 'sheep', 'spider', 'sqirle', 'cow', 'chicken', 'horse', 'butterfly']

    # classes[list(predictions[0] == np.array(predictions).max()).index(True)]
    frame = pd.DataFrame(data=[list(predictions[0])], columns=classes)
    # fig.savefig("output.jpg")
    sns.barplot(x=classes, y=predictions[0], ax=axes[1])
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    return ImageQt(Image.open(buf))
