import tkinter as tk
root=tk.Tk()
root.geometry("400x300")
top=tk.Frame(root,bg="lightgreen",height=60)
top.pack(fill="x")
middle=tk.Frame(root,bg="white")
middle.pack(fill="both",expand=True)
bottom=tk.Frame(root,bg="lightgray",height=50)
bottom.pack(fill="x")
tk.Label(top,text="Header",bg="lightgreen",
                              font=("Arial",16)).pack(pady=15)
