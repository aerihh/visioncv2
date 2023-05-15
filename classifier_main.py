#image classifier model, the model uses scikit libraries 
#to train and test an image classifier program
#the images we are going to use are crops
#taken from the tec's parking lot.

import os 
import numpy as np
import pickle

from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#data and categories

path = "C:/Users/Irving/Documents/Vision/Parking_img"

categories = ['empty', 'not_empty']
label = []
data = []

for category_id, category in enumerate(categories):
    for file in os.listdir(os.path.join(path, category)):
        image_path = os.path.join(path, category, file)
        image = imread(image_path)
        image = resize(image, (15, 15))
        data.append(image.flatten())
        label.append(category_id)

data = np.asarray(data)
label = np.asarray(label)

print(data)
#model training

x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2, shuffle=True ,stratify=label)

#print(x_train, y_train)

classifier = SVC()

parameters = [{'gamma':[0.01, 0.001, 0.0001], 'C':[1, 10, 100, 1000]}]

grid_search = GridSearchCV(classifier, parameters)

grid_search.fit(x_train, y_train)

#testing model

best_model = grid_search.best_estimator_

y_pred = best_model.predict(x_test)

score = accuracy_score(y_pred, y_test)

print('{}% of samples were correctly classified'.format(str(score*100)))

pickle.dump(best_model, open('./model.p', 'wb'))
