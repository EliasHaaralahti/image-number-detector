# Image Number Detector 

#### Image Number Detector is a web-application that uses a convolutional neural network to detect numbers drawn by the users.

## Front-end

* Implementation: Currently the project uses HTML, CSS, JavaScript and JQuery.

## Back-end

[Tensorflow](https://www.tensorflow.org/) used for deep learning. 
* The image data is preprocessed for the neural network, which was trained and tested using the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). The idea of preprocessing is to match the MNIST dataset features for better accuracy.

## To launch
* Create a new virtual environment (python3 -m venv venv).
* Activate the environment (source venv/bin/activate)
* Install all requirements (pip3 install -r requirements.txt)
* Run (python3 app.py)
* Go to localhost:5000

## Notes
* Extra contains two scripts, one to train a model using the MNIST dataset and one to evaluate the model using the MNIST testing dataset.
* The images folder will contain user images, both original and processed.
