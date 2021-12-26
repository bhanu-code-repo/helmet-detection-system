# Importing required packages
from flask import Flask, request, jsonify
import os
from flask_cors import CORS, cross_origin

# Importing packages from application utils
from app_utils.utils import decodeImage
from app_utils.multi_class_obj import MultiClassObj


# Create flask application
app = Flask(__name__)
CORS(app)


# Client application class declaration
class ClientApp:
    def __init__(self):
        self.filename = 'people-with-helmet.jpg'
        modelPath = 'object_detection/model/ssd_mobilenet_v1_coco_2017_11_17'
        self.objectDetection = MultiClassObj(self.filename, modelPath)


@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clientApp.filename)
    result = clientApp.objectDetection.getPrediction()
    return jsonify(result)


# Get available "Port" number from environment
# port = int(os.getenv('PORT'))
if __name__ == '__main__':
    # Create client application class object
    clientApp = ClientApp()
    # Run flask application
    app.run(host='localhost', port=9000)