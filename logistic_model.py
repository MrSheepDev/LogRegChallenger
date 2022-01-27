#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Stelios Zappala
# Last modified : 26/10/2021

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression as lr
from sklearn.metrics import classification_report, confusion_matrix

class Logistic_Model :

    def __init__(self, array_x, array_y):
        # Pour simplifier certaines fonctions, création du modèle non entraîné
        self.base_model = lr(solver='liblinear', random_state=0)
        # Création d'un modèle entraîné
        self.model = self.base_model.fit(array_x, array_y)

        # Enregistrement des données utilisées dans l'objet
        self.base_data_x = array_x
        self.base_data_y = array_y

    def visual_confusion_matrix(self):
        cm = confusion_matrix(self.base_data_y, self.model.predict(self.base_data_x))

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(cm)
        ax.grid(False)
        ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
        ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
        ax.set_ylim(1.5, -0.5)
        for i in range(2):
            for j in range(2):
                ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
        plt.show()

    def print_confusion_matrix(self):
        pass

    def print_coefs(self):
        b0 = self.model.intercept_
        b1 = self.model.coef_
        print("Coefficient b0:", b0, "\nCoefficient b1:",b1)

    def print_y_range(self):
        y_range = self.model.classes_
        print("Distinct values of y:", y_range)

    def print_predictions(self, x_array):
        predicted_y = self.model.predict(x_array)
        print("Here is the predicted y array:\n", predicted_y)

    def print_probability_matrix(self, x_array):
        probability_matrix = self.model.predict_proba(x_array)
        print("Here is the prediction matrix:\n", probability_matrix)

    def print_fiability(self):
        fiability = self.model.score(self.base_data_x, self.base_data_y)
        print("The fiability percentage for this model is", round((fiability*100), 2),"%")

    def print_classification_report(self):
        matrix = classification_report(self.base_data_y, self.model.predict(self.base_data_x),zero_division=1)
        print(matrix)
