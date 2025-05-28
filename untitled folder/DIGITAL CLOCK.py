import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time) 


root = tk.Tk()
root.title("Digital Clock")


root.geometry("300x100")
root.configure(bg="black")


clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="lime")
clock_label.pack(expand=True)


update_time()


root.mainloop()
