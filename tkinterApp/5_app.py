import tkinter as tk

#init
window = tk.Tk()
window.title("My App") # title of the app
window.geometry("400x300") #initial size of window
window.resizable(True, True) # set as resizable
window.config(background="gray") # change background color name / hex value

def print_entry():
    data = username.get()
    var.set(data)
    print(data)

tk.Label(window, text="Username").grid(row=0, column=0) 
username = tk.Entry(window)
username.grid(row=0, column=1)
var = tk.StringVar()
label1 = tk.Label(window , textvariable=var).grid(row=3, column=3)
var.set("yes")

tk.Button(window, text="Login", command=print_entry).grid(row=1, column=0, columnspan=2)




window.mainloop()