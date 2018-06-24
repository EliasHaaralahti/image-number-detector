# Image Number Detector (In development)

#### Image Number Detector is a web-application that uses a convolutional neural network to detect numbers drawn by the users.

##### The project should be live within a month, a link will be added here.

## Front-end

* Implementation: Currently the project uses HTML, CSS, JavaScript and JQuery. Drawing is made possible by using a HTML5 Canvas and the data is sent to the back-end using an AJAX POST request.
* In the future, I will considering using a framework, such as React.

## Back-end

* Implementation: Currently the project uses Flask to handle the requests, however I'm considering switching to [Vibora](https://github.com/vibora-io/vibora), as it seems promising and it is enough for a project of this scale. The neural network uses [Tensorflow](https://www.tensorflow.org/). 
* The image data is preprocessed for the neural network, which was trained and tested using the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). The idea of preprocessing is to fit the images to match the MNIST dataset features.

## To launch
* Install all requirements (Flask, Tensorflow...)
* Run app.py
