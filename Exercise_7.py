import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
data=load_iris()
data.data.shape
print('classes to predict:',data.target_names)
print('features:',data.feature_names)
x = data.data
y = data.target
display(x.shape,y.shape)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=50,test_size=0.25)
classifier = DecisionTreeClassifier()
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)
from sklearn.metrics import accuracy_score
print('Accuracy on train data using Gini: ',accuracy_score(y_true = y_train,y_pred = classifier.predict(x_train)))
print('Accuracy on test data using Gini: ',accuracy_score(y_true = y_test,y_pred = y_pred))
