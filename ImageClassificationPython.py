# Steps for image classification on CIFAR-10:

"""Load the dataset from keras datasets module"""

from keras.datasets import cifar10
import matplotlib.pyplot as plt
 
(train_X,train_Y),(test_X,test_Y)=cifar10.load_data()

"""Plot some images from the dataset to visualize the dataset"""

n=6
plt.figure(figsize=(20,10))
for i in range(n):
plt.subplot(300+1+i)
plt.imshow(train_X[i])
plt.show()

"""Import the required layers and modules to create our convolution neural 
net architecture"""

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils

"""Convert the pixel values of the dataset to float type and then 
normalize the dataset"""

train_x=train_X.astype('float32')
test_X=test_X.astype('float32')
 
train_X=train_X/255.0
test_X=test_X/255.0

"""Now perform the one-hot encoding for target classes"""

train_Y=np_utils.to_categorical(train_Y)
test_Y=np_utils.to_categorical(test_Y)
 
num_classes=test_Y.shape[1]

"""Create the sequential model and add the layers"""

model=Sequential()
model.add(Conv2D(32,(3,3),input_shape=(32,32,3),
    padding='same',activation='relu',
    kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Conv2D(32,(3,3),activation='relu',padding='same',kernel_constraint=maxnorm(3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(512,activation='relu',kernel_constraint=maxnorm(3)))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

"""Configure the optimizer and compile the model"""

sgd=SGD(lr=0.01,momentum=0.9,decay=(0.01/25),nesterov=Fals)
 
model.compile(loss='categorical_crossentropy',
  optimizer=sgd,
  metrics=['accuracy'])

"""View the model summary for better understanding of model
 architecture"""

model.summary()


"""Train the model"""

model.fit(train_X,train_Y,
    validation_data=(test_X,test_Y),
    epochs=10,batch_size=32)


"""Calculate its accuracy on testing data"""

_,acc=model.evaluate(test_X,test_Y)
print(acc*100)


"""Save the model"""

model.save("model1_cifar_10epoch.h5")


"""Make a dictionary to map to the output classes and make 
predictions from the model"""

results={
   0:'aeroplane',
   1:'automobile',
   2:'bird',
   3:'cat',
   4:'deer',
   5:'dog',
   6:'frog',
   7:'horse',
   8:'ship',
   9:'truck'
}
from PIL import Image
import numpy as np
im=Image.open("__image_path__")
# the input image is required to be in the shape of dataset, i.e (32,32,3)
 
im=im.resize((32,32))
im=np.expand_dims(im,axis=0)
im=np.array(im)
pred=model.predict_classes([im])[0]
print(pred,results[pred])

















