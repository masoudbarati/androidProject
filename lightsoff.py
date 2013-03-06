import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import ObjectProperty

# a simple solution for the data. not the brightest one. anyone who wants
# something else should do it himself.
 
mapdata = [
    [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
    ],
    [
    [1,1,0,1,1],
    [1,0,0,0,1],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [1,1,0,1,1]
    ],
    [
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0]
    ],
    [
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0]
    ]
    ]

class MyPaintWidget(Widget):
    
    rects = [] #this holds the state of 25 different areas
    started = False #determines whether the game is started or not

    def update_screen(self):
        with self.canvas:
            for i in range(5):
                for j in range(5):
                    if (self.rects[j][i] == 1): #on
                        Color(1, 0, 0)
                    else: #off
                        Color(1, 0, 1)
                    #it will draw new rectangles over the older ones.
                    #TODO: only draw the changed rectangles
                    Rectangle(pos=[self.pos[0] + 2 + 
                    (i * self.size[0] / 5.0), self.pos[1] + 2 + (j * self.size[1] / 5.0)]
                    , size=[self.size[0] / 5.0 - 4, self.size[1] / 5.0 - 4])


    def check_button(self, touch):
        pass

    def load_level(self, level):
        for i in range(5):
            self.rects.append(mapdata[level][i])
        with self.canvas:
            for i in range(5):
                for j in range(5):
                    if (mapdata[level][j][i] == 1):
                        Color(1, 0, 0)
                    else:
                        Color(1, 0, 1)
                    Rectangle(pos=[self.pos[0] + 2 + 
                    (i * self.size[0] / 5.0), self.pos[1] + 2 + (j * self.size[1] / 5.0)]
                    , size=[self.size[0] / 5.0 - 4, self.size[1] / 5.0 - 4])

    def start(self):
        #upon start, load the first level
        self.load_level(0)
                
    def on_touch_down(self, touch):
        #TODO: a splash screen should replace the black one. should be done in mypaint.kv
	if (not self.started):
	    self.start()
	    self.started = True
	else: #only check buttons if we have really started the game.
            self.check_button(touch)
            self.update_screen()
        
class MyPaintApp(App):
    def build(self):
        return MyPaintWidget() #start the game

if __name__ == '__main__':
    MyPaintApp().run()
