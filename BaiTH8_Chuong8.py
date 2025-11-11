import tkinter as tk
from tkinter import messagebox

def chuyen_do():
    try:
        do_f = float(entry_f.get())
        do_c = (do_f - 32) * 5 / 9
        lbl_kq.config(text=f"Độ C: {do_c:.2f}")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ!")

root = tk.Tk()
root.title("Chuyển độ F sang độ C")
root.configure(bg="yellow")

tk.Label(root, text="Nhập độ F:", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
entry_f = tk.Entry(root, font=("Arial", 12), width=10)
entry_f.grid(row=0, column=1)

tk.Button(root, text="Chuyển", font=("Arial", 12, "bold"), command=chuyen_do, bg="#3498db", fg="white").grid(row=0, column=2, padx=10)

lbl_kq = tk.Label(root, text="Độ C:", bg="yellow", font=("Arial", 12, "bold"))
lbl_kq.grid(row=1, column=0, columnspan=3, pady=15)

root.mainloop()