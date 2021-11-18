
from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class TicTacToe(App):

    def build(self):

        self.username = "player-1"
        self.MySymbol = "X"

        self.configuration()
        self.contenedor()

        return self.boxLayout

    def configuration(self):
        Window.size = (500, 500)
        self.title = "Mi primer Juego en Linea - {}".format(self.username)

        # iniciamos el juego
        self.players = [ "X", "O" ]
        self.buttons = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

        self.isMyTurn = False
        self.existOpponent = False
        self.opponent = 'Sin Oponente :('

    def contenedor(self):
        self.boxLayout = BoxLayout(orientation='vertical', spacing=10)
        self.mibtn = Button(text='Iniciar / Reiniciar', size_hint_y= None)
        self.mibtn.background_color="grey"
        self.mibtn.bind(on_press= self.emitTurn)

        # Oponente
        self.boxLayoutOpponent = BoxLayout(orientation='horizontal', size_hint_y= None, height=30)
        self.lblPlayer = Label(text=self.username)
        self.lblOpponent = Label(text=self.opponent)
        self.boxLayoutOpponent.add_widget(self.lblPlayer)
        self.boxLayoutOpponent.add_widget(Label(text='VS'))
        self.boxLayoutOpponent.add_widget(self.lblOpponent)

        # Turno de
        self.lblTurnoDe = Label(text='', size_hint_y= None, height=15)

        # GridLayout
        self.gridLayout = GridLayout(cols=3)
        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(text='')
                self.buttons[row][column].bind(on_press= lambda button=self, row=row, column=column: self.pre_nex_turn(button=button, column=column, row=row))
                self.gridLayout.add_widget(self.buttons[row][column])
        

        self.boxLayout.add_widget(self.mibtn)
        self.boxLayout.add_widget(self.lblTurnoDe)
        self.boxLayout.add_widget(self.boxLayoutOpponent)
        self.boxLayout.add_widget(self.gridLayout)

    def pre_nex_turn(self, button, row, column):
        self.nex_turn(row, column, self.MySymbol)

    def emitTurn(self, button):
        self.new_game()


    def nex_turn(self, row, column, simbolo):
        if self.isMyTurn == False:
            self.isMyTurn = True
        else:
            self.lblTurnoDe.text= "Es el Turno de {}".format(self.opponent)
            
        print("{},{}".format(row, column))
        print('player->{}'.format(simbolo))
        if self.buttons[row][column].text == "" and self.check_winner() is False:
            self.buttons[row][column].text = simbolo
        else:
            self.buttons[row][column].text = simbolo
            if self.check_winner() is False:
                pass
            elif self.check_winner() == "Empate":
                self.lblTurnoDe = "Empate"

        self.check_winner()

    def check_winner(self):
        # Valida en columnas
        for row in range(3):
            if self.buttons[row][0].text == self.buttons[row][1].text == self.buttons[row][2].text != "":
                print("row->{}, column->{}".format(row,0))
                self.buttons[row][0].background_color="lime"
                self.buttons[row][1].background_color="lime"
                self.buttons[row][2].background_color="lime"
                return True

        # Valida en filas
        for column in range(3):
            if self.buttons[0][column].text == self.buttons[1][column].text == self.buttons[2][column].text != "":
                self.buttons[0][column].background_color="lime"
                self.buttons[1][column].background_color="lime"
                self.buttons[2][column].background_color="lime"
                return True

        # Valida diagonal de 0 a N
        if self.buttons[0][0].text == self.buttons[1][1].text == self.buttons[2][2].text != "":
            self.buttons[0][0].background_color="lime"
            self.buttons[1][1].background_color="lime"
            self.buttons[2][2].background_color="lime"
            return True

        # Valida diagonal de N a 0
        elif self.buttons[0][2].text == self.buttons[1][1].text == self.buttons[2][0].text != "":
            self.buttons[0][2].background_color="lime"
            self.buttons[1][1].background_color="lime"
            self.buttons[2][0].background_color="lime"
            return True
        elif self.empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    if self.buttons[row][column].text != "":
                        self.buttons[row][column].background_color="yellow"
            return "Empate"
        else:
            return False

    def empty_spaces(self):
        spaces = 9
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column].text != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def new_game(self):
        print("Inicia nuevamente")

        for row in range(3):
            for column in range(3):
                if self.buttons[row][column].text != "":
                    self.buttons[row][column].text = ""
                    self.buttons[row][column].background_color=1,1,1,1

    def ganador(self):
        pass

if __name__ == '__main__':
    app = TicTacToe().run()