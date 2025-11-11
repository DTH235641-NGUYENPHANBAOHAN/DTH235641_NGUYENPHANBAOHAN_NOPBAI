import tkinter as tk
from tkinter import messagebox

def change_password():
    old_pass = entry_old.get()
    new_pass = entry_new.get()
    confirm_pass = entry_confirm.get()

    if not old_pass or not new_pass or not confirm_pass:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
        return

    if old_pass != "1234":
        messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng!")
        return

    if new_pass != confirm_pass:
        messagebox.showerror("Lỗi", "Mật khẩu mới không trùng khớp!")
        return

    messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")
    entry_old.delete(0, tk.END)
    entry_new.delete(0, tk.END)
    entry_confirm.delete(0, tk.END)

def cancel():
    root.destroy()

root = tk.Tk()
root.title("Enter New Password")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="Old Password:", font=('Arial', 11)).place(x=20, y=30)
tk.Label(root, text="New Password:", font=('Arial', 11)).place(x=20, y=65)
tk.Label(root, text="Enter New Password Again:", font=('Arial', 11)).place(x=20, y=100)

entry_old = tk.Entry(root, show='*', width=25)
entry_old.place(x=200, y=30)

entry_new = tk.Entry(root, show='*', width=25)
entry_new.place(x=200, y=65)

entry_confirm = tk.Entry(root, show='*', width=25)
entry_confirm.place(x=200, y=100)

tk.Button(root, text="OK", width=10, command=change_password).place(x=90, y=140)
tk.Button(root, text="Cancel", width=10, command=cancel).place(x=190, y=140)

root.mainloop()