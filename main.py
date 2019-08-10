# Вариант портфеля - 7
# Вариант диаграммы - 2

from tkinter import *
from threading import Thread
import time

import random


class Column(Canvas):
    colors = list("0123456789abcdef")
    scale = 5
    speed = 0.05
    def __init__(self, root, color, text):
        Canvas.__init__(self, root)
        self.color = list(color)
        self.fontColor = list("#f0f0f0")
        self.shadow = self.create_rectangle(0, 0, 0, 0, outline="#999", fill="#999")
        self.rect = self.create_rectangle(0, 0, 0, 0, outline=color, fill=color)
        self.lbl = Label(self, text=text, fg="#f0f0f0", justify=LEFT, font='Arial 8')
        self.percentsVariable = StringVar()
        self.percentsVariable.set("0.0%")
        self.perLbl = Label(self, textvariable=self.percentsVariable, fg="#f0f0f0", justify=LEFT, font='Arial 8')
        self.name = self.create_window(0, 0, window=self.lbl, anchor='w')
        self.percents = self.create_window(0, 0, window=self.perLbl, anchor='w')

    def huePlus(self):
        i = 6
        while (i > 0):
            while (self.color[i] != self.colors[-1]):
                ind = self.colors.index(self.color[i])
                self.color[i] = self.colors[ind + 1]
                tempColor = "".join(self.color)
                self.itemconfigure(1, fill=tempColor, outline=tempColor)
                time.sleep(self.speed)
            i -= 1

    def selfColorTo(self):
        i = 1
        while (self.fontColor != self.color):
            if (self.fontColor[i] < self.color[i]):
                ind = self.colors.index(self.fontColor[i])
                self.fontColor[i] = self.colors[ind + 1]
            if (self.fontColor[i] > self.color[i]):
                ind = self.colors.index(self.fontColor[i])
                self.fontColor[i] = self.colors[ind - 1]
            tempColor = "".join(self.fontColor)
            self.lbl.config(fg=tempColor)
            self.perLbl.config(fg=tempColor)
            time.sleep(self.speed)
            i += 1
            if (i > 6): i = 1

    def hueMinus(self):
        i = 6
        while (i > 0):
            while (self.fontColor[i] != self.colors[0]):
                ind = self.colors.index(self.fontColor[i])
                self.fontColor[i] = self.colors[ind - 1]
                tempColor = "".join(self.fontColor)
                self.lbl.config(fg=tempColor)
                time.sleep(self.speed)
            i -= 1

    def fromDarkness(self):
        darkness = list("#000000")
        i = 6
        while (i > 0):
            while (darkness[i] != self.color[i]):
                ind = self.colors.index(darkness[i])
                darkness[i] = self.colors[ind + 1]
                tempColor = "".join(darkness)
                self.itemconfigure(self.rect, fill=tempColor, outline=tempColor)
                time.sleep(self.speed)
            i -= 1

    def grow(self):
        h = 0
        while (h < self.he):
            shadowHeight = h - 5
            if (shadowHeight < 0): shadowHeight = 0
            self.coords(self.shadow, 10, 270 - shadowHeight, self.wi + 10, 270)
            self.coords(self.rect, 0, 270 - h, self.wi, 270)
            self.coords(self.name, 0, 255 - h)
            self.coords(self.percents, self.lbl.winfo_width(), 255 - h)
            time.sleep(self.speed)
            h += 1
            self.percentsVariable.set(str(h/self.scale) + "%")

    def animateHeight(self, width, height):
        self.wi = width
        self.he = height * self.scale
        thread = Thread(target=self.grow)
        thread.start()

    def animateColor(self):
        thread = Thread(target=self.fromDarkness)
        thread.start()

    def animateFont(self):
        self.toColor = self.color
        thread = Thread(target=self.selfColorTo)
        thread.start()


class Package(Tk):
    wi = 100
    he = 400
    startXPosition = 20
    startYPosition = 150
    offset = 2 * startXPosition

    def __init__(self, name, input):
        Tk.__init__(self)
        self.title(name)
        self.geometry(str((self.wi + self.offset) * len(input)) + "x" + str(self.he + 40))
        self.elements = input

    def show(self):
        print("Showing..")

        i = 0
        for text in self.elements:
            col = Column(self, self.getRandomColorHex(), text)
            col.place(x=self.startXPosition + i * (self.wi + self.offset), y=self.startYPosition)
            col.animateHeight(self.wi, self.elements.get(text))
            col.animateColor()
            col.animateFont()
            i += 1
        self.mainloop()

    def getRandomColorHex(self):
        symbols = "01259abc"
        return "#" + symbols[random.randrange(0, len(symbols))] + symbols[random.randrange(0, len(symbols))] + symbols[
            random.randrange(0, len(symbols))] + symbols[random.randrange(0, len(symbols))] + symbols[
                   random.randrange(0, len(symbols))] + symbols[random.randrange(0, len(symbols))]


input = {"Ростелеком": 20, "Мегафон": 15, "МТС": 35, "АФК Система": 10, "Башкирэнерго": 20}

package = Package("Пакеты акций", input)
package.show()
