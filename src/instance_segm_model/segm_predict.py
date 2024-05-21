import os
from ultralytics import YOLO


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join('model_data', 'best_2.pt')
image_path = os.path.join('test_dataset', '943895_2517_1.jpg')

model = YOLO(model_path)

results = model.predict(source=image_path, save=True)