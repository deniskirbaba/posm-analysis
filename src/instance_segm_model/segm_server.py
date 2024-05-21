import os
from flask import Flask, request, jsonify
from ultralytics import YOLO


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model_data', 'best.pt')
model = YOLO(model_path)

# Define a route to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input image path from the request
    image_path = request.json['image_path']
    
    # Check if the image exists
    if not os.path.isfile(image_path):
        return jsonify({'error': 'Image file does not exist'}), 400

    # Perform segmentation
    results = model.predict(source=image_path)

    # Return the prediction results
    if not results[0]:
        return "[]"
    return results[0].tojson()

# Run the Flask application
if __name__ == '__main__':
    print("Starting the segmentation model server...")
    app.run(port=5000, debug=True)
