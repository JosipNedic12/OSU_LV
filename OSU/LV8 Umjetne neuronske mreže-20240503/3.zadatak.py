import numpy as np
from tensorflow import keras
from keras import layers
from matplotlib import pyplot as plt
from PIL import Image
from keras.api.models import load_model

model = load_model('LV8 Umjetne neuronske mreže-20240503\model.keras')

def do_prediction(path):
    image = Image.open(path).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image)

    image_array = image_array.astype("float32") / 255
    image_array = np.expand_dims(image_array, axis=0)
    image_array = np.expand_dims(image_array, axis=-1)

    predicted_label = np.argmax(model.predict(image_array))
    return predicted_label

accurate = []

for i in range(10):
    print("===================================")
    print(f"Testing on number {i}")
    prediction = do_prediction(f"LV8 Umjetne neuronske mreže-20240503\\{i}.png")
    print(f"Predicted: {prediction}")
    print(f"Good prediction: {prediction == i}")
    if prediction == i:
        accurate.append(prediction)
    print("===================================")
    print()

print("===================================")
print(f"Accurate predictions: {len(accurate)} / 10")
print(f"Accuracy: {len(accurate) / 10}")
print("===================================")