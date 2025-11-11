import tkinter as tk
from tkinter import messagebox

can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

def chuyen_nam():
    try:
        nam_duong = int(entry_nam.get())
        nam_am = can[(nam_duong + 6) % 10] + " " + chi[(nam_duong + 8) % 12]
        lbl_kq.config(text="Năm âm: " + nam_am)
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập năm hợp lệ!")

root = tk.Tk()
root.title("Chuyển năm Dương Lịch sang Âm Lịch")
root.configure(bg="yellow")

tk.Label(root, text="Nhập năm dương:", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
entry_nam = tk.Entry(root, font=("Arial", 12), width=10)
entry_nam.grid(row=0, column=1)

tk.Button(root, text="Chuyển", font=("Arial", 12, "bold"), command=chuyen_nam, bg="#3498db", fg="white").grid(row=0, column=2, padx=10)

lbl_kq = tk.Label(root, text="Năm âm: ", bg="yellow", font=("Arial", 12, "bold"))
lbl_kq.grid(row=1, column=0, columnspan=3, pady=15)

root.mainloop()