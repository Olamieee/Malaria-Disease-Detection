#Malaria Detection Using MLP (Multilayer Perceptron)

#Overview

This project focuses on building a machine learning model to detect malaria from cell images using a Multilayer Perceptron (MLP) neural network. The goal is to develop an efficient and accurate deep learning model that can automatically classify whether a given cell image is infected with malaria or not. The project leverages image data preprocessing, MLP architecture for classification, and various evaluation metrics to assess the performance of the model.

The dataset used in this project consists of thousands of blood smear images labeled as either parasitized or uninfected.
	•	Number of images: 27,558 images
	•	Image size: 3-channel RGB images (130x130 pixels)
	•	Classes: Parasitized (infected), Uninfected (not infected)
 The dataset is publicly available and can be downloaded from Kaggle.
 Link to dataset: https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria 

#Results
After training, the MLP model achieves promising results in detecting malaria-infected cells. Key metrics such as accuracy, precision, recall, F1-score, ans mean squared error are reported to give a comprehensive view of the model’s performance.
	•	Accuracy: 83%
	•	Precision: 82%
	•	Recall: 83%
	•	F1-Score: 83%
 	•	MSE: 0.17
