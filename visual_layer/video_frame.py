import customtkinter as ctk
import tkinter as tk
from threading import Thread
from PIL import Image, ImageTk
import time
from typing import Callable

class VideoFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, 
                getvideoframe: Callable[[int, int], Image.Image], 
                
                    *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.get_video_frame = getvideoframe  
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack(expand=True)
        self.running = True  # Control flag for the thread
        self.thread = Thread(target=self.update_thread, daemon=True)
        self.thread.start()


    def launch(self):
        master = self.master
        master.update()
        self.width = int(master.winfo_width()//2)
        self.height = int(master.winfo_height()//2)
        


    def update_thread(self):
        while self.running:
            self.launch()
            image: Image.Image = self.get_video_frame(
                self.width, self.height
            )  # Get the next frame
            if image:
                tk_image = ImageTk.PhotoImage(image)
                self.image_label.configure(image=tk_image)
                self.image_label.image = tk_image
            time.sleep(0.03)

    def stop(self):
        """Stop the video playback."""
        self.running = False
        self.thread.join()

    def go_grid(self, *, row, column, columnspan=None, rowspan=None):
        self.grid(row=row, column=column,
                  columnspan=columnspan,
                  rowspan=rowspan, sticky="nsew",
                  padx=10, pady=5)
