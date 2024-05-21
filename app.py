from flask import Flask ,request , jsonify, render_template
import os ,sys 
from flask_cors import CORS, cross_origin 
from src.CatVSDog.pipeline.prediction import DogCat
from src.CatVSDog.utils import decodeImage ,encodeImageIntoBase64
TF_ENABLE_ONEDNN_OPTS=0
app = Flask(__name__)
CORS(app) 

class ClientApp():
    print(123)
    def __init__(self):
        self.filename = 'inputImage.jpg'
        self.model = DogCat(self.filename)

@app.route('/' ,methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.model.prediction()
    return jsonify(result)




if __name__=="__main__":
    clApp = ClientApp()
    app.run(debug=True,port=8501)


#Author :Pramod