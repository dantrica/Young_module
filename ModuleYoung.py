
# coding: utf-8

# In[1]:



"""
@author: J C Acevedo1, J G Trejos1, D M Celis1, J R Herrera1, K L Cristiano1 and D A Triana
"""

from Tkinter import *
from PIL import Image, ImageTk

# coding: utf-8

class Samples:
    def __init__(self, material, posX, posY, SpriteType):
        #Lista de propiedades
        self.posX = posX
        self.posY = posY
        self.material = material
        self.SpriteType = SpriteType
        
    def SpriteLoad(self, Nsprites):
        self.SpriteList =[]
        for i in range(Nsprites):
            self.SpriteList.append(
                    ImageTk.PhotoImage(Image.open("Sprites/" +
                                                  self.material + "AndMachine"
                                                  + self.SpriteType
                                                  + str(i) + ".png")))
        return self.SpriteList
    
    def SpriteLoadInitial(self):
        self.sprite = ImageTk.PhotoImage(Image.open("Sprites/" +
                                                  self.material
                                                  + self.SpriteType
                                                  + ".png"))    
        return self.sprite
    
    def Results(self):
        self.results = ImageTk.PhotoImage(Image.open("Sprites/" +
                                                  self.material + "G"
                                                  + self.SpriteType
                                                  + ".png"))          
        return self.results
        


class MainWindow():
    def __init__(self):
        self.window = Tk()
        self.window.title("Young Module")
        self.window.iconbitmap("Sprites/Icon.ico")
        
        background = ImageTk.PhotoImage(Image.open("Sprites/Background.png"))
        self.width, self.height = 1250, 597
        self.canvas = Canvas(self.window, width = self.width, height = self.height)
        self.canvas.create_image(self.width/2, self.height/2, image = background, 
                                 tags= "Background")
        
        self.main()
    
    def main(self):

        # Poner ícono en la aplicación
        self.MachineCoordinates = [600 , 299]
        self.MachineCoordinates1 = [600 , 370]
        
        self.ResultsCoordinates = [1081, 345]

        

        self.NSprites = 8
        self.NSpritesAcople = 12
        self.SpriteHeight = 71
        self.SpriteWidth = 125
        self.buttonCCoordinates = [832, 300]
        self.buttonTCoordinates = [832, 400]
        self.buttonHelpCoordinates = [50, 50]
        self.buttonResetCoordinates = [1080, 520]
        

        self.spriteCoordinates = [71, 380]
        self.Space = 130
        self.Chosen = False
        self.FixedOnMachine = False
        self.secondClick = False
        
        
        self.buttonCOver = ImageTk.PhotoImage(Image.open("Sprites/YellowButtonC.png"))
        self.buttonCReady = ImageTk.PhotoImage(Image.open("Sprites/GreenButtonC.png"))
        self.buttonCStoped = ImageTk.PhotoImage(Image.open("Sprites/RedButtonC.png"))
        self.buttonTOver = ImageTk.PhotoImage(Image.open("Sprites/YellowButtonT.png"))
        self.buttonTReady = ImageTk.PhotoImage(Image.open("Sprites/GreenButtonT.png"))
        self.buttonTStoped = ImageTk.PhotoImage(Image.open("Sprites/RedButtonT.png"))
        
        self.machine = ImageTk.PhotoImage(Image.open("Sprites/Machine.png"))
        
#        self.SpriteList =[]
#        for i in range(self.NSprites):
#            self.SpriteList.append(ImageTk.PhotoImage(Image.open("Resources/Sprite" + str(i) + ".png")))
#%% Fondo y Máquina
        self.machine = ImageTk.PhotoImage(Image.open("Sprites/Machine.png"))


        self.canvas.create_image(self.MachineCoordinates, image = self.machine, tags= "Machine")

#%% Botones iniciales para Compresión y tensión.
        self.canvas.create_image(self.buttonCCoordinates, image = self.buttonCReady, tags= "ButtonCReady")
        self.canvas.create_image(self.buttonTCoordinates, image = self.buttonTReady, tags= "ButtonTReady")

#%% Binding Botones para Compresión y tensión.
        self.canvas.tag_bind("ButtonCReady", '<Enter>', self.OverCButton)
        self.canvas.tag_bind("ButtonTReady", '<Enter>', self.OverTButton)
        self.canvas.tag_bind("ButtonCLeave", '<Leave>', self.LeaveCButton)
        self.canvas.tag_bind("ButtonTLeave", '<Leave>', self.LeaveTButton)
        self.canvas.tag_bind("ButtonCLeave", '<Button-1>', self.ClickCButton)
        self.canvas.tag_bind("ButtonTLeave", '<Button-1>', self.ClickTButton)
        
#%% Botón Ayuda
        self.buttonHelp = ImageTk.PhotoImage(Image.open("Sprites/HelpButtonOn-Off.png"))
        self.buttonHelpOver = ImageTk.PhotoImage(Image.open("Sprites/HelpButtonSelect.png"))
        self.dialogHelp = ImageTk.PhotoImage(Image.open("Sprites/Helptext.png"))
        
        self.canvas.create_image(self.buttonHelpCoordinates, image = self.buttonHelp, tags= "ButtonHelp")

        self.canvas.tag_bind("ButtonHelp", '<Enter>', self.OverHelpButton)
        self.canvas.tag_bind("ButtonHelpLeave", '<Leave>', self.LeaveHelpButton)
        self.canvas.tag_bind("ButtonHelpLeave", '<Button-1>', self.ClickHelpButton)
        self.canvas.tag_bind("DialogHelp", '<Button-1>', self.CloseHelp)

#%% Botón Reset
        
        self.buttonReset = ImageTk.PhotoImage(Image.open("Sprites/ResetButton.png"))
        self.buttonResetOver = ImageTk.PhotoImage(Image.open("Sprites/ResetButtonPress.png"))
        
        self.canvas.create_image(self.buttonResetCoordinates, image = self.buttonReset, tags= "ButtonReset")

        self.canvas.tag_bind("ButtonReset", '<Enter>', self.OverResetButton)
        self.canvas.tag_bind("ButtonResetLeave", '<Leave>', self.LeaveResetButton)
        self.canvas.tag_bind("ButtonResetLeave", '<Button-1>', self.ClickResetButton)

#%% Definición Materiales
        
        self.Materials = [ "Aluminio", "Bronce", "Acero"]
        self.indice = len(self.Materials) + 1 #Este se coloca fuera del rango.
        # Reset lo anterior
        
        for i in range(len(self.Materials)):
            self.canvas.delete("Sprite" + str(i), "Results")
            
        self.canvas.pack()
        
        self.window.mainloop()

#%% Botón Reset

    def OverResetButton(self, event):
        self.canvas.delete("ButtonReset")
        self.canvas.create_image(self.buttonResetCoordinates, image = self.buttonResetOver, tags= "ButtonResetLeave")

    def LeaveResetButton(self, event):
        self.canvas.delete("ButtonResetLeave")
        self.canvas.create_image(self.buttonResetCoordinates, image = self.buttonReset, tags= "ButtonReset")
        
    def ClickResetButton(self, event):
        self.canvas.delete("Machine")
        self.main()

#%% Botón Ayuda
        
    def OverHelpButton(self, event):
        self.canvas.delete("ButtonHelp")
        self.canvas.create_image(self.buttonHelpCoordinates, image = self.buttonHelpOver, tags= "ButtonHelpLeave")

    def LeaveHelpButton(self, event):
        self.canvas.delete("ButtonHelpLeave")
        self.canvas.create_image(self.buttonHelpCoordinates, image = self.buttonHelp, tags= "ButtonHelp")
        
    def ClickHelpButton(self, event):
        self.canvas.create_image(self.width/2, self.height/2, image = self.dialogHelp, tags= "DialogHelp")
        
    def CloseHelp(self, event):
        self.canvas.delete("DialogHelp")
        
                
#%% Botones Compresión y Tensión

    def OverCButton(self, event):
        self.canvas.delete("ButtonCReady")
        self.canvas.create_image(self.buttonCCoordinates, image = self.buttonCOver, tags= "ButtonCLeave")

    def OverTButton(self, event):
        self.canvas.delete("ButtonTReady")
        self.canvas.create_image(self.buttonTCoordinates, image = self.buttonTOver, tags= "ButtonTLeave")
        
    def LeaveCButton(self, event):
        self.canvas.delete("ButtonCLeave")
        self.canvas.create_image(self.buttonCCoordinates, image = self.buttonCReady, tags= "ButtonCReady")

    def LeaveTButton(self, event):
        self.canvas.delete("ButtonTLeave")
        self.canvas.create_image(self.buttonTCoordinates, image = self.buttonTReady, tags= "ButtonTReady")

    def ClickCButton(self, event):
        if self.secondClick == True and self.Chosen == True:
            self.canvas.delete("ButtonCReady", "ButtonCLeave")
            self.canvas.create_image(self.buttonCCoordinates, image = self.buttonCStoped, tags= "ButtonCStoped")
            self.AnimateSprite()
            return
        
        self.canvas.delete("ButtonCLeave", "ButtonTLeave")
        self.canvas.create_image(self.buttonCCoordinates, image = self.buttonCReady, tags= "ButtonCReady")
        self.canvas.create_image(self.buttonTCoordinates, image = self.buttonTStoped, tags= "ButtonTStoped")
        self.SpriteType = "C"
        self.AnimateLoading() #Sólo de Tracción a Compresión.
        self.CreateSamples()
        self.secondClick = True
    
    def ClickTButton(self, event):
        if self.secondClick == True and self.Chosen == True:
            self.canvas.delete("ButtonTReady", "ButtonTLeave")
            self.canvas.create_image(self.buttonTCoordinates, image = self.buttonTStoped, tags= "ButtonTStoped")
            self.AnimateSprite()
            return
        
        self.canvas.create_image(self.buttonCCoordinates, image = self.buttonCStoped, tags= "ButtonCStoped")
        self.canvas.create_image(self.buttonTCoordinates, image = self.buttonTReady, tags= "ButtonTReady")
        self.SpriteType = "T"
#        self.AnimateLoading() #Ya se encuentra en posición de Tracción.

        self.CreateSamples()
        self.secondClick = True

#%% Crear la lista de Muestras (3)

    def CreateSamplesList(self):
        self.SamplesList = []

        for i in range(len(self.Materials)):
            self.SamplesList.append(Samples(self.Materials[i], 
                                    self.spriteCoordinates[0] + self.Space * i, 
                                    self.spriteCoordinates[1], self.SpriteType))

#%% Binding para poder mover el mouse
    def BindSamples(self):
        for i in range(len(self.Materials)):
            self.canvas.tag_bind("Sprite" + str(i), '<B1-Motion>', self.Move)
            self.canvas.tag_bind("Sprite" + str(i), '<Button-1>', self.SetMouse)
            self.canvas.tag_bind("Sprite" + str(i), '<ButtonRelease-1>', self.SetExperiment)
            
    def CreateSamples(self):
        self.CreateSamplesList()
        
        for i in range(len(self.SamplesList)):
            self.canvas.delete("Sprite" + str(i))
            if self.indice == i and self.Chosen == True:
                continue
            self.canvas.create_image(self.SamplesList[i].posX, self.SamplesList[i].posY,
                                     image = self.SamplesList[i].SpriteLoadInitial(), 
                                     tags= "Sprite" + str(i))
        self.BindSamples()
    
    def AnimateLoading(self):
        for i in range(self.NSpritesAcople):
            self.canvas.delete("Machine")
            
            self.SpriteAcople = ImageTk.PhotoImage(Image.open("Sprites/MachineAcople"
                                                             + str(i) + ".png" ))
            
            self.canvas.create_image(self.MachineCoordinates,
                                         image = self.SpriteAcople, 
                                         tags= "Machine")
            
            self.canvas.after(200)
            self.canvas.update()
        pass

    def SetMouse(self, event):
        self.xSetMouse = event.x
        self.ySetMouse = event.y

    def Move(self, event):
        for i in range(len(self.SamplesList)):
            if abs(event.x -  self.SamplesList[i].posX) < self.SpriteWidth and self.Chosen == False and self.FixedOnMachine == False:
                self.Chosen = True
                self.indice = i  
            if self.Chosen == True:
                self.canvas.move("Sprite" + str(self.indice), event.x - self.xSetMouse,
                                 event.y - self.ySetMouse)
                self.xSetMouse = event.x
                self.ySetMouse = event.y

    def SetExperiment(self, event):
        if abs(self.xSetMouse - self.MachineCoordinates[0]) < 100  and         abs (self.ySetMouse - self.MachineCoordinates[1] - 70) < 100 and         self.FixedOnMachine == False:
            
            self.canvas.delete("Machine")
            self.CreateSamples()
            self.canvas.create_image(self.MachineCoordinates, image = self.SamplesList[self.indice].SpriteLoad(self.NSprites)[0], tags= "Machine")
            
            self.FixedOnMachine = True

        if self.FixedOnMachine == False:
            self.Chosen = False
            self.CreateSamples()

    def AnimateSprite(self):
        spritelist = self.SamplesList[self.indice].SpriteLoad(self.NSprites)
        
        ResultsLoading = ImageTk.PhotoImage(Image.open("Sprites/Loading.png"))
        
        self.canvas.create_image(self.ResultsCoordinates, image = ResultsLoading, tags= "Results")
        for i in range(self.NSprites):
            self.canvas.delete("Machine")
            self.canvas.create_image(self.MachineCoordinates, image = spritelist[i], tags= "Machine")
            self.canvas.after(700)
            self.canvas.update()
        
        ResultsImage = self.SamplesList[self.indice].Results()
        self.canvas.create_image(self.ResultsCoordinates, image = ResultsImage, tags= "Results")

        
MainWindow()

