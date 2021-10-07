from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image
from numpy import loadtxt
from sklearn.metrics import confusion_matrix


json_file = open('model.json','r')
load_model_json = json_file.read()
json_file.close()
model = model_from_json(load_model_json)
model.load_weights('model.h5')
print('Loaded model from disk')


dataset = loadtxt('pima-indians-diabetes.csv',delimiter=',')
dataset = dataset[650:]
x = dataset[:,0:8]
y = dataset[:,8]


pred = model.predict_classes(x)
for i in range(len(y)):
	print('%s => %d (expected %d)' % (str(x[i]),pred[i],y[i]))


y_pred = model.predict_classes(x)

print(confusion_matrix(y,y_pred))
