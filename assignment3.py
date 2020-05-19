#INHERITANCE#

class animal :
    def make_sound(self):
        pass
    def type(self):
        print('Animal')

class man(animal):
    def make_sound(self):
        print('I can talk....')
    def type(self):
        print('I am an animal')   #overriden function

class cat(animal):
    def make_sound(self):
        print('meow.....')

class dog(animal):
    def make_sound(self):
        print('bark.....')

class lion(animal):
    def make_sound(self):
        print('Roar.....')

class horse(animal):
    def make_sound(self):
        print('snort....')

class bear(animal):
    def make_sound(self):
        print('Grawl....')

class goat(animal):
    def make_sound(self):
        print('bleat....')

class jackal(animal):
    def make_sound(self):
        print('Howl....')        

class rabbit(animal):
    def make_sound(self):
        print('squeak..')

class donkey(animal):
    def make_sound(self):
        print('bray....')




class polygon :
    def sides(self):
        pass
    def fact(self):
        print('2-Dimensional shape')

class square(polygon):
    def sides(self):
        print('4-sides')

class triangle(polygon):
    def sides(self):
        print('3-sides')

class trapezium(polygon):
    def sides(self):
        print('4-sides')

class rectangle(polygon):
    def sides(self):
        print('4-sides')

class pentagon(polygon):
    def sides(self):
        print('5-sides')

class hexagon(polygon):
    def sides(self):
        print('6-sides')

class octagon(polygon):
    def sides(self):
        print('8-sides')

class rhombus(polygon):
    def sides(self):
        print('4-sides')
    def fact(self):
        print('All sides are equal')

class quadrilateral(polygon):
    def sides(self):
        print('4-sides')

class decagon(polygon):
    def sides(self):
        print('10-sides')

class parallelogram(polygon):
    def sides(self):
        print('4-sides')
    def fact(self):
        print('Opposite sides are equal')
