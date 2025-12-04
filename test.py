import tkinter as tk

def show_text():
    label.config(text="Hello! This text appeared after clicking the button.")

root = tk.Tk()
root.title("Show Text Example")

# Label (initially empty)
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=10)

# Button
button = tk.Button(root, text="Show Text", command=show_text)
button.pack(pady=10)

root.mainloop()
