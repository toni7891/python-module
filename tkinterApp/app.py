import tkinter as tk

root = tk.Tk() # initiate window
root.title("My App") # title of the app
root.geometry("400x300") #initial size of window
root.resizable(True, True) # set as resizable
root.config(background="black") # change background color name / hex value

#set icon for the app
icon = PhotoImage(file='logo.png')
root.iconphoto(True, icon)

#label
label = tk.Label(root , text="welcome to devops course")
label.pack()

label1 = tk.Label(root, text="Hello!")
label1.pack()

label2 = tk.Label(root, text="Tony", fg="blue")
label2.pack()

# # Label — display text
# tk.Label(root, text="Hello")
# # Button — clickable
# tk.Button(root, text="Click", command=fn)
# # Entry — single-line input
# tk.Entry(root)
# # Text — multi-line input
# tk.Text(root, height=5)
# # Checkbutton / Radiobutton
# tk.Checkbutton(root, text="Option")

# label = tk.Label(
#     root,
#     text="Styled",
#     fg="white", # text color
#     bg="#333", # background
#     font=("Arial", 14, "bold"),
#     pad x=10,
#     pad y=5,
#     relief="raised", # border style
#     width=20
# )

# # Side options
# widget.pack(side="left")
# widget.pack(side="right")
# widget.pack(side="top")
# widget.pack(side="bottom")
# # Fill and expand
# widget.pack(fill="x", expand=True)
# widget.pack(fill="both", expand=1)
# # Padding
# widget.pack(pad x=10, pad y=5)


# # reading user input
# entry = tk.Entry(root)
# entry.pack()

# def get_value():
#     value = entry.get()
#     print(value)

# btn = tk.Button(
#     root,
#     text="Submit",
#     command=get_value
# )

# btn.pack()
# # Set default value
# entry.insert(0, "default text")
# # Clear the field
# entry.delete(0, tk.END)

root.mainloop() # displays window, listen for events
