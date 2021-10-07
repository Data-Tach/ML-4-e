'''
1. Number of time pregnant
2. Plasma glucose concenteration
3. Bloop pressure (mm Hg)
4. skin Thickness (mm)
5. insulin (mu U/ml)
6. BMI
7. Diabetes predigree function
8. Age
9. Class variable (0 or 1) 
'''
# import Lib
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

dataset = loadtxt('pima-indians-diabetes.csv',delimiter=',')
x = dataset[:,0:8]
y = dataset[:,8]

# print(x[0])

# print(y[0])

# model creation
model = Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.summary()

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x,y,epochs=250,batch_size=10)

_,accuracy = model.evaluate(x,y)
print('Accuracy: %.2f'%(accuracy*100))

model_json = model.to_json()
with open('model.json','w') as json_file:
	json_file.write(model_json)
model.save_weights('model.h5')
print('Saved model to disk')

pred = model.predict_classes(x)
for i in range(5,10):
	print('%s => %d (expected %d)' % (str(x[i]),pred[i],y[i]))