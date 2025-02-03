import customtkinter as ctk

from function_block import func1, func2, func3

class Header(ctk.CTkFrame):

    def __init__(self,
                master,
                name_and_functions_list = None,
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

        if name_and_functions_list is None: name_and_functions_list = [
            ("Function 1", func1),
            ("Function 2", func2),
            ("Function 3", func3),
        ]


        for name, funct in name_and_functions_list:
            ctk.CTkButton(self, text=name, command=funct).pack(
                side="left",
                padx=10,
                pady=5
            )