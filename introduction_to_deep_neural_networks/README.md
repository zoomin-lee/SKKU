### DNN_HW1
Linear Regression
- Implement training and evaluation function in ‘models/LinearRegression.py’ (‘train’ and ‘forward’ respectively) using the gradient descent method. Training should be based on minibatch. 
- Implement the linear regression with scikit-learn library in ‘/linear_sklearn.py’. The linear regression using scikit-learn library uses an analytic solution.

Logistic Regression
- Implement training and evaluation function in ‘models/ LogisticRegression.py’ (‘train’ and ‘forward’ respectively) using the gradient descent method. 
- Implement the logistic regression with scikit-learn library in ‘/linear_sklearn.py’. 


### DNN_HW2
- Implement functions in ReLU, Sigmoid, Tanh, FCLayer, SoftmaxLayer, L2Regularization in ‘Answer.py’.
(a) [Activation Layer] Implement sigmoid, ReLU, tanh activation functions in ‘Answer.py’ (‘Sigmoid’,
‘ReLU’, ‘Tanh’).
(b) [Fully Connected Layer] Implement a fully-connected layer in ‘Answer.py’ (‘FCLayer’).
(c) [Softmax Layer] Implement the softmax layer in ‘Answer.py’ (‘SoftmaxLayer’).

- [DNN with different activation layer] Report test accuracy on MNIST using three different activation functions (sigmoid, ReLU, and tanh) with a given DNN architecture and parameters. Explain the differences among three activation functions based on the result (use only one activation function in one experiment among sigmoid, ReLU, and tanh).

- [Deep Neural Networks] optimize your model architecture (# of hidden layers, # of hidden nodes, # of epochs, learning rate etc.) to achieve the best results on FashionMNIST using ‘main.py’. Report your best test accuracy with your fine-tuned hyperparameters. Show the plot of training and validation accuracy every epoch on each case. 


### DNN_HW3
- Implement Multilayer Perceptron (MLP) models in ‘MLP_classifier.py’ and ‘MLP_regressor.py.’
(a) [Regression] Implement __init__, forward, and predict method functions in ‘MLP_regressor.py.’
(b) [Classification] Implement __init__, forward, and predict method functions in ‘MLP_classifier.py.’

- [Regression with different architectures] Adjust the model settings (number of hidden layers, number of hidden nodes, number of epochs, learning rate, etc.) to obtain the best results over the House dataset using ‘main_regressionpy.’

- [Classification with different architectures] Adjust the model settings (number of hidden layers, number ofhidden nodes, number of epochs, learning rate, etc.) to get the best results over FashionMNIST using ‘main_classification.py.’

### DNN_HW4
- Implement CNN models in ‘AlexNet.py’ and ‘ResNet.py.’
(a) [AlexNet] Implement AlexNet in ‘models/AlexNet.py’.
(b) [ResNet] Implement ResNet-18 in ‘model/ResNet.py’.

- [Random Search with MNIST] Adjust the model settings (# of hidden layers, # of hidden nodes, # of epochs, learning rate, etc.) with random search to get the best results over MNIST dataset using ‘main_random_search.py’

- [CNN with Fashion MNIST] Choose a model and adjust the model settings (# of hidden layers, # of hidden nodes, # of epochs, learning rate, etc.) to get the best results over FashionMNIST dataset using ‘main_classification.py.’

### Final_Project
Semi-supervised learning for image classification: The goal of our final project is to build a machine learning model for image classification, where a few data are only labeled and most of the data are unlabeled. Therefore, it is essential to utilize a large amount of unlabeled data to improve the accuracy of your model.

Dataset: 
- Train(labeled)/Train(unlabeled)/Test data: 5,000 / 35,551 / 10,000
- Input: 32x32 image with RGB channels.
- Classes: 10 (Detailed information on labels is not provided.)


