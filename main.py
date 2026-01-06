import matplotlib as mpl
import pandas as pd
import numpy as np
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="ZDex", width=1280, height=720)
dpg.set_viewport_min_width(1280)
dpg.set_viewport_min_height(720)
dpg.set_viewport_max_width(1280)
dpg.set_viewport_max_height(720)
dpg.set_viewport_large_icon('data/Images/GreatBall.ico')

fullMon = pd.read_csv('data/Lists/pokemon.csv')
monNames = fullMon['Name'].tolist()

print(monNames)

with dpg.window(tag= "Welcome", label="Welcome", height = int(dpg.get_viewport_height()), width = int(dpg.get_viewport_width())):
    dpg.add_text("Welcome to ZDex!")
    dpg.add_text("All Pokemon", indent = int(dpg.get_viewport_width()/2))
    dpg.add_listbox(label = "AllPokemon", items = monNames, width = int(dpg.get_viewport_width()/2), num_items = 35, indent = int(dpg.get_viewport_width()/2))
    dpg.set_primary_window("Welcome", True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()