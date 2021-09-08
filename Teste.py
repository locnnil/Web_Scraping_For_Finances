# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 16:56:33 2021

@author: linco
"""
from tkinter import *
# from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Testando Plot')
root.geometry("500x600")


def graph():
    house_prices = np.random.normal(200_00, 25_00, 5_00)
    plt.pie(house_prices)
    plt.show()



butt = Button(root, text='Start', command=graph)
butt.pack()

root.mainloop()

