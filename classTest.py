class Sample:
    color = 'white'
    size = 30

    def __init__(self, c, s):
        self.color = c
        self.size = s

    def show(self):
        print(self.color)
        print(str(self.size))


class Virtual(Sample):
    texture = 'glass'

    def __init__(self, c, s, t):
        Sample(c, s)
        self.texture = t

    def show(self):
        print(self.color,self.size)
        print(self.texture)


fox = Virtual('red', 77, 'plastic')
fox.show()
