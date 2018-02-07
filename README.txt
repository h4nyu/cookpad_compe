This is the sample code which you can work on in this competition.

Descriptions of folders and files:
・data
    - given: Data given in this competition go here. By default, "mnist data"[1] are given.
・models: Trained model(s) saved go here.
・package: Your original package which can be imported go here.
・preprocess.py: A script for preprocessing the given data(e.g. extract zipfiles or tarfiles, etc.)
・train.py: A script for instanciating, training, and saving your model.
・predict.py: A script for making predictions for test data and save them as a submit file.

Environment:
・python 3.5.2
・OS: Windows7
・libraries
    - scikit-learn 0.18
    - pandas 0.19.2
    - numpy 1.12.1
    - PIL 3.4.2

Process of execution all together:
0. Move to /path/to/sample_code/ in your command line.
1. Excecute 'python preprocess.py'. Preprocessed data are created under /data/processed/.
    - Make sure paths(e.g. PATH_TO_GIVEN_DATA) are set right.
2. Excecute 'python train.py'. Trained model for train data given is saved under /models/.
    - Make sure paths(e.g. PATH_TO_TRAIN_IMAGES) are set right.
3. Excecute 'python predict.py'. Predictions are made with the saved model and are saved as a submit file(submit.csv).
    - Make sure paths(e.g. PATH_TO_TRAINED_MODEL) are set right.

Process of reproducing the submit file:
0. Move to /path/to/sample_code/ in your command line. The trained model is assumed to be given.
1. Put the trained model under /path/to/sample_code/models/
2. Excecute 'python predict.py'. Submit file should be reproduced(submit.csv).
    - Make sure paths(e.g. PATH_TO_TRAINED_MODEL) are set right.

Notes:
・When you submit your code, make sure your submitted file is ready to be reproduced like above.
・Don't forget to submit your trained model along with your code.
・Though these sample codes are written in Python, you don't need to write yours in Python(R, Java, Lua, etc. are OK.).
・If the environment you are working on is a bit hard to create, please explain how to create it if possible.

External Link:
[1] http://yann.lecun.com/exdb/mnist/