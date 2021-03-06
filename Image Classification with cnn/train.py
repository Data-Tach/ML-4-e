# Image classification
''' 
	Flow of the cnn model

1. Input
2. Convolutional LAyer
3. Pooling
4. Flattening
5. Output(0,1)
'''


from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

# Model Building
model = Sequential()
model.add(Conv2D(32,(3,3), input_shape=(64,64,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
model.summary()
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# Collecting uniform train data
train_datagen = ImageDataGenerator(rescale=1./255,
								   shear_range=0.2,
								   zoom_range=0.2,
								   horizontal_flip=True)

val_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('Dataset/train',
												  target_size=(64, 64),
												  batch_size=8,
												  class_mode='binary')
val_set = train_datagen.flow_from_directory('Dataset/val',
												  target_size=(64, 64),
												  batch_size=8,
												  class_mode='binary')

model.fit_generator(training_set,
						steps_per_epoch=10,
						epochs=150,
						validation_data=val_set,
						validation_steps=2)


model_json = model.to_json()
with open('model.json','w') as json_file:
	json_file.write(model_json)
model.save_weights('model.h5')
print('Saved model in Disk')