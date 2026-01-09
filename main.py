import customtkinter as ctk
import matplotlib as mpl
import pandas as pd
import numpy as np
import MoreCustomTkinterWidgets as mw

ctk.set_appearance_mode("dark")

fullMon = pd.read_csv('data/Lists/pokemon.csv')
monNames = fullMon['Name'].tolist()

class MainFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class SearchFrame(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class PokemonButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ZDex")
        self.geometry("1000x720")
        self.resizable(False, False)
        self.iconbitmap('data/Images/GreatBall.ico')

        self.Search = SearchFrame(
            master=self,
            width=215,
            height=30,
            placeholder_text= "Search...",
        )

        self.Search.grid(
            row=0,
            column=0,
            padx=20,
            pady=20
        )

        self.pokemonList = MainFrame(
            master=self,
            width=350,
            height=600,
        )

        self.pokemonList.grid(
            row=1,
            column=0,
            padx = 20,
            pady = 10
        )

        count = -1

        for Name in monNames:

            count += 1

            self.temp = PokemonButton(
                master=self.pokemonList,
                fg_color= "#1f1f1f",
                width=335,
                height=30,
                text=Name,
            )

            self.temp.grid(
                row=count,
                column=0,
                padx=5,
                pady=2
            )

            self.temp.widgetName = Name

    def onPokemonSelected(self, event):
        self.pokemonList.grid()

app = App()
app.mainloop()