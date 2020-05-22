'''
1.Hrishikesh Eknath Padale
S.Y.Computer
Div-2
MIS-111803164

2.Prashant Govidrao Shinde
S.Y.Computer
Div-2
MIS-111803167

'''


import pygame 

pygame.init()

import random

res = (200,200) 
screen = pygame.display.set_mode(res) 
color = (0,0,0) 
color_light = (170,170,170) 
color_dark = (200,60,100) 
width = screen.get_width() 
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel',35)
Resume = smallfont.render('Resume' , True , color)
Save = smallfont.render('Save & Quit' , True , color)
Quit = smallfont.render('Quit' , True , color)
New = smallfont.render('New Game' , True , color)

win = pygame.display.set_mode((830,830))

pygame.display.set_caption("LUDO")

image = pygame.image.load('ludo11.png')

BlueP = pygame.image.load('Blue.png')
GreenP = pygame.image.load('Green.png')
RedP = pygame.image.load('Red.png')
YellowP = pygame.image.load('Yellow.png')
win_img = pygame.image.load('win_img.png')
clock = pygame.time.Clock()

crashed = False

BLUE = True 
GREEN = False 
RED = False 
YELLOW = False

global T
T = 0

################################################## PATH FOR ALL PIECES#########################################################
                                                                                                                             
class path_box():                                                                                                                  
    def __init__(self,x = 0,y = 0,double = False):              
        self.x = x
        self.y = y
        self.double = double
        
###############################################################################################################################


################################################# BLUE PLAYER CLASS ###########################################################

    
class B_player(): 
    def __init__(self,path,init_x,init_y,current_x=0,current_y=0,safe=False,ID=1,win = False,double = False):
        self.ID=ID
        self.path = path
        self.init_x = init_x
        self.init_y = init_y
        self.current_x = init_x
        self.current_y = init_y
        self.safe = safe
        self.win = win
        self.double = double
    def B_move(self,n):
    
        if self.init_x == self.current_x and self.init_y == self.current_y and n == 6:
            self.current_x = self.path[1].x
            self.current_y = self.path[1].y 
            update()
            return   
        
        c = 0                          
        for i in range(58):
         if self.current_x == 415 and self.current_y == 470 :
            break
         
         elif self.path[i].x == self.current_x and self.path[i].y == self.current_y :     
          if i+n > 57 :
            break
          self.current_x = self.path[i+n].x
          self.current_y = self.path[i+n].y
          win.blit(image,(0,0))
          update()
          pygame.display.update()
          c += 1
          break
          
        b_home = False 
        if c == 0:
            print("\nNot allowed") 

################################################################################################################################


################################################## GREEN PLAYER CLASS ##########################################################

class G_player(): 
    def __init__(self,path,init_x,init_y,current_x=0,current_y =0,safe=False,ID=2,win = False,double = False):
        self.ID = ID
        self.path = path
        self.init_x = init_x
        self.init_y = init_y
        self.current_x = init_x
        self.current_y = init_y 
        self.safe = safe
        self.win = win
        self.double = double
    def G_move(self,n):
    
        if self.init_x == self.current_x and self.init_y == self.current_y and n == 6:
            self.current_x = self.path[1].x
            self.current_y = self.path[1].y
            update()
            return
                             
        for i in range(58):
         if self.current_x == 360 and self.current_y == 415 :
            break
         
         elif self.path[i].x == self.current_x and self.path[i].y == self.current_y :     
          if i+n > 57 :
            break
          self.current_x = self.path[i+n].x
          self.current_y = self.path[i+n].y
          win.blit(image,(0,0))
          update()
          pygame.display.update()

          break
    
###############################################################################################################################

###################################### RED PLAYER CLASS ##############################################
class R_player(): 
    def __init__(self,path,init_x,init_y,current_x=0,current_y =0,safe=False,ID=3,win = False,double = False):
        self.ID = ID
        self.path = path
        self.init_x = init_x
        self.init_y = init_y
        self.current_x = init_x
        self.current_y = init_y 
        self.safe = safe
        self.win = win
        self.double = double
    def R_move(self,n):
    
        if self.init_x == self.current_x and self.init_y == self.current_y and n == 6:
            self.current_x = self.path[1].x
            self.current_y = self.path[1].y
            update()
            return
                             
        for i in range(58):
         if self.current_x == 415 and self.current_y == 360 :
            break
         
         elif self.path[i].x == self.current_x and self.path[i].y == self.current_y :     
          if i+n > 57 :
            break
          self.current_x = self.path[i+n].x
          self.current_y = self.path[i+n].y
          win.blit(image,(0,0))
          update()
          pygame.display.update()

          break
###################################################################################################

################################################## YELLOW PLAYER CLASS ##########################################################

class Y_player(): 
    def __init__(self,path,init_x,init_y,current_x=0,current_y =0,safe=False,ID=4,win = False,double = False):
        self.ID = ID
        self.path = path
        self.init_x = init_x
        self.init_y = init_y
        self.current_x = init_x
        self.current_y = init_y 
        self.safe = safe
        self.win = win
        self.double = double
    def Y_move(self,n):
    
        if self.init_x == self.current_x and self.init_y == self.current_y and n == 6:
            self.current_x = self.path[1].x
            self.current_y = self.path[1].y
            update()
            return
                             
        for i in range(58):
         if self.current_x == 470 and self.current_y == 415 :
            break
         
         elif self.path[i].x == self.current_x and self.path[i].y == self.current_y :     
          if i+n > 57 :
            break
          self.current_x = self.path[i+n].x
          self.current_y = self.path[i+n].y
          win.blit(image,(0,0))
          update()
          pygame.display.update()

          break
    
###################################################################################################


class Bbutton():
    def __init__(self, color = (210,150,75), x = 60 ,y = 720 ,width = 50,height = 50, text=" ",status = False):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.status = status

    def draw(self,win,outline =None ):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    '''def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False'''
        
    def clicked(self):
        x = roll()
        self.text = str(x) 
        update()   
        return x

Blue_Button = Bbutton() 

class Gbutton():
    def __init__(self, color = (210,150,75), x = 60 ,y = 60 ,width = 50,height = 50, text=" ",status = False):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.status = status

    def draw(self,win,outline =None ):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        
    def clicked(self):
        x = roll()
        self.text = str(x) 
        update()   
        return x

Green_Button = Gbutton()


class Rbutton():
    def __init__(self, color = (210,150,75), x = 720 ,y = 60 ,width = 50,height = 50, text=" ",status = False):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.status = status

    def draw(self,win,outline =None ):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


    def clicked(self):
        x = roll()
        self.text = str(x) 
        update()   
        return x

Red_Button = Rbutton()

class Ybutton():
    def __init__(self, color = (210,150,75), x = 720 ,y = 720 ,width = 50,height = 50, text=" ",status = False):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.status = status

    def draw(self,win,outline =None ):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
       
    def clicked(self):
        x = roll()
        self.text = str(x) 
        update()   
        return x
    

Yellow_Button = Ybutton()

def roll():
    y = random.randrange(1,7)
    return y

class Label():
    def __init__(self, color = (200,200,0), x = 390 ,y = 390 ,width = 50,height = 50, text="Blue's Turn"):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline =None ):
            
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (255,0,255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

label = Label()

'''############################################# INITIALIZE 4 BLUE PIECES #######################################################       
              
B_path = [path_box() for i in range(58)]
B_1 = B_player(B_path,195,690)
B_2 = B_player(B_path,195,635)
B_3 = B_player(B_path,140,635)
B_4 = B_player(B_path,140,690)

###################################################################################################################################

############################################### INITIALIZE 4 GREEN PIECES #####################################################

G_path = [path_box() for i in range(58)]
G_1 = G_player(G_path,140,140)
G_2 = G_player(G_path,195,140)
G_3 = G_player(G_path,140,195)
G_4 = G_player(G_path,195,195)

#############################################################################################################################

############################################### INITIALIZE 4 RED PIECES #####################################################

R_path = [path_box() for i in range(58)]
R_1 = R_player(R_path,635,140)
R_2 = R_player(R_path,690,140)
R_3 = R_player(R_path,635,195)
R_4 = R_player(R_path,690,195)

#############################################################################################################################

############################################### INITIALIZE 4 YELLOW PIECES #####################################################

Y_path = [path_box() for i in range(58)]
Y_1 = Y_player(Y_path,690,690)
Y_2 = Y_player(Y_path,690,635)
Y_3 = Y_player(Y_path,635,635)
Y_4 = Y_player(Y_path,635,690)'''

####################################################################################################

################################################  CHECK SAFETY ##################################################################
    
def check_safety(P):
    if  0 <= P.current_x <= 335 and 0 <= P.current_y <= 335:
        P.safe = True
        return
    if  0 <= P.current_x <= 335 and 495 <= P.current_y <= 830:
        P.safe = True
        return
    if  490 <= P.current_x <= 830 and 0 <= P.current_y <= 335:
        P.safe = True
        return
    if 495 <= P.current_x <= 830 and  495 <= P.current_y <= 830 :
        P.safe = True
        return
    if 135 <= P.current_x <= 145 and 465 <= P.current_y <= 475 :
        P.safe = True
        return
    if 355 <= P.current_x <= 365 and 135 <= P.current_y <= 145 :
        P.safe = True
        return
    if 685 <= P.current_x <= 695 and 355 <= P.current_y <= 365 :
        P.safe = True
        return
    if 465 <= P.current_x <= 475 and 685 <= P.current_y <= 695 :
        P.safe = True
        return
    if 65 <= P.current_x <= 115 and 335 <= P.current_y <= 385 :
        P.safe = True
        return
    if 445 <= P.current_x <= 495 and 65 <= P.current_y <= 115 :
        P.safe = True
        return 
    if 720 <= P.current_x <= 770 and 445 <= P.current_y <= 495 :
        P.safe = True
        return
    if 390 <= P.current_x <= 440 and 725 <= P.current_y <= 775 :
        P.safe = True
        return
    if 355 <= P.current_x <= 365 and 740 <= P.current_y <= 750 :
        P.safe = True
        return
    
    else :
        P.safe = False
    
################################################################################################################################

def check_same():
    if B_1.current_x == B_2.current_x and B_1.current_y == B_2.current_y :
        B_1.safe = True
        B_2.safe = True
        return
    if B_1.current_x == B_3.current_x and B_1.current_y == B_3.current_y :
        B_1.safe = True
        B_3.safe = True
        return
    if B_1.current_x == B_4.current_x and B_1.current_y == B_4.current_y :
        B_1.safe = True
        B_2.safe = True
        return
    if B_2.current_x == B_3.current_x and B_2.current_y == B_3.current_y :
        B_2.safe = True
        B_3.safe = True
        return
    if B_2.current_x == B_4.current_x and B_2.current_y == B_4.current_y :
        B_2.safe = True
        B_4.safe = True
        return
    if B_3.current_x == B_4.current_x and B_3.current_y == B_4.current_y :
        B_3.safe = True
        B_4.safe = True
        return

    if G_1.current_x == G_2.current_x and G_1.current_y == G_2.current_y :
        G_1.safe = True
        G_2.safe = True
        return
    if G_1.current_x == G_3.current_x and G_1.current_y == G_3.current_y :
        G_1.safe = True
        G_3.safe = True
        return
    if G_1.current_x == G_4.current_x and G_1.current_y == G_4.current_y :
        G_1.safe = True
        G_2.safe = True
        return
    if G_2.current_x == G_3.current_x and G_2.current_y == G_3.current_y :
        G_2.safe = True
        G_3.safe = True
        return
    if G_2.current_x == G_4.current_x and G_2.current_y == G_4.current_y :
        G_2.safe = True
        G_4.safe = True
        return
    if G_3.current_x == G_4.current_x and G_3.current_y == G_4.current_y :
        G_3.safe = True
        G_4.safe = True
        return

    if R_1.current_x == R_2.current_x and R_1.current_y == R_2.current_y :
        R_1.safe = True
        R_2.safe = True
        return
    if R_1.current_x == R_3.current_x and R_1.current_y == R_3.current_y :
        R_1.safe = True
        R_3.safe = True
        return
    if R_1.current_x == R_4.current_x and R_1.current_y == R_4.current_y :
        R_1.safe = True
        R_2.safe = True
        return
    if R_2.current_x == R_3.current_x and R_2.current_y == R_3.current_y :
        R_2.safe = True
        R_3.safe = True
        return
    if R_2.current_x == R_4.current_x and R_2.current_y == R_4.current_y :
        R_2.safe = True
        R_4.safe = True
        return
    if R_3.current_x == R_4.current_x and R_3.current_y == R_4.current_y :
        R_3.safe = True
        R_4.safe = True
        return



B_path = [path_box() for i in range(58)]
G_path = [path_box() for i in range(58)]
R_path = [path_box() for i in range(58)]
Y_path = [path_box() for i in range(58)]
################################################### MAKE PATH FOR BLUE PIECES #######################################################

def makepath_BLUE(B):   #function to make path for blue pieces
 
 a = 0
 for i in range(6):
    B.path[i].x = 360
    B_path[i].y = 800-(a*55) 
    a += 1  

 j = 0
 for i in range(6,12):
    B.path[i].x = 305-(j*55)
    B.path[i].y = 470
    j += 1
 
 k = 0
 for i in range(12,14):
     B.path[i].x = 30
     B.path[i].y = 415-(k*55)  
     k += 1

 l = 0
 for i in range(14,19):
     B.path[i].x = 85+(l*55)
     B.path[i].y = 360  
     l += 1    
 
 m = 0
 for i in range(19,25):
     B.path[i].x = 360
     B.path[i].y = 305-(m*55) 
     m += 1
 
 n = 0    
 for i in range(25,27):
     B.path[i].x = 415+(n*55)
     B.path[i].y = 30 
     n += 1 
     
 o=0
 for i in range(27,32):
     B.path[i].x = 470
     B.path[i].y = 85+(o*55)  
     o += 1 
 
 p = 0 
 for i in range(32,38):
     B.path[i].x = 525+(p*55) 
     B.path[i].y = 360  
     p += 1     
        
 q = 0
 for i in range(38,40):
     B.path[i].x = 800
     B.path[i].y = 415+(q*55)  
     q += 1 
     
 r = 0 
 for i in range(40,45):
     B.path[i].x = 745-(r*55)
     B.path[i].y = 470 
     r += 1   
     
 s = 0 
 for i in range(45,51):
     B.path[i].x = 470
     B.path[i].y = 525+(s*55)
     s += 1 
 
 t = 0 
 for i in range(51,58):
     B.path[i].x = 415
     B.path[i].y = 800-(t*55) 
     t += 1       




    
'''for i in range(0,58):
    print("Blue :",i,B_path[i].x,B_path[i].y)'''
###################################################################################################################################    

################################################## MAKE PATH FOR GREEN PIECES #####################################################

def makepath_GREEN(G):
  
  a = 0
  for i in range(6):
    G.path[i].x = 30+(a*55)
    G.path[i].y = 360
    a += 1
    
  b = 0 
  for i in range(6,12):
    G.path[i].x = 360
    G.path[i].y = 305-(b*55)
    b += 1
    
  c = 0 
  for i in range(12,14):
    G.path[i].x = 415+(c*55)
    G.path[i].y = 30
    c += 1  
   
  d = 0
  for i in range(14,19):
    G.path[i].x = 470
    G.path[i].y = 85+(d*55)
    d += 1
  
  e = 0
  for i in range(19,25):
    G.path[i].x = 525+(e*55)
    G.path[i].y = 360
    e += 1
  
  f = 0 
  for i in range(25,27):
    G.path[i].x = 800
    G.path[i].y = 415+(f*55)
    f+= 1
    
  g = 0
  for i in range(27,32):
    G.path[i].x = 745-(g*55)
    G.path[i].y = 470
    g += 1
  
  h = 0
  for i in range(32,38):
    G.path[i].x = 470
    G.path[i].y = 525+(h*55)
    h += 1  
    
  j = 0
  for i in range(38,40):
    G.path[i].x = 415-(j*55)
    G.path[i].y = 800
    j += 1   
    
  k = 0
  for i in range(40,45):
    G.path[i].x = 360
    G.path[i].y = 745-(k*55)
    k += 1  
  
  l = 0
  for i in range(45,51):
    G.path[i].x = 305-(l*55)
    G.path[i].y = 470
    l += 1  
  
  m = 0
  for i in range(51,58):
    G.path[i].x = 30+(m*55)
    G.path[i].y = 415
    m += 1
  
 
'''for i in range(58):
    print("Green :",i,G_path[i].x,G_path[i].y)'''

###################################################################################################################################

################################################## MAKE PATH FOR RED PIECES #####################################################

def makepath_RED(R):

    a = 0
    for i in range(6):
        R.path[i].x = 470
        R.path[i].y = 30+(a*55)
        a += 1

    b = 0
    for i in range(6,12):
        R.path[i].x = 525+(b*55)
        R.path[i].y = 360
        b += 1
        
    c = 0
    for i in range(12,14):
        R.path[i].x = 800
        R.path[i].y = 415+(c*55)
        c += 1

    d = 0
    for i in range(14,19):
        R.path[i].x = 745-(d*55)
        R.path[i].y = 470
        d += 1

    e = 0
    for i in range(19,25):
        R.path[i].x = 470
        R.path[i].y = 525+(e*55)
        e += 1

    f = 0
    for i in range(25,27):
        R.path[i].x = 415-(f*55)
        R.path[i].y = 800
        f += 1

    g = 0
    for i in range(27,32):
        R.path[i].x = 360
        R.path[i].y = 745-(g*55)
        g += 1

    h = 0
    for i in range(32,38): 
        R.path[i].x = 305-(h*55)
        R.path[i].y = 470
        h+= 1

    j = 0
    for i in range(38,40):
        R.path[i].x = 30
        R.path[i].y = 415-(j*55)
        j += 1

    k = 0
    for i in range(40,45):
        R.path[i].x = 85+(k*55) 
        R.path[i].y = 360
        k += 1

    l = 0
    for i in range(45,51):
        R.path[i].x = 360
        R.path[i].y = 305-(l*55)
        l += 1
        
    m = 0
    for i in range(51,58):
        R.path[i].x = 415
        R.path[i].y = 30+(m*55)
        m +=1


'''for i in range(58):
    print("Red :",i,R_path[i].x,R_path[i].y)'''
        
############################################## FUNCTION TO CHECK KILL ############################################################

################################################### MAKE PATH FOR YELLOW PIECES #######################################################

def makepath_YELLOW(Y):   #function to make path for blue pieces
 
 a = 0
 for i in range(6):
    Y.path[i].x = 800-(a*55) 
    Y_path[i].y = 470
    a += 1  

 b = 0
 for i in range(6,12):
    Y.path[i].x = 470
    Y_path[i].y = 525+(b*55)
    b += 1

 c = 0
 for i in range(12,14):
    Y.path[i].x = 415-(c*55)
    Y_path[i].y = 800
    c +=1

 d = 0
 for i in range(14,19):
    Y.path[i].x = 360
    Y_path[i].y = 745-(d*55)
    d += 1

 e = 0
 for i in range(19,25):
    Y.path[i].x = 305-(e*55)
    Y_path[i].y = 470
    e += 1

 f = 0
 for i in range(25,27):
    Y.path[i].x = 30
    Y_path[i].y = 415-(f*55)
    f += 1

 g = 0
 for i in range(27,32):
    Y.path[i].x = 85+(g*55)
    Y_path[i].y = 360
    g += 1

 h = 0
 for i in range(32,38):
    Y.path[i].x = 360
    Y_path[i].y = 305-(h*55)
    h += 1

 j = 0
 for i in range(38,40):
    Y.path[i].x = 415+(j*55)
    Y_path[i].y = 30
    j += 1   

 k = 0
 for i in range(40,45):
    Y.path[i].x = 470
    Y_path[i].y = 85+(k*55)
    k += 1

 l = 0
 for i in range(45,51):
    Y.path[i].x = 525+(l*55)
    Y_path[i].y = 360
    l += 1

 m = 0
 for i in range(51,58):
    Y.path[i].x = 800-(m*55)
    Y_path[i].y = 415
    m += 1



'''for i in range(58):
    print("Yellow :",i,Y_path[i].x,Y_path[i].y)'''
    
###################################################################################################

    
######################################## NEW GAME  ##################################################
             
B_1 = B_player(B_path,195,690)
B_2 = B_player(B_path,195,635)
B_3 = B_player(B_path,140,635)
B_4 = B_player(B_path,140,690)
G_1 = G_player(G_path,140,140)
G_2 = G_player(G_path,195,140)
G_3 = G_player(G_path,140,195)
G_4 = G_player(G_path,195,195)
R_1 = R_player(R_path,635,140)
R_2 = R_player(R_path,690,140)
R_3 = R_player(R_path,635,195)
R_4 = R_player(R_path,690,195)
Y_1 = Y_player(Y_path,690,690)
Y_2 = Y_player(Y_path,690,635)
Y_3 = Y_player(Y_path,635,635)
Y_4 = Y_player(Y_path,635,690)
makepath_BLUE(B_1)    #CALL FUNCTION TO MAKE PATH
makepath_BLUE(B_2)
makepath_BLUE(B_3)
makepath_BLUE(B_4)
makepath_GREEN(G_1)    #CALL FUNCTION TO MAKE PATH
makepath_GREEN(G_2)
makepath_GREEN(G_3)
makepath_GREEN(G_4)
makepath_RED(R_1)    #CALL FUNCTION TO MAKE PATH
makepath_RED(R_2)
makepath_RED(R_3)
makepath_RED(R_4)
makepath_YELLOW(Y_1)
makepath_YELLOW(Y_2)
makepath_YELLOW(Y_3)
makepath_YELLOW(Y_4)


################################################## FUNCTION TO UPDATE ALL PIECES ON SCREEN ######################################    


def update():

    win.blit(BlueP,(B_1.current_x-25,B_1.current_y-25))
    win.blit(BlueP,(B_2.current_x-25,B_2.current_y-25))
    win.blit(BlueP,(B_3.current_x-25,B_3.current_y-25))
    win.blit(BlueP,(B_4.current_x-25,B_4.current_y-25))
    win.blit(GreenP,(G_1.current_x-25,G_1.current_y-25))
    win.blit(GreenP,(G_2.current_x-25,G_2.current_y-25))
    win.blit(GreenP,(G_3.current_x-25,G_3.current_y-25))
    win.blit(GreenP,(G_4.current_x-25,G_4.current_y-25))
    win.blit(RedP,(R_1.current_x-25,R_1.current_y-25))
    win.blit(RedP,(R_2.current_x-25,R_2.current_y-25))
    win.blit(RedP,(R_3.current_x-25,R_3.current_y-25))
    win.blit(RedP,(R_4.current_x-25,R_4.current_y-25))
    win.blit(YellowP,(Y_1.current_x-25,Y_1.current_y-25))
    win.blit(YellowP,(Y_2.current_x-25,Y_2.current_y-25))
    win.blit(YellowP,(Y_3.current_x-25,Y_3.current_y-25))
    win.blit(YellowP,(Y_4.current_x-25,Y_4.current_y-25))
    check_safety(B_1)
    check_safety(B_2)
    check_safety(B_3)
    check_safety(B_4)
    check_safety(G_1)
    check_safety(G_2)
    check_safety(G_3)
    check_safety(G_4)
    check_safety(R_1)
    check_safety(R_2)
    check_safety(R_3)
    check_safety(R_4)
    check_safety(Y_1)
    check_safety(Y_2)
    check_safety(Y_3)
    check_safety(Y_4)
    checkwin_blue()
    checkwin_green()
    checkwin_red()
    Blue_Button.draw(win)  
    Green_Button.draw(win)
    Red_Button.draw(win)
    Yellow_Button.draw(win)
            
        
    if T == 0:
     win.blit(text1, textRect1)
    if T == 1 :   
     win.blit(text2, textRect2)
    if T == 2 :
     win.blit(text3,textRect3)
    if T == 3 :
     win.blit(text4,textRect4)
    if T == 4:
     win.blit(lost1, lostRect1)
    if T == 5:
     win.blit(lost2, lostRect2)
    if T == 6:
     win.blit(lost3, lostRect3)
    if T == 7:
     win.blit(lost4, lostRect4)
    x = checkwin_blue()
    y = checkwin_green()
    z = checkwin_red()
    v = checkwin_yellow()
    if x == True :
        win.blit(win_img,(60,555))
    if y == True :
        win.blit(win_img,(60,60))
    if z == True:
        win.blit(win_img,(555,60))
    if v == True :
        win.blit(win_img,(555,555))
################################################################################################################################  


def kill(P):
    update()
    check_same()
    if P.ID == 1 :
        if P.current_x == G_1.current_x and P.current_y == G_1.current_y and G_1.safe == False : 
         G_1.current_x = G_1.init_x
         G_1.current_y = G_1.init_y
         return True
       
        elif P.current_x == G_2.current_x and P.current_y == G_2.current_y and G_2.safe == False :
         G_2.current_x = G_2.init_x
         G_2.current_y = G_2.init_y
         return True
        
        elif P.current_x == G_3.current_x and P.current_y == G_3.current_y and G_3.safe == False :
         G_3.current_x = G_3.init_x
         G_3.current_y = G_3.init_y
         return True
        
        elif P.current_x == G_4.current_x and P.current_y == G_4.current_y  and G_4.safe == False :
         G_4.current_x = G_4.init_x
         G_4.current_y = G_4.init_y
         return True

        elif P.current_x == R_1.current_x and P.current_y == R_1.current_y and R_1.safe == False : 
         R_1.current_x = R_1.init_x
         R_1.current_y = R_1.init_y
         return True
       
        elif P.current_x == R_2.current_x and P.current_y == R_2.current_y and R_2.safe == False :
         R_2.current_x = R_2.init_x
         R_2.current_y = R_2.init_y
         return True
            
        elif P.current_x == R_3.current_x and P.current_y == R_3.current_y and R_3.safe == False :
         R_3.current_x = R_3.init_x
         R_3.current_y = R_3.init_y
         return True
        
        elif P.current_x == R_4.current_x and P.current_y == R_4.current_y  and R_4.safe == False :
         R_4.current_x = R_4.init_x
         R_4.current_y = R_4.init_y
         return True

        elif P.current_x == Y_1.current_x and P.current_y == Y_1.current_y and Y_1.safe == False : 
         Y_1.current_x = Y_1.init_x
         Y_1.current_y = Y_1.init_y
         return True
       
        elif P.current_x == Y_2.current_x and P.current_y == Y_2.current_y and Y_2.safe == False :
         Y_2.current_x = Y_2.init_x
         Y_2.current_y = Y_2.init_y
         return True
        
        elif P.current_x == Y_3.current_x and P.current_y == Y_3.current_y and Y_3.safe == False :
         Y_3.current_x = Y_3.init_x
         Y_3.current_y = Y_3.init_y
         return True
        
        elif P.current_x == Y_4.current_x and P.current_y == Y_4.current_y  and Y_4.safe == False :
         Y_4.current_x = Y_4.init_x
         Y_4.current_y = Y_4.init_y
         return True
       
    
    if P.ID == 2: 
        if P.current_x == B_1.current_x and P.current_y == B_1.current_y and B_1.safe == False : 
         B_1.current_x = B_1.init_x
         B_1.current_y = B_1.init_y
         return True
        
        elif P.current_x == B_2.current_x and P.current_y == B_2.current_y and B_2.safe == False :
         B_2.current_x = B_2.init_x
         B_2.current_y = B_2.init_y
         return True
       
        elif P.current_x == B_3.current_x and P.current_y == B_3.current_y and B_3.safe == False :
         B_3.current_x = B_3.init_x
         B_3.current_y = B_3.init_y
         return True
       
        elif P.current_x == B_4.current_x and P.current_y == B_4.current_y  and B_4.safe == False :
         B_4.current_x = B_4.init_x
         B_4.current_y = B_4.init_y
         return True

        elif P.current_x == R_1.current_x and P.current_y == R_1.current_y and R_1.safe == False : 
         R_1.current_x = R_1.init_x
         R_1.current_y = R_1.init_y
         return True
       
        elif P.current_x == R_2.current_x and P.current_y == R_2.current_y and R_2.safe == False :
         R_2.current_x = R_2.init_x
         R_2.current_y = R_2.init_y
         return True
        
        elif P.current_x == R_3.current_x and P.current_y == R_3.current_y and R_3.safe == False :
         R_3.current_x = R_3.init_x
         R_3.current_y = R_3.init_y
         return True
        
        elif P.current_x == R_4.current_x and P.current_y == R_4.current_y  and R_4.safe == False :
         R_4.current_x = R_4.init_x
         R_4.current_y = R_4.init_y
         return True

        elif P.current_x == Y_1.current_x and P.current_y == Y_1.current_y and Y_1.safe == False : 
         Y_1.current_x = Y_1.init_x
         Y_1.current_y = Y_1.init_y
         return True
       
        elif P.current_x == Y_2.current_x and P.current_y == Y_2.current_y and Y_2.safe == False :
         Y_2.current_x = Y_2.init_x
         Y_2.current_y = Y_2.init_y
         return True
        
        elif P.current_x == Y_3.current_x and P.current_y == Y_3.current_y and Y_3.safe == False :
         Y_3.current_x = Y_3.init_x
         Y_3.current_y = Y_3.init_y
         return True
        
        elif P.current_x == Y_4.current_x and P.current_y == Y_4.current_y  and Y_4.safe == False :
         Y_4.current_x = Y_4.init_x
         Y_4.current_y = Y_4.init_y
         return True

    if P.ID == 3: 
        if P.current_x == B_1.current_x and P.current_y == B_1.current_y and B_1.safe == False : 
         B_1.current_x = B_1.init_x
         B_1.current_y = B_1.init_y
         return True
        
        elif P.current_x == B_2.current_x and P.current_y == B_2.current_y and B_2.safe == False :
         B_2.current_x = B_2.init_x
         B_2.current_y = B_2.init_y
         return True
       
        elif P.current_x == B_3.current_x and P.current_y == B_3.current_y and B_3.safe == False :
         B_3.current_x = B_3.init_x
         B_3.current_y = B_3.init_y
         return True
       
        elif P.current_x == B_4.current_x and P.current_y == B_4.current_y  and B_4.safe == False :
         B_4.current_x = B_4.init_x
         B_4.current_y = B_4.init_y
         return True

        elif P.current_x == G_1.current_x and P.current_y == G_1.current_y and G_1.safe == False : 
         G_1.current_x = G_1.init_x
         G_1.current_y = G_1.init_y
         return True
       
        elif P.current_x == G_2.current_x and P.current_y == G_2.current_y and G_2.safe == False :
         G_2.current_x = G_2.init_x
         G_2.current_y = G_2.init_y
         return True
        
        elif P.current_x == G_3.current_x and P.current_y == G_3.current_y and G_3.safe == False :
         G_3.current_x = G_3.init_x
         G_3.current_y = G_3.init_y
         return True
        
        elif P.current_x == G_4.current_x and P.current_y == G_4.current_y  and G_4.safe == False :
         G_4.current_x = G_4.init_x
         G_4.current_y = G_4.init_y
         return True

        elif P.current_x == Y_1.current_x and P.current_y == Y_1.current_y and Y_1.safe == False : 
         Y_1.current_x = Y_1.init_x
         Y_1.current_y = Y_1.init_y
         return True
       
        elif P.current_x == Y_2.current_x and P.current_y == Y_2.current_y and Y_2.safe == False :
         Y_2.current_x = Y_2.init_x
         Y_2.current_y = Y_2.init_y
         return True
        
        elif P.current_x == Y_3.current_x and P.current_y == Y_3.current_y and Y_3.safe == False :
         Y_3.current_x = Y_3.init_x
         Y_3.current_y = Y_3.init_y
         return True
        
        elif P.current_x == Y_4.current_x and P.current_y == Y_4.current_y  and Y_4.safe == False :
         Y_4.current_x = Y_4.init_x
         Y_4.current_y = Y_4.init_y
         return True

    if P.ID == 4: 
        if P.current_x == B_1.current_x and P.current_y == B_1.current_y and B_1.safe == False : 
         B_1.current_x = B_1.init_x
         B_1.current_y = B_1.init_y
         return True
        
        elif P.current_x == B_2.current_x and P.current_y == B_2.current_y and B_2.safe == False :
         B_2.current_x = B_2.init_x
         B_2.current_y = B_2.init_y
       
        elif P.current_x == B_3.current_x and P.current_y == B_3.current_y and B_3.safe == False :
         B_3.current_x = B_3.init_x
         B_3.current_y = B_3.init_y
         return True
       
        elif P.current_x == B_4.current_x and P.current_y == B_4.current_y  and B_4.safe == False :
         B_4.current_x = B_4.init_x
         B_4.current_y = B_4.init_y
         return True

        elif P.current_x == G_1.current_x and P.current_y == G_1.current_y and G_1.safe == False : 
         G_1.current_x = G_1.init_x
         G_1.current_y = G_1.init_y
         return True
       
        elif P.current_x == G_2.current_x and P.current_y == G_2.current_y and G_2.safe == False :
         G_2.current_x = G_2.init_x
         G_2.current_y = G_2.init_y
         return True
        
        elif P.current_x == G_3.current_x and P.current_y == G_3.current_y and G_3.safe == False :
         G_3.current_x = G_3.init_x
         G_3.current_y = G_3.init_y
         return True
        
        elif P.current_x == G_4.current_x and P.current_y == G_4.current_y  and G_4.safe == False :
         G_4.current_x = G_4.init_x
         G_4.current_y = G_4.init_y
         return True

        elif P.current_x == R_1.current_x and P.current_y == R_1.current_y and R_1.safe == False : 
         R_1.current_x = R_1.init_x
         R_1.current_y = R_1.init_y
         return True
       
        elif P.current_x == R_2.current_x and P.current_y == R_2.current_y and R_2.safe == False :
         R_2.current_x = R_2.init_x
         R_2.current_y = R_2.init_y
         return True
        
        elif P.current_x == R_3.current_x and P.current_y == R_3.current_y and R_3.safe == False :
         R_3.current_x = R_3.init_x
         R_3.current_y = R_3.init_y
         return True
        
        elif P.current_x == R_4.current_x and P.current_y == R_4.current_y  and R_4.safe == False :
         R_4.current_x = R_4.init_x
         R_4.current_y = R_4.init_y
         return True
         
    update()
    
##################################################################################################################################

def movecheck(P,n):
    if P.current_x == P.init_x and P.current_y == P.init_y and n != 6:
        update()
        return False
    elif 335 <= P.current_x <= 500 and 335 <= P.current_y <= 500 :
        update()
        return False
    elif P.current_x != P.init_x and P.current_y != P.init_y:
        i = 0
        for i in range(58):
         if P.path[i].x == P.current_x and P.path[i].y == P.current_y:
            break
         i += 1
        if i+n > 58:    
            return False
        else :
            return True
    else :
         return True
        

def clear(B):
    B.text = ' '
    B.draw(win)

font = pygame.font.Font('freesansbold.ttf', 32) 
  
text1 = font.render("Blue's turn", True, (255,0,255)) 
  
textRect1 = text1.get_rect()  
  
textRect1.center = (830 // 2, 830 // 2)

text2 = font.render("Green's turn", True, (255,0,255)) 
  
textRect2 = text2.get_rect()  
  
textRect2.center = (830 // 2, 830 // 2)

text3 = font.render("Red's turn", True, (255,0,255)) 
  
textRect3 = text3.get_rect()  
  
textRect3.center = (830 // 2, 830 // 2)

text4 = font.render("Yellow's Turn",True,(255,0,255))

textRect4 = text4.get_rect()

textRect4.center = (830 // 2, 830 // 2)

lost1 = font.render("Blue Player Lost", True, (255,0,255)) 
  
lostRect1 = lost1.get_rect()  
  
lostRect1.center = (830 // 2, 830 // 2)

lost2 = font.render("Green Player Lost", True, (255,0,255)) 
  
lostRect2= lost2.get_rect()  
  
lostRect2.center = (830 // 2, 830 // 2)

lost3 = font.render("Red Player Lost", True, (255,0,255)) 
  
lostRect3 = lost3.get_rect()  
  
lostRect3.center = (830 // 2, 830 // 2)

lost4 = font.render("Yellow Player Lost", True, (255,0,255)) 
  
lostRect4 = lost4.get_rect()  
  
lostRect4.center = (830 // 2, 830 // 2)

#____________________________________________________________________________________________________________________________________#
def checkwin(P):
    if 335 <= P.current_x <= 500 and 335 <= P.current_y <= 500 :
        P.win = True
#____________________________________________________________________________________________________________________________________#

    
#____________________________________________________________________________________________________________________________________#
def checkwin_blue():
    if B_1.win == B_2.win == B_3.win == B_4.win == True:
        return True
#____________________________________________________________________________________________________________________________________#
    
#____________________________________________________________________________________________________________________________________#
def checkwin_green():
    if G_1.win == G_2.win == G_3.win == G_4.win == True:
        return True
#____________________________________________________________________________________________________________________________________#

#____________________________________________________________________________________________________________________________________#
def checkwin_red():
    if R_1.win == R_2.win == R_3.win == R_4.win == True:
        return True
#____________________________________________________________________________________________________________________________________#

#____________________________________________________________________________________________________________________________________#
def checkwin_yellow():
    if Y_1.win == Y_2.win == Y_3.win == Y_4.win == True:
        return True
#____________________________________________________________________________________________________________________________________#

x=None
y =None
z = None
v = None
def result():


    if x != True and y == True and z == True and v == True :
            BLUE = False
            GREEN = False
            RED = False
            YELLOW = False
            T = 4
            win.blit(lost1, lostRect1)
    elif x == True and y != True and z == True and v == True :
            BLUE = False
            GREEN = False
            RED = False
            YELLOW = False
            T = 5
            win.blit(lost2, lostRect2)
    elif x == True and y == True and z != True and v == True :
            BLUE = False
            GREEN = False
            RED = False
            YELLOW = False
            T = 6
            win.blit(lost3, lostRect3)
    elif x == True and y == True and z == True and v != True :
            BLUE = False
            GREEN = False
            RED = False
            YELLOW = False
            T = 6
            win.blit(lost4, lostRect4)
    update()            
#____________________________________________________________________________________________________________________________________#

file = open('save.txt','r')
s = file.readlines()
if s != []:     
        B_1.current_x = int(s[0])
        B_2.current_x = int(s[1])
        B_3.current_x = int(s[2])
        B_4.current_x = int(s[3])
        B_1.current_y = int(s[4])
        B_2.current_y = int(s[5])
        B_3.current_y = int(s[6])
        B_4.current_y = int(s[7])

        G_1.current_x = int(s[8])
        G_2.current_x = int(s[9])
        G_3.current_x = int(s[10])
        G_4.current_x = int(s[11])
        G_1.current_y = int(s[12])
        G_2.current_y = int(s[13])
        G_3.current_y = int(s[14])
        G_4.current_y = int(s[15])

        R_1.current_x = int(s[16])
        R_2.current_x = int(s[17])
        R_3.current_x = int(s[18])
        R_4.current_x = int(s[19])
        R_1.current_y = int(s[20])
        R_2.current_y = int(s[21])
        R_3.current_y = int(s[22])
        R_4.current_y = int(s[23])

        Y_1.current_x = int(s[24])
        Y_2.current_x = int(s[25])
        Y_3.current_x = int(s[26])
        Y_4.current_x = int(s[27])
        Y_1.current_y = int(s[28])
        Y_2.current_y = int(s[29])
        Y_3.current_y = int(s[30])
        Y_4.current_y = int(s[31])

file.close()


    
while not crashed:
    win.blit(image,(0,0))
    update()    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            while not done: 
                for ev in pygame.event.get(): 
                    if ev.type == pygame.MOUSEBUTTONDOWN: 
                        if 50 <= mouse[0] <= 170 and 50 <= mouse[1] <= 90: 
                            done = True
                        if 200 <= mouse[0] <= 370 and 50 <= mouse[1] <= 90 : 
                             file = open('save.txt','w')
                             file.write(str(B_1.current_x))
                             file.write('\n')
                             file.write(str(B_2.current_x))
                             file.write('\n')
                             file.write(str(B_3.current_x))
                             file.write('\n')
                             file.write(str(B_4.current_x))
                             file.write('\n')
                             file.write(str(B_1.current_y))
                             file.write('\n')
                             file.write(str(B_2.current_y))
                             file.write('\n')
                             file.write(str(B_3.current_y))
                             file.write('\n')
                             file.write(str(B_4.current_y))
                             file.write('\n')
                             file.write(str(G_1.current_x))
                             file.write('\n')
                             file.write(str(G_2.current_x))
                             file.write('\n')
                             file.write(str(G_3.current_x))
                             file.write('\n')
                             file.write(str(G_4.current_x))
                             file.write('\n')
                             file.write(str(G_1.current_y))
                             file.write('\n')
                             file.write(str(G_2.current_y))
                             file.write('\n')
                             file.write(str(G_3.current_y))
                             file.write('\n')
                             file.write(str(G_4.current_y))
                             file.write('\n')
                             file.write(str(R_1.current_x))
                             file.write('\n')
                             file.write(str(R_2.current_x))
                             file.write('\n')
                             file.write(str(R_3.current_x))
                             file.write('\n')
                             file.write(str(R_4.current_x))
                             file.write('\n')
                             file.write(str(R_1.current_y))
                             file.write('\n')
                             file.write(str(R_2.current_y))
                             file.write('\n')
                             file.write(str(R_3.current_y))
                             file.write('\n')
                             file.write(str(R_4.current_y))
                             file.write('\n')
                             file.write(str(Y_1.current_x))
                             file.write('\n')
                             file.write(str(Y_2.current_x))
                             file.write('\n')
                             file.write(str(Y_3.current_x))
                             file.write('\n')
                             file.write(str(Y_4.current_x))
                             file.write('\n')
                             file.write(str(Y_1.current_y))
                             file.write('\n')
                             file.write(str(Y_2.current_y))
                             file.write('\n')
                             file.write(str(Y_3.current_y))
                             file.write('\n')
                             file.write(str(Y_4.current_y))
                             file.write('\n')
                             file.close()
                             pygame.quit()
                        if 400 <= mouse[0] <= 480 and 50 <= mouse[1] <= 90 :
                            file = open('save.txt','w')     
                            file.write('')
                            file.close()
                            pygame.quit()
                        if 500 <= mouse[0] <= 650 and 50 <= mouse[1] <= 90 :
                             B_1 = B_player(B_path,195,690)
                             B_2 = B_player(B_path,195,635)
                             B_3 = B_player(B_path,140,635)
                             B_4 = B_player(B_path,140,690)
                             G_1 = G_player(G_path,140,140)
                             G_2 = G_player(G_path,195,140)
                             G_3 = G_player(G_path,140,195)
                             G_4 = G_player(G_path,195,195)
                             R_1 = R_player(R_path,635,140)
                             R_2 = R_player(R_path,690,140)
                             R_3 = R_player(R_path,635,195)
                             R_4 = R_player(R_path,690,195)
                             Y_1 = Y_player(Y_path,690,690)
                             Y_2 = Y_player(Y_path,690,635)
                             Y_3 = Y_player(Y_path,635,635)
                             Y_4 = Y_player(Y_path,635,690)
                             makepath_BLUE(B_1)    #CALL FUNCTION TO MAKE PATH
                             makepath_BLUE(B_2)
                             makepath_BLUE(B_3)
                             makepath_BLUE(B_4)
                             makepath_GREEN(G_1)    #CALL FUNCTION TO MAKE PATH
                             makepath_GREEN(G_2)
                             makepath_GREEN(G_3)
                             makepath_GREEN(G_4)
                             makepath_RED(R_1)    #CALL FUNCTION TO MAKE PATH
                             makepath_RED(R_2)
                             makepath_RED(R_3)
                             makepath_RED(R_4)
                             makepath_YELLOW(Y_1)
                             makepath_YELLOW(Y_2)
                             makepath_YELLOW(Y_3)
                             makepath_YELLOW(Y_4)                           
                            
                             done = True
                            
                screen.fill((255,255,255)) 
                mouse = pygame.mouse.get_pos() 
                pygame.draw.rect(screen,color_dark,[50,50,120,40])   
                pygame.draw.rect(screen,color_dark,[200,50,170,40])
                pygame.draw.rect(screen,color_dark,[400,50,80,40])
                pygame.draw.rect(screen,color_dark,[500,50,150,40])
                screen.blit(Resume , (50,50))
                screen.blit(Save , (200,50))
                screen.blit(Quit , (400,50))
                screen.blit(New , (500,50))
                pygame.display.update() 
        result()
        if BLUE == True :
         if event.type == pygame.MOUSEBUTTONDOWN:
            label.draw(win)
            pos = pygame.mouse.get_pos()
            if 60 <= pos[0] <= 120 and 710 <= pos[1] <= 770 and Blue_Button.status == False:
                clear(Green_Button)
                clear(Red_Button)
                clear(Yellow_Button)
                n = Blue_Button.clicked()
                Blue_Button.status = True
                print("\nMoves available [Blue]=",n)
               
                if movecheck(B_1,n) or movecheck(B_2,n) or movecheck(B_3,n) or movecheck(B_4,n) :
                    BLUE = True 
                    T = 0
                else :
                  w = checkwin_green()
                  q = checkwin_red()
                  p = checkwin_yellow()
                  if w == None: 
                    BLUE = False
                    GREEN = True
                    T = 1
                    Blue_Button.status = False

                  else :
                    if q == None:  
                      BLUE = False
                      RED = True
                      T = 2
                      Blue_Button.status = False
                    else :
                        if p == None :
                           BLUE = False
                           YELLOW = True
                           T = 3
                           Blue_Button.status = False
                        
                    
                      
            if BLUE == True and B_1.win != True and Blue_Button.status == True and B_1.current_x-25<=pos[0]<=B_1.current_x+25 and B_1.current_y-25<=pos[1]<=B_1.current_y+25 and BLUE == True and movecheck(B_1,n) :
                    clear(Green_Button)
                    if movecheck(B_1,n) :
                        B_1.B_move(n)
                        k = kill(B_1)
                        clear(Blue_Button)
                        T = 1                        
                        if n < 6 and k != True:
                          w = checkwin_green()
                          q = checkwin_red()
                          p = checkwin_yellow()
                          if w == None:  
                            BLUE = False
                            GREEN = True 
                            T = 1
                          else :
                            if q == None:       
                             BLUE = False
                             RED = True
                             T = 2
                            else :
                                if p == None :
                                   BLUE = False
                                   YELLOW = True
                                   T = 3
                                   Blue_Button.status = False
                              
                        if n == 6 :
                            T = 0
                        elif k == True:
                            T = 0
                        n = 0
                    Blue_Button.status = False
                    checkwin(B_1)
                        
                        
            elif BLUE == True and B_2.win != True and Blue_Button.status == True and B_2.current_x-25<=pos[0]<=B_2.current_x+25 and B_2.current_y-25<=pos[1]<=B_2.current_y+25 and BLUE == True and movecheck(B_2,n):
                    if movecheck(B_2,n) :
                        B_2.B_move(n)
                        k = kill(B_2)
                        clear(Blue_Button)
                        
                        T = 1
                        if n < 6 and k != True:
                          w = checkwin_green()
                          q = checkwin_red()
                          p = checkwin_yellow()
                          if w == None:  
                            BLUE = False
                            GREEN = True 
                            T = 1
                          else :
                            if q == None:       
                             BLUE = False
                             RED = True
                             T = 2
                            else :
                                if p == None :
                                   BLUE = False
                                   YELLOW = True
                                   T = 3
                                   Blue_Button.status = False
                        if n == 6 :
                            T = 0
                        elif k == True :
                            T = 0
                        n = 0
                    Blue_Button.status = False
                    checkwin(B_2)
                             
            elif BLUE == True and B_3.win != True and Blue_Button.status == True and B_3.current_x-25<=pos[0]<=B_3.current_x+25 and B_3.current_y-25<=pos[1]<=B_3.current_y+25 and BLUE == True and movecheck(B_3,n):
                    if movecheck(B_3,n) :
                        B_3.B_move(n)
                        k=kill(B_3)
                        clear(Blue_Button)
                        T = 1
                        
                        if n < 6 and k != True:
                          w = checkwin_green()
                          q= checkwin_red()
                          p = checkwin_yellow()
                          if w == None:  
                            BLUE = False
                            GREEN = True 
                            T = 1
                          else :
                            if q == None:       
                             BLUE = False
                             RED = True
                             T = 2
                            else :
                                if p == None :
                                   BLUE = False
                                   YELLOW = True
                                   T = 3
                                   Blue_Button.status = False
                        if n == 6 :
                            T = 0
                        elif k == True :
                            T = 0
                        n = 0
                    Blue_Button.status = False
                    checkwin(B_3)

            elif BLUE == True and B_4.win != True and Blue_Button.status == True and B_4.current_x-25<=pos[0]<=B_4.current_x+25 and B_4.current_y-25<=pos[1]<=B_4.current_y+25 and BLUE == True and movecheck(B_4,n) :
                    if movecheck(B_4,n) :
                        B_4.B_move(n)
                        k = kill(B_4)
                        clear(Blue_Button)
                        T = 1
                        
                        if n < 6 and k != True:
                          w = checkwin_green()
                          q = checkwin_red()
                          p = checkwin_yellow()
                          if w == None:  
                            BLUE = False
                            GREEN = True 
                            T = 1
                          else :
                            if q == None:       
                             BLUE = False
                             RED = True
                             T = 2
                            else :
                                if p == None :
                                   BLUE = False
                                   YELLOW = True
                                   T = 3
                                   Blue_Button.status = False
                        if n == 6 :
                            T = 0
                        elif k == True :
                            T = 0
                        n = 0
                    Blue_Button.status = False
                    checkwin(B_4)
                        
        if GREEN == True :
      
         if event.type == pygame.MOUSEBUTTONDOWN:
                gpos = pygame.mouse.get_pos()
                if 60 <= gpos[0] <= 120 and 60 <= gpos[1] <= 120 and Green_Button.status == False:
                    clear(Blue_Button)
                    clear(Red_Button)
                    clear(Yellow_Button)
                    z = Green_Button.clicked()
                    Green_Button.status = True
                    print("\nMoves available [Green]=",z)
                    if movecheck(G_1,z) or movecheck(G_2,z) or movecheck(G_3,z) or movecheck(G_4,z) :
                         GREEN == True
                         T = 1
                        
                    else :
                      r = checkwin_blue()
                      s = checkwin_red()
                      t = checkwin_yellow()
                      if s == None :
                         RED = True
                         GREEN = False
                         T = 2
                         Green_Button.status = False    
                      else :  
                        if t == None:
                          YELLOW = True
                          GREEN = False
                          T = 3
                          Green_Button.status = False
                        else :
                            if r == None:
                                BLUE = True
                                GREEN = False
                                T = 0
                                Green_Button.status = False
                
                if GREEN == True and G_1.win != True and Green_Button.status == True and G_1.current_x-25<=gpos[0]<=G_1.current_x+25 and G_1.current_y-25<=gpos[1]<=G_1.current_y+25  and movecheck(G_1,z):
                    if movecheck(G_1,z) :
                        G_1.G_move(z)
                        k = kill(G_1)
                        clear(Green_Button)
                        T = 2       
                        if z < 6 and k != True :
                          r = checkwin_red()
                          b = checkwin_blue()
                          y = checkwin_yellow()
                          if r == None :
                            RED = True
                            GREEN = False
                            T = 2
                          else :
                             if y == None :
                                 YELLOW = True
                                 GREEN = False
                                 T = 3
                             else :
                                 if b == None :
                                     BLUE = True
                                     GREEN = False
                                     T = 0
                          
                        if z == 6 :
                            T = 1
                        elif k == True :
                            T = 1
                        z = 0    
                    Green_Button.status = False
                    checkwin(G_1)
                       
                elif GREEN == True and G_2.win != True and Green_Button.status == True and G_2.current_x-25<=gpos[0]<=G_2.current_x+25 and G_2.current_y-25<=gpos[1]<=G_2.current_y+25  and movecheck(G_2,z):
                    if movecheck(G_2,z) :
                        G_2.G_move(z)
                        k = kill(G_2)
                        clear(Green_Button)
                        T = 2       
                        if z < 6 and k != True :
                          r = checkwin_red()
                          b = checkwin_blue()
                          y = checkwin_yellow()
                          if r == None :
                            RED = True
                            GREEN = False
                            T = 2
                          else :
                             if y == None :
                                 YELLOW = True
                                 GREEN = False
                                 T = 3
                             else :
                                 if b == None :
                                     BLUE = True
                                     GREEN = False
                                     T = 0 
                        if z == 6 :
                            T = 1
                        elif k == True :
                            T = 1
                        z = 0    
                    Green_Button.status = False
                    checkwin(G_2)
                    
                elif GREEN == True and G_3.win != True and Green_Button.status == True  and G_3.current_x-25<=gpos[0]<=G_3.current_x+25 and G_3.current_y-25<=gpos[1]<=G_3.current_y+25  and movecheck(G_3,z) :
                    if movecheck(G_3,z) :
                        G_3.G_move(z)
                        k = kill(G_3)
                        clear(Green_Button)
                        T = 2       
                        if z < 6 and k != True:
                          r = checkwin_red()
                          b = checkwin_blue()
                          y = checkwin_yellow()
                          if r == None :
                            RED = True
                            GREEN = False
                            T = 2
                          else :
                             if y == None :
                                 YELLOW = True
                                 GREEN = False
                                 T = 3
                             else :
                                 if b == None :
                                     BLUE = True
                                     GREEN = False
                                     T = 0
                        if z == 6 :
                            T = 1
                        elif k == True :
                            T = 1
                        z = 0     
                    Green_Button.status = False
                    checkwin(G_3)
                    
                elif GREEN == True and G_4.win != True and Green_Button.status == True and G_4.current_x-25<=gpos[0]<=G_4.current_x+25 and G_4.current_y-25<=gpos[1]<=G_4.current_y+25  and movecheck(G_4,z):
                    if movecheck(G_4,z) :
                        G_4.G_move(z)
                        k = kill(G_4)
                        clear(Green_Button)
                        T = 2       
                        if z < 6 and k != True:
                          r = checkwin_red()
                          b = checkwin_blue()
                          y = checkwin_yellow()
                          if r == None :
                            RED = True
                            GREEN = False
                            T = 2
                          else :
                             if y == None :
                                 YELLOW = True
                                 GREEN = False
                                 T = 3
                             else :
                                 if b == None :
                                     BLUE = True
                                     GREEN = False
                                     T = 0
                        if z == 6 :
                            T = 1
                        elif k == True :
                            T = 1
                        z = 0    
                    Green_Button.status = False    
                    checkwin(G_4)


        if RED == True:
  
         if event.type == pygame.MOUSEBUTTONDOWN:
                rpos = pygame.mouse.get_pos()
                if 720 <= rpos[0] <= 775 and 60 <= rpos[1] <= 115  and Red_Button.status == False:
                    clear(Green_Button)
                    clear(Blue_Button)
                    clear(Yellow_Button)
                    f= Red_Button.clicked()
                    Red_Button.status = True
                    print("\nMoves available [Red]=",f)
                    if movecheck(R_1,f) or movecheck(R_2,f) or movecheck(R_3,f) or movecheck(R_4,f) :
                         RED = True 
                         T = 2
                    else :
                      r = checkwin_blue()
                      s = checkwin_green()
                      t = checkwin_yellow()
                      if t == None :
                         RED = False
                         YELLOW = True
                         T = 3
                         Red_Button.status = False    
                      else :  
                        if r == None:
                          BLUE = True
                          RED = False
                          T = 0
                          Red_Button.status = False
                        else :
                            if s == None :
                                GREEN = True
                                RED = False
                                T = 1
                                Red_Button.status = False
                
                    
                if RED == True and R_1.win != True and Red_Button.status == True and R_1.current_x-25<=rpos[0]<=R_1.current_x+25 and R_1.current_y-25<=rpos[1]<=R_1.current_y+25 and RED == True and movecheck(R_1,f):
                    if movecheck(R_1,f) :
                        R_1.R_move(f)
                        k= kill(R_1)
                        clear(Red_Button)
                        T = 0       
                        if f< 6 and k != True:
                          b = checkwin_blue()
                          g = checkwin_green()
                          y = checkwin_yellow()
                          if y == None :
                            RED = False
                            YELLOW = True
                            T = 3
                          else :
                             if b == None :
                                 BLUE = True
                                 RED = False
                                 T = 0
                             else :
                                 if g == None:
                                     GREEN = True
                                     RED = False
                                     T = 1
                                                               
                        if f== 6 :
                            T = 2
                        elif k == True:
                            T = 2
                        f= 0    
                    Red_Button.status = False
                    checkwin(R_1)
                       
                elif RED == True and R_2.win != True and Red_Button.status == True and R_2.current_x-25<=rpos[0]<=R_2.current_x+25 and R_2.current_y-25<=rpos[1]<=R_2.current_y+25 and RED == True and movecheck(R_2,f):
                    if movecheck(R_2,f) :
                        R_2.R_move(f)
                        k = kill(R_2)
                        clear(Red_Button)
                        T = 0       
                        if f< 6 and k != True:
                          b = checkwin_blue()
                          g = checkwin_green()
                          y = checkwin_yellow()
                          if y == None :
                            RED = False
                            YELLOW = True
                            T = 3
                          else :
                             if b == None :
                                 BLUE = True
                                 RED = False
                                 T = 0
                             else :
                                 if g == None:
                                     GREEN = True
                                     RED = False
                                     T = 1
                          
                        if f== 6 :
                            T = 2
                        elif k == True:
                            T = 2
                        f= 0    
                    Red_Button.status = False
                    checkwin(R_2)
                    
                elif RED == True and R_3.win != True and Red_Button.status == True  and R_3.current_x-25<=rpos[0]<=R_3.current_x+25 and R_3.current_y-25<=rpos[1]<=R_3.current_y+25 and RED == True and movecheck(R_3,f) :
                    if movecheck(R_3,f) :
                        R_3.R_move(f)
                        k = kill(R_3)
                        clear(Red_Button)
                        T = 0       
                        if f< 6 and k != True:
                          b = checkwin_blue()
                          g = checkwin_green()
                          y = checkwin_yellow()
                          if y == None :
                            RED = False
                            YELLOW = True
                            T = 3
                          else :
                             if b == None :
                                 BLUE = True
                                 RED = False
                                 T = 0
                             else :
                                 if g == None:
                                     GREEN = True
                                     RED = False
                                     T = 1
                          
                        if f== 6 :
                            T = 2
                        elif k == True:
                            T = 2
                        f= 0     
                    Red_Button.status = False
                    checkwin(R_3)
                    
                elif RED == True and R_4.win != True and Red_Button.status == True and R_4.current_x-25<=rpos[0]<=R_4.current_x+25 and R_4.current_y-25<=rpos[1]<=R_4.current_y+25 and RED == True and movecheck(R_4,f):
                    if movecheck(R_4,f) :
                        R_4.R_move(f)
                        k = kill(R_4)
                        clear(Red_Button)
                        T = 0       
                        if f< 6 and k != True :
                          b = checkwin_blue()
                          g = checkwin_green()
                          y = checkwin_yellow()
                          if y == None :
                            RED = False
                            YELLOW = True
                            T = 3
                          else :
                             if b == None :
                                 BLUE = True
                                 RED = False
                                 T = 0
                             else :
                                 if g == None:
                                     GREEN = True
                                     RED = False
                                     T = 1
                          
                        if f== 6 :
                            T = 2
                        elif k == True:
                            T = 2
                        f= 0    
                    Red_Button.status = False    
                    checkwin(R_4) 

        if YELLOW ==True  :
  
         if event.type == pygame.MOUSEBUTTONDOWN:
                ypos = pygame.mouse.get_pos()
                if 720 <= ypos[0] <= 775 and 720 <= ypos[1] <= 775  and Yellow_Button.status == False:
                    clear(Green_Button)
                    clear(Blue_Button)
                    clear(Red_Button)
                    u = Yellow_Button.clicked()
                    Yellow_Button.status = True
                    print("\nMoves available [Yellow]=",u)
                    if movecheck(Y_1,u) or movecheck(Y_2,u) or movecheck(Y_3,u) or movecheck(Y_4,u) :
                         YELLOW = True 
                         T = 3
                    else :
                      r = checkwin_blue()
                      s = checkwin_green()
                      t = checkwin_red()
                      if r == None :
                         YELLOW = False
                         BLUE = True
                         T = 0
                         Yellow_Button.status = False    
                      else :  
                        if s == None:
                          GREEN = True
                          YELLOW = False
                          T = 1
                          Yellow_Button.status = False
                        else :
                            if t == None :
                                RED = True
                                YELLOW = False
                                T = 2
                                Yellow_Button.status = False
                
                    
                if YELLOW ==True and Y_1.win != True and Yellow_Button.status == True and Y_1.current_x-25<=ypos[0]<=Y_1.current_x+25 and Y_1.current_y-25<=ypos[1]<=Y_1.current_y+25 and YELLOW ==True and movecheck(Y_1,u):
                    if movecheck(Y_1,u) :
                        Y_1.Y_move(u)
                        k = kill(Y_1)
                        clear(Yellow_Button)
                        T = 0       
                        if u < 6 and k != True :
                          b = checkwin_blue()
                          g = checkwin_green()
                          r = checkwin_red()
                          if b == None :
                            YELLOW = False
                            BLUE = True
                            T = 0
                          else :
                             if g == None :
                                 GREEN = True
                                 YELLOW = False
                                 T = 1
                             else :
                                 if r == None:
                                     RED = True 
                                     YELLOW = False
                                     T = 2
                                                               
                        if u== 6 :
                            T = 3
                        elif k == True:
                            T = 3
                        u = 0    
                    Yellow_Button.status = False
                    checkwin(Y_1)
                       
                elif YELLOW ==True and Y_2.win != True and Yellow_Button.status == True and Y_2.current_x-25<=ypos[0]<=Y_2.current_x+25 and Y_2.current_y-25<=ypos[1]<=Y_2.current_y+25 and YELLOW ==True and movecheck(Y_2,u):
                    if movecheck(Y_2,u) :
                        Y_2.Y_move(u)
                        k = kill(Y_2)
                        clear(Yellow_Button)
                        T = 0       
                        if u < 6 and k != True :
                          b = checkwin_blue()
                          g = checkwin_green()
                          r = checkwin_red()
                          if b == None :
                            YELLOW = False
                            BLUE = True
                            T = 0
                          else :
                             if g == None :
                                 GREEN = True
                                 YELLOW = False
                                 T = 1
                             else :
                                 if r == None:
                                     RED = True 
                                     YELLOW = False
                                     T = 2
                                                               
                        if u== 6 :
                            T = 3
                        elif k == True:
                            T = 3
                        u = 0   
                    Yellow_Button.status = False
                    checkwin(Y_2)
                    
                elif YELLOW ==True and Y_3.win != True and Yellow_Button.status == True  and Y_3.current_x-25<=ypos[0]<=Y_3.current_x+25 and Y_3.current_y-25<=ypos[1]<=Y_3.current_y+25 and YELLOW ==True and movecheck(Y_3,u) :
                    if movecheck(Y_3,u) :
                        Y_3.Y_move(u)
                        k = kill(Y_3)
                        clear(Yellow_Button)
                        T = 0       
                        if u < 6 and k != True:
                          b = checkwin_blue()
                          g = checkwin_green()
                          r = checkwin_red()
                          if b == None :
                            YELLOW = False
                            BLUE = True
                            T = 0
                          else :
                             if g == None :
                                 GREEN = True
                                 YELLOW = False
                                 T = 1
                             else :
                                 if r == None:
                                     RED = True 
                                     YELLOW = False
                                     T = 2
                                                               
                        if u== 6 :
                            T = 3
                        elif k == True:
                            T = 3
                        u = 0     
                    Yellow_Button.status = False
                    checkwin(Y_3)
                    
                elif YELLOW ==True and Y_4.win != True and Yellow_Button.status == True and Y_4.current_x-25<=ypos[0]<=Y_4.current_x+25 and Y_4.current_y-25<=ypos[1]<=Y_4.current_y+25 and YELLOW ==True and movecheck(Y_4,u):
                    if movecheck(Y_4,u) :
                        Y_4.Y_move(u)
                        k = kill(Y_4)
                        clear(Yellow_Button)
                        T = 0       
                        if u < 6 and k != True:
                          b = checkwin_blue()
                          g = checkwin_green()
                          r = checkwin_red()
                          if b == None :
                            YELLOW = False
                            BLUE = True
                            T = 0
                          else :
                             if g == None :
                                 GREEN = True
                                 YELLOW = False
                                 T = 1
                             else :
                                 if r == None:
                                     RED = True 
                                     YELLOW = False
                                     T = 2
                                                               
                        if u== 6 :
                            T = 3
                        elif k == True:
                            T = 3
                        u = 0 
                    Yellow_Button.status = False    
                    checkwin(Y_4)



                
    clock.tick(60)      
  
pygame.quit()



