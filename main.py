import math 
from random import randrange
from tkinter import Canvas, Tk, mainloop

class Star:

    __slots__ = ['x', 'y', 'z', 'id', 'radius', 'fill']

    def __init__(self, x, y, z) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.id = None
        self.radius = 1
        self.fill = 'white'

class Star_Field:

    def __init__(self, width, height, depth = 30 , star_num = 800):
        self.master = Tk()
        self.master.title("Star Field")
        self.master.resizable(False, False)
        self.master.maxsize(width, height)
        self.stars = []
        self.fov = 180 * math.pi / 180
        self.view_distance = 0.1
        self.width = width
        self.height = height
        self.max_depth = depth
        self.speed = 0.5

        self.canvas = Canvas(self.master, width = width, height = height , bg = "#000000")
        self.canvas.pack()


        for i in range(star_num):
            star = Star(x = randrange(-self.width, self.width),
                        y = randrange(-self.height, self.height),
                        z = randrange(1, self.max_depth))
            star.id = self.canvas.create_oval(star.x - star.radius, star.y - star.radius, star.x + star.radius, star.y + star.radius,
                                              fill='#FFFFFF')
            self.stars.append(star) 
        self.draw()
        mainloop()

    def draw(self):
        for star in self.stars:
                star.z -= self.speed
                star.radius = (1 - float(star.z) / self.max_depth) * 1.7
                star.fill = int((1 - float(star.z) / self.max_depth) * 255)

                if star.z <= 0:
                    star.x = randrange(-self.width, self.width)
                    star.y = randrange(-self.height, self.height)
                    star.z = self.max_depth
                    star.radius = 1
                    star.fill = 0
                factor = self.fov / (self.view_distance + star.z)
                x = star.x * factor + self.width / 2
                y = -star.y * factor + self.height / 2

                self.canvas.coords(star.id, x - star.radius, y - star.radius, x + star.radius, y + star.radius)
                self.canvas.itemconfig(star.id, fill='#%02x%02x%02x' % (star.fill, star.fill, star.fill))
        self.canvas.after(30, self.draw)

if __name__ ==  '__main__':
    s = Star_Field(800, 600)