MNIST Classification Project

This project demonstrates various machine learning models and techniques applied to the MNIST dataset. It includes data preprocessing, binary classification, multi-class classification, multi-label classification, and noise removal using scikit-learn.

Features

Data Loading and Visualization:
  Fetch and visualize the MNIST dataset.
  Display individual digit images and their pixel values.
Binary Classification:
  Train a Stochastic Gradient Descent (SGD) classifier to detect the digit "5".
  Evaluate model performance using precision, recall, F1 score, and ROC curves.
Multi-Class Classification:
  Use SVM, SGD, and Random Forest models to classify digits from 0 to 9.
  Visualize confusion matrices and analyze classification errors.
Multi-Label Classification:
  Train a K-Nearest Neighbors (KNN) model for multi-label classification (e.g., identifying if a digit is odd or greater than or equal to 7).
Noise Removal:
  Add random noise to MNIST images.
  Train a KNN model to clean noisy images and recover the original digits.
