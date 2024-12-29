import customtkinter as ctk

from functional_layer import func1, func2, func3, getvideo
from .header import Header
from .body import Body
from .video_frame import VideoFrame


def main():
    # Initialize the root window
    root = ctk.CTk()
    root.title("Drone Swarm Dashboard")
    root.geometry("800x600")

    # Create the header frame
    header = Header(root, height=50, corner_radius=0)
    header.pack(fill="x", padx=10, pady=5)

    # Create the body frame
    body = ctk.CTkFrame(root)
    body.pack(fill="both", expand=True, padx=10, pady=5)

    # Divide the body into parts
    # Video part
    video_frame = VideoFrame(body, getvideo)
    video_frame.grid(row=0, column=0, columnspan=2, rowspan=2)


    # Drone information part
    info_frame = Body(body, text="Battery: 75%\nStatus: Active")
    info_frame.go_grid(row=0, column=2, rowspan=2)


    # External data part
    external_frame = Body(body, text="External Data: Placeholder")
    external_frame.go_grid(row=2, column=0, columnspan=2)


    # Control data part
    control_frame = Body(body, text="Control Data: Placeholder")
    control_frame.go_grid(row=2, column=2)


    # Configure grid layout for the body
    body.rowconfigure([0, 1, 2], weight=1)
    body.columnconfigure([0, 1, 2], weight=1)

    # Run the main loop
    # video_frame.launch()
    root.mainloop()


if __name__ == "__main__":
    main()