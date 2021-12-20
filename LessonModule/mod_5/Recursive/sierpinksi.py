"""
Example program shows the use of recursion to create fractals, 
in this case, the Sierpinski Triangle. See function:

draw_triangles

for the recursion. The rest is TkInter program allowing the
user to change properties of the Sierpinski triangle drawn.

"""


from tkinter import *
import math

class MyApp(object):
    def __init__(self, parent):
        ##Function local to __init__ to simplify repetitive button creation process
        def put_button(parent, name, functionname, placement):
            newbutton = Button(parent, text=name, command=functionname)
            newbutton.pack(side=placement)
            newbutton.configure(width=button_width,\
                                padx=button_padx, pady=button_pady)
            return newbutton
        
        ## constants used  in the initialization
        button_width = 10
        button_padx = "3m"
        button_pady = "3m"

        ## variables used in the program
        self.maxlevel = 6
        self.size = 600  #3**self.maxlevel
        self.maxy = int(self.size * math.sqrt(3) / 2)
        self.stopped = False
        self.depth = 2
        self.wait_time = 1
        self.parent = parent
        
        ## interface elements
        ## all frames
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        self.top_frame = Frame(self.main_frame)
        self.top_frame.pack(side=TOP)
        self.bottom_frame = Frame(self.main_frame)
        self.bottom_frame.pack(side=BOTTOM)

        ## canvases: top for info, buttom for drawing Triangles
        self.infocanvas = Canvas(self.top_frame, \
                                 width=self.size, height=30)
        self.infocanvas.pack(side=TOP)
        self.text_area = self.infocanvas.create_text(30, 10, anchor='nw')
        self.canvas = Canvas(self.top_frame, \
                             width=self.size, height=self.maxy)
        self.canvas.pack(side=BOTTOM)

        ## buttons: for controlling the program
        self.drawbutton = put_button(self.bottom_frame, 'Draw', self.draw, LEFT)
        self.clearbutton = put_button(self.bottom_frame, 'Clear', self.clear, LEFT)
        self.fasterbutton = put_button(self.bottom_frame, \
                                         "Faster", self.faster, LEFT)
        self.slowerbutton = put_button(self.bottom_frame, \
                                         "Slower", self.slower, LEFT)
        self.increasebutton = put_button(self.bottom_frame, \
                                         "Depth+1", self.increase, LEFT)
        self.decreasebutton = put_button(self.bottom_frame, \
                                         "Depth-1", self.decrease, LEFT)
        self.quitbutton = put_button(self.bottom_frame, \
                                     "Quit", self.quit, RIGHT)
        ## display settings for the program on the info canvas
        self.put_info()

    def put_info(self):
        """ Function for displaying the settings for the program, 
            depth and wait time for the animation effect.

        """
        
        info = "Wait time: %d ms" %(self.wait_time)
        if self.depth == self.maxlevel + 3:
            info += " " * 10 + "Depth: %d (max level reached)" % self.depth
        elif self.depth == 0:
            info += " " * 10 + "Depth: 0 (min level reached)"
        else:
            info += " " * 10 + "Depth: %d" % self.depth
        self.infocanvas.itemconfigure(self.text_area, text=info)

    def clear(self):
        """ Clear the drawing (used in self.clearbutton). """
        self.canvas.delete("all")
        
    def faster(self):
        """ Make the animation faster (used in self.fasterbutton). """
        self.wait_time //= 2
        if self.wait_time <= 0:
            self.wait_time = 1
        self.put_info()

    def slower(self):
        """ Make the animation slower (used in self.slowerbutton). """
        self.wait_time *= 2
        self.put_info()
        
    def increase(self):
        """ Increases the depth for recursion (used in self.fasterbutton). """
        if self.depth < self.maxlevel + 3: 
            self.depth += 1
            self.put_info()
        
    def decrease(self):
        """ Decreases the depth for recursion (used in self.slowerbutton). """
        if self.depth > 0:
            self.depth -= 1
            self.put_info()
            
    def draw(self):
        """ Clear the canvas and draws the Sierpinksi triangles (used in self.drawbutton). """
        padding = 20 ##just leave some space off the corners
        if not self.stopped:
            self.clear()
            self.draw_triangles(0 + padding, self.maxy - padding, self.size - 2 * padding, 1)
            
    def draw_triangles(self, x, y, length, depth):
        """ Draws two triangles: one with x,y as the bottom left corner,
            in red and a second inverted one inside between the midpoints
            of the outside triangle, in white.

        """
        ## Triangle 1: Outside Triangle
        mid = length / 2
        self.canvas.create_polygon(x, y, \
                                   x + length, y, \
                                   x + mid, y - math.sqrt(3) * mid,\
                                   fill = "red")
            
        if depth <= self.depth:
            ## Triangle 2: Inside Triangle
            leftmid = (x + mid / 2, y - (math.sqrt(3) * mid) / 2)
            rightmid = (x + (length + mid) / 2, y - (math.sqrt(3) * mid) / 2)
            bottommid = (x + mid, y)
            
            self.canvas.create_polygon(leftmid[0], leftmid[1], \
                                       rightmid[0], rightmid[1], \
                                       bottommid[0], bottommid[1], \
                                       fill = "white")
            self.draw_triangles(x, y, length / 2, depth + 1)
            self.draw_triangles(leftmid[0], leftmid[1], length/2, depth + 1)
            self.draw_triangles(x + length / 2, y, length / 2, depth + 1)
            ## Add animation effect
            self.canvas.update()
            self.canvas.after(self.wait_time)
            
    def quit(self):
        self.stopped = True
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Recursion Example with Sierpinski Triangles")
    myApp = MyApp(root)
    root.mainloop()
