#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Stelios Zappala
# Last modified : 26/10/2021

from interface import *

if __name__ == '__main__' :
    main = Menu()
    main.start_menu()

    main.main_menu()
    while main.state != "quit" :
        main.main_menu()
