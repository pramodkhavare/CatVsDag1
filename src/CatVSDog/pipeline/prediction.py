import numpy as np 
from keras.models import load_model 
from keras.preprocessing import image 


class DogCat:
    def __init__(self ,filename):
        self.filename = filename 

    def prediction(self):
        model = load_model('D:\\Data Science\\ComputerVision\\DogVSCat\\model.h5') 

        imagename = self.filename 

        test_image = image.load_img(imagename ,target_size=(64,64)) 
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image , axis=0) 

        result = model.predict(test_image)

        if result[0][0] == 1:
            prediction = 'dog'
            return [{ "Category" : prediction}]
        else:
            prediction = 'cat'
            return [{ "Category" : prediction}]
        # if result[0][0] == 1:
        #     prediction = 'dog'
        #     return [prediction]
        # else:
        #     prediction = 'cat'
        #     return [prediction]