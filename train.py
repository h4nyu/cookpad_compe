# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:50:58 2017

@author: n.aoi
"""

import os
import pandas as pd
import numpy as np
import pickle
from PIL import Image
from sklearn.neural_network import MLPClassifier
# from package.models import MyModel # you may import your own model in the package
# from package import preprocess_methods # you may import your own preprocess method in the package

PATH_TO_TRAIN_IMAGES = os.path.join('data', 'processed', 'train_images')
PATH_TO_TRAIN_DATA = os.path.join('data', 'given', 'train_master.tsv')
PATH_TO_MODEL = os.path.join('models', 'mlp')

def load_train_data(path_to_train_images, path_to_train_data):
    print('loading train data ...')
    data = pd.read_csv(path_to_train_data, sep='\t')
    X = []
    y = []
    for row in data.iterrows():
        f, l = row[1]['file_name'], row[1]['label_id']
        try:
            im = Image.open(os.path.join(path_to_train_images, f))

            # you may write preprocess method here given an image
            # im = preprocess_methods.my_preprocess_method(im)

            X.append(np.array(im).flatten())
            y.append(l)
        except Exception as e:
            print(str(e))

    X = np.array(X)
    y = np.array(y)
    print('done.')
    return X, y

def train_model(X, y):
    print('training the model ...')
    model = MLPClassifier() # or you can instanciate your own model(MYModel)
    model.fit(X, y)
    print('done.')
    return model

def save_model(model, name):
    print('saving the model ...')
    with open(name+'.pkl', mode='wb') as f:
        pickle.dump(model, f)
    print('done.')

if __name__ == '__main__':
    ## load the data for training
    X, y = load_train_data(PATH_TO_TRAIN_IMAGES, PATH_TO_TRAIN_DATA)
    
    ## instanciate and train the model
    model = train_model(X, y)

    ## save the trained model
    save_model(model, PATH_TO_MODEL)