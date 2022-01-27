#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logistic_model import Logistic_Model
from prompts import Prompts
import numpy as np

class Menu :

    # Un peu de triche, le modèle n'a pas assez de casse pour créer quelque chose de simple avec une donnée
    CHALLENGER_X = np.array([[53],[54],[55],[56],[57],[58],[59],[60],[61],[62],[63],[66],[67],[68],[69],[70],[72],[73],[75],[76],[76],[78],[79],[81]])
    CHALLENGER_Y = np.array([  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0])

    def __init__(self):
        self.state = "first start"

    def start_menu(self):
        Prompts.array_load_print()
        array_load_choice = input("Enter the number of your choice : ")
        while array_load_choice not in "1230" and len(array_load_choice) != 1 :
            print("Sorry, but your choice seems invalid. Please try again.")
            Prompts.array_load_print()
            array_load_choice = input("Enter the number of your choice : ")

        if array_load_choice == "0" :
            self.state = "stopped"
            exit()

        elif array_load_choice == "1" :
            x = self.get_default_x()
            y = self.get_default_y()
            self.lr_model = Logistic_Model(x, y)

        elif array_load_choice == "2" :
            print("Work in progress ! (WIP)")

        elif array_load_choice == "3" :
            x = np.arange(10).reshape(-1, 1)
            y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
            self.lr_model = Logistic_Model(x, y)

        else :
            print("Something went wrong.")


    @classmethod
    def get_default_x(cls) :
        return cls.CHALLENGER_X

    @classmethod
    def get_default_y(cls) :
        return cls.CHALLENGER_Y

    def main_menu(self):
        self.state = "main"
        Prompts.main_menu_prompt()
        main_choice = input("Enter your choice: ")
        while main_choice not in "1234560" and len(main_choice) != 1 :
            Prompts.invalid_choice()
            main_choice = input("Enter your choice: ")

        if main_choice == "0" :
            self.state = "quit"

        elif main_choice == "1" :
            self.lr_model.visual_confusion_matrix()

        elif main_choice == "2" :
            self.lr_model.print_confusion_matrix()

        elif main_choice == "3" :
            self.lr_model.print_coefs()

        elif main_choice == "4" :
            number = int(input("Enter the temperature to predict: "))
            self.lr_model.print_predictions(np.array([[number]]))

        elif main_choice == "5" :
            Prompts.wip()

        elif main_choice == "6" :
            self.lr_model.print_fiability()

        elif main_choice == "7" :
            self.lr_model.print_classification_report()

        else :
            print("Unrecognized choice")
            self.state = "quit"



