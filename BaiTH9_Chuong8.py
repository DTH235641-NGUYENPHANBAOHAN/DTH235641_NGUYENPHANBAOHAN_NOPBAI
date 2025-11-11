import tkinter as tk
from tkinter import messagebox

def tinh_bmi():
    try:
        chieu_cao = float(entry_chieu_cao.get())
        can_nang = float(entry_can_nang.get())
        if chieu_cao <= 0 or can_nang <= 0:
            raise ValueError
        
        bmi = can_nang / (chieu_cao ** 2)
        lbl_bmi_kq.config(text=f"{bmi:.2f}")

        if bmi < 18.5:
            tinh_trang = "Gầy"
            nguy_co = "Thấp"
        elif 18.5 <= bmi < 25:
            tinh_trang = "Bình thường"
            nguy_co = "Trung bình"
        elif 25 <= bmi < 30:
            tinh_trang = "Hơi béo"
            nguy_co = "Cao"
        else:
            tinh_trang = "Béo phì"
            nguy_co = "Rất cao"

        lbl_tinh_trang.config(text=tinh_trang)
        lbl_nguy_co.config(text=nguy_co)

    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số hợp lệ!")

def thoat():
    root.destroy()

root = tk.Tk()
root.title("Phần mềm tính BMI")
root.configure(bg="yellow")

tk.Label(root, text="Nhập chiều cao (m):", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_chieu_cao = tk.Entry(root, width=10, font=("Arial", 12))
entry_chieu_cao.grid(row=0, column=1, pady=5)

tk.Label(root, text="Nhập cân nặng (kg):", bg="yellow", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_can_nang = tk.Entry(root, width=10, font=("Arial", 12))
entry_can_nang.grid(row=1, column=1, pady=5)

tk.Button(root, text="Tính BMI", font=("Arial", 12, "bold"), bg="#3498db", fg="white", command=tinh_bmi).grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="BMI của bạn:", bg="yellow", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
lbl_bmi_kq = tk.Label(root, text="x", bg="yellow", font=("Arial", 12, "bold"))
lbl_bmi_kq.grid(row=3, column=1, pady=5)

tk.Label(root, text="Tình trạng của bạn:", bg="yellow", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="e")
lbl_tinh_trang = tk.Label(root, text="", bg="yellow", font=("Arial", 12, "bold"))
lbl_tinh_trang.grid(row=4, column=1, pady=5)

tk.Label(root, text="Nguy cơ phát triển bệnh:", bg="yellow", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=5, sticky="e")
lbl_nguy_co = tk.Label(root, text="", bg="yellow", font=("Arial", 12, "bold"))
lbl_nguy_co.grid(row=5, column=1, pady=5)

tk.Button(root, text="Thoát", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", command=thoat).grid(row=6, column=0, columnspan=2, pady=15)

root.mainloop()