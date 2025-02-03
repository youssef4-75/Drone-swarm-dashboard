import customtkinter as ctk

class OM(ctk.CTkFrame):
    def __init__(self, title, values, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.values = values
        self.var = ctk.IntVar()
        ctk.CTkOptionMenu(self, variable=self.var, values=[k for k in values]).pack(side=ctk.RIGHT)
        ctk.CTkLabel(self, text=self.title).pack(side=ctk.LEFT, padx=4)




