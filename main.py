import matplotlib as mpl
import pandas as pd
import numpy as np
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="ZDex", width=1280, height=720)
dpg.set_viewport_min_width(854)
dpg.set_viewport_min_height(480)
dpg.set_viewport_large_icon('data/Images/GreatBall.ico')

with dpg.window(label="Welcome"):
    dpg.add_text("Welcome to ZDex!")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

