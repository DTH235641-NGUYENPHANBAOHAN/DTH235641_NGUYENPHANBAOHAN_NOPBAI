import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("frame 2")

frame = ttk.LabelFrame(root, text="frame 2", padding=10)
frame.pack(padx=10, pady=10)

reliefs = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

for bw in range(5):
    lbl = ttk.Label(frame, text=f"borderwidth = {bw}")
    lbl.grid(row=bw, column=0, padx=5, pady=5, sticky="w")
    
    for col, relief in enumerate(reliefs):
        btn = tk.Button(
            frame,
            text=relief,
            borderwidth=bw,
            relief=relief,
            width=8
        )
        btn.grid(row=bw, column=col + 1, padx=5, pady=5)

root.mainloop()