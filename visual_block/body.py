import customtkinter as ctk
import tkinter as tk
from typing import Iterable


class Body(ctk.CTkFrame):
    def __init__(self,
                master,
                text,
                data=None,
                width = 200,
                height = 200,
                corner_radius = None,
                border_width = None,
                bg_color = "transparent",
                fg_color = None,
                border_color = None, 
                background_corner_colors = None, 
                overwrite_preferred_drawing_method = None,
                **kwargs):
        super().__init__(master, width, height, corner_radius,
            border_width, bg_color, fg_color, border_color, 
            background_corner_colors, overwrite_preferred_drawing_method,
            
            **kwargs)


        self.text = text
        text_ = ""
        if data is None: data = {}
        if not isinstance(data, dict): raise Exception("data must be a dict")
        for key, value in data.items():
            text_ += f"\n{key}: {value}"
        self.info_label = ctk.CTkLabel(self, text=text + text_)
        self.info_label.pack(expand=True)

    def update_data(self, data=None):
        if data is None: data = {}
        if not isinstance(data, dict): raise Exception("data must be a dict")
        text_ = ""
        for key, value in data.items():
            text_ += f"\n{key}: {value}"
        self.info_label.configure(text=self.text + text_)

        
    def go_grid(self, *, row, column, columnspan=None, rowspan=None):
        self.grid(row=row, column=column,
                  columnspan=columnspan,
                  rowspan=rowspan, sticky="nsew",
                  padx=10, pady=5)