#?dijital saay uygulaması
import tkinter as tk
import time
form = tk.Tk()#form oluşturmak için
form.title("saat uygulaması")
form.geometry("250x250")
form.config(bg="pink")

def zaman():
    zaman_format = time.strftime("%H:%M:%S")
    zmn_label.config(text=zaman_format)
    zmn_label.after(200,zaman)


zmn_label = tk. Label(bg="white",font="times 35 bold")
zmn_label.place(x=30,y=80)
zaman()


baslık = tk.Label(text="dijital saat uygulaması ",fg="black",font="times 15 bold",bg="pink").pack()


form.mainloop()