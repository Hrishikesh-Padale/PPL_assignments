
class man:
    def make_sound(self):
        print('I can talk....')
    def type(self):
        print('man')
        
class cat:
    def make_sound(self):
        print('meow.....')
    def type(self):
        print('cat')   

class dog:
    def make_sound(self):
        print('bark.....')
    def type(self):
        print('dog')

class lion:
    def make_sound(self):
        print('Roar.....')
    def type(self):
        print('lion')
    
class horse:
    def make_sound(self):
        print('snort....')
    def type(self):
        print('horse')
        
class bear:
    def make_sound(self):
        print('Grawl....')
    def type(self):
        print('bear')
    
class goat:
    def make_sound(self):
        print('bleat....')
    def type(self):
        print('goat')
        
class jackal:
    def make_sound(self):
        print('Howl....')        
    def type(self):
        print('jackal')
    
class rabbit:
    def make_sound(self):
        print('squeak..')
    def type(self):
        print('rabbit')
    
class donkey:
    def make_sound(self):
        print('bray....')
    def type(self):
        print('donkey')


m = man()
c = cat()
d = dog()
l = lion()
h = horse()
b = bear()
g = goat()
j = jackal()
r = rabbit()
do = donkey()
list = [m,c,d,l,h,b,g,j,r,do]
for animal in list:
    animal.type()
    animal.make_sound()
    print('\n')


class square:
    def sides(self):
        print('4-sides')
    def type(self):
        print('square')

class triangle:
    def sides(self):
        print('3-sides')
    def type(self):
        print('triangle')
        
class trapezium:
    def sides(self):
        print('4-sides')
    def type(self):
        print('trapezium')
        
class rectangle:
    def sides(self):
        print('4-sides')
    def type(self):
        print('rectangle')
        
class pentagon:
    def sides(self):
        print('5-sides')
    def type(self):
        print('pentagon')
        
class hexagon:
    def sides(self):
        print('6-sides')
    def type(self):
        print('hexagon')
        
class octagon:
    def sides(self):
        print('8-sides')
    def type(self):
        print('octagon')
        
class rhombus:
    def sides(self):
        print('4-sides')
    def type(self):
        print('rhombus')
        
class quadrilateral:
    def sides(self):
        print('4-sides')
    def type(self):
        print('quadrilateral')
        
class decagon:
    def sides(self):
        print('10-sides')
    def type(self):
        print('decagon')
        
class parallelogram:
    def sides(self):
        print('4-sides')
    def type(self):
        print('parellelogram')    

s = square()
t = triangle()
tr = trapezium()
r = rectangle()
p = pentagon()
h = hexagon()
o = octagon()
rh = rhombus()
q = quadrilateral()
d = decagon()
pa = parallelogram()

shapes = [s,t,tr,r,p,h,o,rh,q,d,pa]
for shape in shapes:
    shape.type()
    shape.sides()
    print('\n')
