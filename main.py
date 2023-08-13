from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image



class Adm (ScreenManager):
    pass

class Principal (Screen):

    def marca1 (self):



         if self.ids.id1.source == "nada.png" and self.ids.label.text == "jogador1":
             self.ids.id1.source = "bola.png"
             self.ids.label.text = "jogador2"


         elif self.ids.id1.source == "nada.png" and self.ids.label.text == "jogador2":
             self.ids.id1.source = "xis.png"
             self.ids.label.text = "jogador1"



    def marca2(self):
        if self.ids.id2.source == "nada.png" and self.ids.label.text == "jogador1":
            self.ids.id2.source = "bola.png"
            self.ids.label.text = "jogador2"


        elif self.ids.id2.source == "nada.png" and self.ids.label.text == "jogador2":
            self.ids.id2.source = "xis.png"
            self.ids.label.text = "jogador1"

    def marca3(self):
        if self.ids.id3.source == "nada.png" and self.ids.label.text == "jogador1":
            self.ids.id3.source = "bola.png"
            self.ids.label.text = "jogador2"


        elif self.ids.id3.source == "nada.png" and self.ids.label.text == "jogador2":
            self.ids.id3.source = "xis.png"
            self.ids.label.text = "jogador1"

    def marca4(self):
        if self.ids.id4.source == "nada.png" and self.ids.label.text == "jogador1":
            self.ids.id4.source = "bola.png"
            self.ids.label.text = "jogador2"


        elif self.ids.id4.source == "nada.png" and self.ids.label.text == "jogador2":
            self.ids.id4.source = "xis.png"
            self.ids.label.text = "jogador1"

    def marca5(self):
        if self.ids.id5.source == "nada.png" and self.ids.label.text == "jogador1":
            self.ids.id5.source = "bola.png"
            self.ids.label.text = "jogador2"


        elif self.ids.id5.source == "nada.png" and self.ids.label.text == "jogador2":
            self.ids.id5.source = "xis.png"
            self.ids.label.text = "jogador1"

    def marca6(self):
        if self.ids.id6.source == "nada.png" and self.ids.label.text == "jogador1":
            self.ids.id6.source = "bola.png"
            self.ids.label.text = "jogador2"


        elif self.ids.id6.source == "nada.png" and self.ids.label.text == "jogador2":
            self.ids.id6.source = "xis.png"
            self.ids.label.text = "jogador1"

    def marca7(self):
        if self.ids.id7.source == "nada.png" and self.ids.label.text == "jogador1":
            self.ids.id7.source = "bola.png"
            self.ids.label.text = "jogador2"


        elif self.ids.id7.source == "nada.png" and self.ids.label.text == "jogador2":
            self.ids.id7.source = "xis.png"
            self.ids.label.text = "jogador1"

    def marca8(self):
        if self.ids.id8.source == "nada.png" and self.ids.label.text == "jogador1":
            self.ids.id8.source = "bola.png"
            self.ids.label.text = "jogador2"


        elif self.ids.id8.source == "nada.png" and self.ids.label.text == "jogador2":
            self.ids.id8.source = "xis.png"
            self.ids.label.text = "jogador1"

    def marca9(self):
        if self.ids.id9.source == "nada.png" and self.ids.label.text == "jogador1":
            self.ids.id9.source = "bola.png"
            self.ids.label.text = "jogador2"


        elif self.ids.id9.source == "nada.png" and self.ids.label.text == "jogador2":
            self.ids.id9.source = "xis.png"
            self.ids.label.text = "jogador1"


    def verifica (self):

    # condições de vitória do jogador 1

        if self.ids.id1.source == "bola.png" and self.ids.id2.source == "bola.png" and self.ids.id3.source == "bola.png":
            self.ids.label.text = "Jogador 1 ganhou!"
        if self.ids.id1.source == "bola.png" and self.ids.id4.source == "bola.png" and self.ids.id7.source == "bola.png":
            self.ids.label.text = "Jogador 1 ganhou!"
        if self.ids.id7.source == "bola.png" and self.ids.id8.source == "bola.png" and self.ids.id9.source == "bola.png":
            self.ids.label.text = "Jogador 1 ganhou!"
        if self.ids.id3.source == "bola.png" and self.ids.id6.source == "bola.png" and self.ids.id9.source == "bola.png":
            self.ids.label.text = "Jogador 1 ganhou!"
        if self.ids.id4.source == "bola.png" and self.ids.id5.source == "bola.png" and self.ids.id6.source == "bola.png":
            self.ids.label.text = "Jogador 1 ganhou!"
        if self.ids.id2.source == "bola.png" and self.ids.id5.source == "bola.png" and self.ids.id8.source == "bola.png":
            self.ids.label.text = "Jogador 1 ganhou!"
        if self.ids.id1.source == "bola.png" and self.ids.id5.source == "bola.png" and self.ids.id9.source == "bola.png":
            self.ids.label.text = "Jogador 1 ganhou!"
        if self.ids.id3.source == "bola.png" and self.ids.id5.source == "bola.png" and self.ids.id7.source == "bola.png":
            self.ids.label.text = "Jogador 1 ganhou!"

    #condiçoes de vitória do jogador 2

        if self.ids.id1.source == "xis.png" and self.ids.id2.source == "xis.png" and self.ids.id3.source == "xis.png":
            self.ids.label.text = "Jogador 2 ganhou!"
        if self.ids.id1.source == "xis.png" and self.ids.id4.source == "xis.png" and self.ids.id7.source == "xis.png":
            self.ids.label.text = "Jogador 2 ganhou!"
        if self.ids.id7.source == "xis.png" and self.ids.id8.source == "xis.png" and self.ids.id9.source == "xis.png":
            self.ids.label.text = "Jogador 2 ganhou!"
        if self.ids.id3.source == "xis.png" and self.ids.id6.source == "xis.png" and self.ids.id9.source == "xis.png":
            self.ids.label.text = "Jogador 2 ganhou!"
        if self.ids.id4.source == "xis.png" and self.ids.id5.source == "xis.png" and self.ids.id6.source == "xis.png":
            self.ids.label.text = "Jogador 2 ganhou!"
        if self.ids.id2.source == "xis.png" and self.ids.id5.source == "xis.png" and self.ids.id8.source == "xis.png":
            self.ids.label.text = "Jogador 2 ganhou!"
        if self.ids.id1.source == "xis.png" and self.ids.id5.source == "xis.png" and self.ids.id9.source == "xis.png":
            self.ids.label.text = "Jogador 2 ganhou!"
        if self.ids.id3.source == "xis.png" and self.ids.id5.source == "xis.png" and self.ids.id7.source == "xis.png":
            self.ids.label.text = "Jogador 2 ganhou!"

    def limpa (self):
        self.ids.id1.source = "nada.png"
        self.ids.id2.source = "nada.png"
        self.ids.id3.source = "nada.png"
        self.ids.id4.source = "nada.png"
        self.ids.id5.source = "nada.png"
        self.ids.id6.source = "nada.png"
        self.ids.id7.source = "nada.png"
        self.ids.id8.source = "nada.png"
        self.ids.id9.source = "nada.png"
        self.ids.label.text = "jogador1"



class MainApp (MDApp):
    def fechar(self):
        self.stop()

    def build (self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"

        return Adm()

MainApp().run()