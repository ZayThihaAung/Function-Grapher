import matplotlib.pyplot as plt
from fractions import Fraction
import tkinter as tk
from tkinter import messagebox

defult = [-3, -2, -1, 0, 1, 2, 3]
# Window set up
root = tk.Tk()
root.title("Quadratic Function Grapher")
root.geometry('500x200')
root.resizable(False, False)

tk.Label(root, text="This program graphs quadratic functions of the form y=ax^2", font=("Arial Bold", 12)).pack(padx=10, pady=(10, 0))
tk.Label(root, text="Enter equations in the format ax^2 (No Spaces)", font=("Arial", 12)).pack(padx=10, pady=(10, 0))

input = tk.Entry(root, font=("Arial", 14), relief="solid", borderwidth=1)
input.pack(fill="x", padx=10, pady=(0, 10))

def draw():
  try :
    pos_x = []
    pos_y = []

    equation = input.get().strip() # Get user input and remove spaces

    if equation[0].isalpha(): # If the equation starts with x
      first_num = 1
    elif equation[1].isalpha(): # If x is behind a number
      first_num = int(equation[0])
    elif equation[3].isdigit():
      first_num = Fraction(equation[0] + equation[1] + equation[2] + equation[3])
    elif equation[1].isdigit():
      first_num = int(equation[0] + equation[1])
    elif len(equation) > 4 or len(equation) < 5: # If the input length is incorrect
      messagebox.showerror("Input error", "Please enter a valid equation.")
      draw()
    else: # If there's a fraction or neg num in front of x
      first_num = Fraction(equation[0] + equation[1] + equation[2])
      
    for i in defult:
      plt_y = first_num * (i ** 2)
      pos_y.append(plt_y)
      pos_x.append(i)

    print(first_num)
    print(f"x {pos_x}, y {pos_y}")  
    plt.plot(pos_x, pos_y, marker='x', color='blue')
    plt.plot(0, 0, marker='o', color='orange', label="Origin")
    plt.title(f"The Graph of {equation}")
    plt.legend()
    plt.grid()
    plt.show()
    pos_x.clear()
    pos_y.clear()

    input.delete(0, tk.END)
  except ValueError:
    messagebox.showerror("Input error", "Please enter a valid equation.")
    draw()
  
compute_btn = tk.Button(root, text="Graph Equation", font=("Arial Bold", 12), command=draw, 
                        bg="#7B94A0", fg='white', border=2, borderwidth=1)
compute_btn.pack(padx=10, pady=(0, 10), fill="x")

root.mainloop()