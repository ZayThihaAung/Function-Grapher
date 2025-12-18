import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Window set up
root = tk.Tk()
root.title("Linear Function Grapher")
root.geometry('500x200')
root.resizable(False, False)

tk.Label(root, text="This program graphs linear functions of the form y=mx+b", font=("Arial Bold", 12)).pack(padx=10, pady=(10, 0))
tk.Label(root, text="Enter equations in the format mx+b or mx-b (No Spaces)", font=("Arial", 12)).pack(padx=10, pady=(10, 0))

try:
  input = tk.Entry(root, font=("Arial", 14), relief="solid", borderwidth=1)
  input.pack(fill="x", padx=10, pady=(0, 10))
except ValueError:
  messagebox.showerror("Input error", "Please enter a valid equation.")
  exit()

def draw():
  equation = input.get().strip()
  try: 
    x = [-2, -1, 0, 1, 2]
    pos_x = []
    pos_y = []
    if equation[0].isalpha(): # If the equation starts with x
      first_num = 1
    elif type(equation[0]) == type("p"): # If the eq starts with num in str
      first_num = -1
    elif equation[1].isalpha(): # If x is behind a number
      first_num = int(equation[0])
    elif equation[1].isdigit(): # If there's a neg num in front of x
      first_num = int(equation[0] + equation[1])
    else :
      first_num = int(equation[0] + equation[1])
    if type(equation[-2]) == type('text'): # If the num is negative
      last_num = int(equation[-2] + equation[-1])
    else :
      last_num = int(equation[-1])

    for i in x:
      plt_y = first_num * i + last_num
      pos_y.append(plt_y)
      pos_x.append(i)
    print(f"x {pos_x}, y {pos_y}")

    plt.plot(pos_x, pos_y, marker='o', color='red')
    plt.plot(0,0, marker='o', color='orange', label="Origin")
    plt.title(f"The Graph of {equation}")
    plt.legend()
    plt.grid()
    plt.show()

    input.delete(0, tk.END)
  
  except ValueError:
    messagebox.showerror("Input error", "Please enter a valid equation.")
    draw()

compute_btn = tk.Button(root, text="Graph Equation", font=("Arial Bold", 12), command=draw, 
                        bg="#7B94A0", fg='white', border=2, borderwidth=1)
compute_btn.pack(padx=10, pady=(0, 10), fill="x")
root.mainloop()