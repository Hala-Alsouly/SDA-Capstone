# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 05:44:11 2022

@author: hello
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

df = pd.read_csv('Enumerated dataset.csv')
df.head()

# Finding the best features to use for the traning
df.corrwith(df['Victim of cybercrime']).sort_values( ascending=False)

# Finding the best features to use for the traning and store it
corrArray=df.corrwith(df['Victim of cybercrime']).sort_values( ascending=False)
# pick the best 10 columns. 5 from the top and 5 from the last
top5=corrArray[1:6]
top5= list(top5.index)
top10= list(corrArray[1:11].index)
top15= list(corrArray[1:16].index)
top3= list(corrArray[1:4].index)
toplist= [top3, top5, top10, top15]

buttom5=corrArray[-5:]
buttom5= list(buttom5.index)
buttom10= list(corrArray[-10:].index)
buttom15= list(corrArray[-15:].index)
buttom20= list(corrArray[-20:].index)
buttom3= list(corrArray[-3:].index)
buttomlist= [buttom3, buttom5, buttom10, buttom15]

#Scores lists
logistic_regression= []
Decision_Tree= []
Random_forest= []
svc=[]
#Cross values lists
logCrossVal= []
DecisionTree_CrossVal= []
RandomForest_crossVal= []
svc_crossVal=[]


for i in range (0, len(toplist)):
    predictors = df[toplist[i] + buttomlist[i]] # training , X
    target = df['Victim of cybercrime'] # prediction , Y


    x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size = 0.20, random_state = 0)

    # Building model
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)
        # getting the prediction
    y_pred=logreg.predict(x_test)
    t=logreg.score(x_train, y_train)
    print("Training Accuracy:", t)
    test= metrics.accuracy_score(y_test, y_pred)
    print("Testing Accuracy:", test)
    # precision tp / (tp + fp)
    precision = metrics.precision_score(y_test, y_pred)
    print('Precision: %f' % precision)
    # recall: tp / (tp + fn)
    recall = metrics.recall_score(y_test, y_pred)
    print('Recall: %f' % recall)
    logistic_regression.append({'training':t,
                                'testing': test,
                                'precision':precision,
                                'recall': recall  })
    scores = cross_val_score(logreg, x_train, y_train, cv=5)
    logCrossVal.append(scores)
    
    ######## Decision Tree
    
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=3).fit(x_train, y_train)
    # Predicting the y values corresponding to X_test_sm
    clf_pred = clf.predict(x_test)
    t=clf.score(x_train, y_train)
    print("Training Accuracy:", t)
    test= metrics.accuracy_score(y_test, clf_pred)
    print("Testing Accuracy:", test)
    # precision tp / (tp + fp)
    precision = metrics.precision_score(y_test, clf_pred)
    print('Precision: %f' % precision)
    # recall: tp / (tp + fn)
    recall = metrics.recall_score(y_test, clf_pred)
    print('Recall: %f' % recall)
    Decision_Tree.append({'training':t,
                                'testing': test,
                                'precision':precision,
                                'recall': recall  })
    scores = cross_val_score(clf, x_train, y_train, cv=5)
    DecisionTree_CrossVal.append(scores)
    print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))
    
    #######Random Forest
    class_forest = RandomForestClassifier(n_estimators = 5, criterion = 'entropy', random_state = 0).fit(x_train, y_train)
    preds_class = class_forest.predict(x_test)
    t= class_forest.score(x_train, y_train)
    print("Training Accuracy:", t)
    test=metrics.accuracy_score(y_test, preds_class)
    print("Testing Accuracy:", test)
    # precision tp / (tp + fp)
    precision = metrics.precision_score(y_test, preds_class)
    print('Precision: %f' % precision)
    # recall: tp / (tp + fn)
    recall = metrics.recall_score(y_test, preds_class)
    print('Recall: %f' % recall)
    Random_forest.append({'training':t,
                                'testing': test,
                                'precision':precision,
                                'recall': recall  })
    scores = cross_val_score(class_forest, x_train, y_train, cv=5)
    RandomForest_crossVal.append(scores)
    print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))
    
    
    ##################SVC
    class_sv = SVC(kernel = 'linear', random_state = 0)
    class_sv.fit(x_train, y_train)
    preds_class = class_sv.predict(x_test)
    
    t=class_sv.score(x_train, y_train)
    print("Training Accuracy:", t)
    test=metrics.accuracy_score(y_test, preds_class)
    print("Testing Accuracy:", test)
    # precision tp / (tp + fp)
    precision = metrics.precision_score(y_test, preds_class)
    print('Precision: %f' % precision)
    # recall: tp / (tp + fn)
    recall = metrics.recall_score(y_test, preds_class)
    print('Recall: %f' % recall)
    
    svc.append({'training':t,
                                'testing': test,
                                'precision':precision,
                                'recall': recall  })
    scores = cross_val_score(class_sv, x_train, y_train, cv=5)
    svc_crossVal.append(scores)
    print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))
    
print(logistic_regression)
print(Decision_Tree)
print(Random_forest)
print(svc)

print('----Logistic Regression----')
print(pd.DataFrame(logistic_regression))
print('----Decision Tree Classifair----')
print(pd.DataFrame(Decision_Tree))
print('----Random forest----')
print(pd.DataFrame(Random_forest))
print('----Support Vector Classifair----')
print(pd.DataFrame(svc))