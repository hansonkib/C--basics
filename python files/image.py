# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 21:56:21 2019

@author: HANSON
"""

from PIL import Image, ImageTk, ImageDraw
root = Tk()
canvas = Canvas(width=300, height=300)
canvas.grid()
image=Image.new(mode='RGB',size=(300,300))
draw = ImageDraw.Draw(image)
draw.rectangle([(0,0),(300, 300)],fill='#000030')
L = [(randint(0,299), randint(0, 299)) for i in range(100)]
draw.point(L, fill='yellow')
photo=ImageTk.PhotoImage(image)
canvas.create_image(0,0,image=photo,anchor=NW)
mainloop()