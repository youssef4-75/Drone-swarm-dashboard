
import customtkinter as ctk
from om import OM
# from function_block import btn


def btn():...





def main():
    # Initialize the root window
    root = ctk.CTk()
    root.title("Sending to...")
    root.geometry("800x200")

    

    # Create the body frame
    body = ctk.CTkFrame(root)
    body.pack(fill="both", expand=True, padx=10, pady=5)

    # Divide the body into parts

    # Ip input part
    ip_frame = ctk.CTkTextbox(body, height=1)
    ip_frame.grid(row=0, column=0, columnspan=20, rowspan=2, padx=20)


    # Drone information part
    info_frame = OM(master=body, title="Resolution", values=[
        #here you put possible values for this resolution ...
    ])
    info_frame.grid(row=0, column=2, rowspan=2, padx=10, columnspan=2)


    button = ctk.CTkButton(root, command=btn)
    button.pack(fill="x", expand=False, padx=10, pady=5, side=ctk.BOTTOM)


    # Configure grid layout for the body
    body.rowconfigure([0, 1, 2], weight=1)
    body.columnconfigure([0, 1, 2], weight=1)

    # Run the main loop
    root.mainloop()

main()