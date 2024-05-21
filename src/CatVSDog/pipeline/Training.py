from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense




model = Sequential()

model.add(Conv2D(32 ,(3,3) ,input_shape=(64,64,3) ,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(units=128 ,activation='relu'))
model.add(Dense(units=1 ,activation='sigmoid')) 

model.compile(optimizer='adam' ,loss='binary_crossentropy' ,metrics=['accuracy']) 


from tensorflow.keras.preprocessing.image  import ImageDataGenerator 

train_datagen = ImageDataGenerator(
    rescale =1./255 ,
    shear_range =0.2 ,
    zoom_range = 0.2 ,
    horizontal_flip = True
)

test_datagen = ImageDataGenerator(rescale =1./255 ) 

training_set = train_datagen.flow_from_directory(
    'D:\\Data Science\\ComputerVision\\DogVSCat\\cats_and_dogs_filtered\\train' ,
    target_size = (64,64) ,
    batch_size = 32 ,
    class_mode = 'binary' ,
    color_mode = 'rgb'
)
test_set = test_datagen.flow_from_directory(
    'D:\\Data Science\\ComputerVision\\DogVSCat\\cats_and_dogs_filtered\\validation' ,
    target_size = (64,64) ,
    batch_size = 32 ,
    class_mode = 'binary' ,
    color_mode = 'rgb'
)

final_model = model.fit(training_set ,
                        steps_per_epoch = 8000,
                         epochs = 5,
                         validation_data = test_set,    
                         validation_steps = 2000) 

print(final_model)
model.save("model.h5")
print("Saved model to disk")


# D:\Data Science\ComputerVision\DogVSCat\src\CatVSDog\pipeline\Training.py