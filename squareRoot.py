import math
import matplotlib.pyplot as plt 
import tkinter as tk
from tkinter import messagebox

defult = [0, 1, 2, 3]

# Window set up
root = tk.Tk()
root.title("Square Root Function Grapher")
root.geometry('500x200')
root.resizable(False, False)

tk.Label(root, text="This program graphs square root functions of the form y=a√x", font=("Arial Bold", 12)).pack(padx=10, pady=(10, 0))
tk.Label(root, text="This program graphs the function y=3√x", font=("Arial", 12)).pack(padx=10, pady=(10, 0))

input = tk.Entry(root, font=("Arial", 14), relief="solid", borderwidth=1)
input.pack(fill="x", padx=10, pady=(0, 10))

def draw():
    equation = input.get() # Get user input and remove spaces
    pos_x = []
    pos_y = []
    for i in defult:
      plt_y = i * math.sqrt(float(equation))
      pos_x.append(i)
      pos_y.append(plt_y)
    
    plt.plot(pos_x, pos_y, marker='*', color='red')
    plt.title(f"The Graph of y= {equation[0]}√x")
    plt.plot(0, 0, marker='o', color='orange', label="Origin")
    plt.grid()
    plt.legend()
    plt.show()

    input.delete(0, tk.END)

compute_button = tk.Button(root, text="Graph Equation", font=("Arial Bold", 12), command=draw,
                          bg="#7B94A0", fg='white', border=2, borderwidth=1)
compute_button.pack(pady=20)

root.mainloop()