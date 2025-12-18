import matplotlib.pyplot as plt
from fractions import Fraction
import tkinter as tk
from tkinter import messagebox
# Formula = a |x-h| + k
# h = x, k = y
defult = [-3, -2, -1, 0, 1, 2, 3]
defult2 = [3, 2, 1, 0, 1, 2, 3]
defult3 = [-3, -2, -1, 0, -1, -2, -3]

# Window setup
root = tk.Tk()
root.resizable(False, False)
root.title("Absolute Value Function Grapher")
root.geometry('500x300')

tk.Label(root, text="This program graphs absolute value functions of the form a|x-h|+k", font=("Arial Bold", 12)).pack(padx=10, pady=(10, 0))
tk.Label(root, text="Enter equations in the format a(x-h)+k using () instead of ||", font=("Arial", 12)).pack(padx=10, pady=(10, 0))

try:
  input = tk.Entry(root, font=("Arial", 14), relief="solid", borderwidth=1)
  input.pack(fill="x", padx=10, pady=(0, 10))
except ValueError:
  messagebox.showerror("Input error", "Please enter a valid equation.")
  exit()

def draw():
    equation = input.get().strip()

    # This is for the translation based on user's equation
    x = []
    y = []
    # For base |x| and -|x|
    pos_x = []
    pos_y = []

    # This part is for error handling based on how user put the equation
    if len(equation) == 4:
      a_value = int(equation[0])
      h_value = 0
      k_value = 0
    elif len(equation) == 5:
      a_value = int(equation[0] + equation[1])
      h_value = 0
      k_value = 0
    elif equation.find("_") == 0 or equation[0] == '(': # If the a is underscore or missing
      messagebox.showerror("Input error", "Please enter a valid equation.")
      print("Error: Invalid equation input.2")
      return
    elif equation[3].isdigit(): # If the a is negative fraction
      converted = equation[0] + equation[1] + equation[2] + equation[3]
      a_value = Fraction(converted)
      if 6 < len(equation) > 8:
        h_value = 0
      else:
        h_value = int(equation[6] + equation[7])
    elif equation[2].isdigit(): # If the a is fraction
      converted2 = equation[0] + equation[1] + equation[2]
      a_value = Fraction(converted2)
      if 6 < len(equation) > 8:
        h_value = 0
      else:
        h_value = int(equation[5] + equation[6])
    elif equation[1].isdigit(): # If the a is negative
      a_value = int(equation[0] + equation[1])
      h_value = int(equation[4] + equation[5])
    else : # If the a is only minus
      a_value = -1 
      h_value = int(equation[3] + equation[4])
    if len(equation) == 4 or len(equation) == 5:
      pass
    else:
      k_value = int(equation[-2] + equation[-1])
  
    if a_value < 0:  # This is the translation of base -|x| 
    # h is always taken inverse
      if h_value > 0:
        h_value = -abs(h_value)
      else:
        h_value = abs(h_value)
      # This code is based on -|x| or defult
      for i in defult:
        pos_x.append(i)
      for t in defult3:
        pos_y.append(t)
      for c in defult:
        px = c + h_value
        x.append(px)
      for d in defult3:
        py = d + k_value
        y.append(py)
    
    if a_value > 0:  # This is the translation of base |x|
    # h is always taken inverse
      if h_value > 0:
        h_value = -abs(h_value)
      else:
        h_value = abs(h_value)
      # This code is based on |x| or defult
      for i in defult:
        pos_x.append(i)
      for t in defult2:
        pos_y.append(t) 
      for a in defult:
        plt_x = a + h_value
        x.append(plt_x)
      for b in defult2:
        plt_y = b + k_value
        y.append(plt_y) 

    formated = equation.replace("(", "|")
    final_format = formated.replace(")", "|")  
    print(f"x {x}, y {y}")
    print(f"Vertex ({h_value}, {k_value})")
    if a_value > 0:
      base = ''
    else :
      base = equation[0]
    plt.plot(pos_x, pos_y, color="red", marker='x', label=f"Base {base}|x|")
    plt.plot(0,0, color='orange', label="Origin", marker='o')
    plt.plot(x, y, color='green', label='Translation', marker="*", linestyle='dotted')
    plt.title(f"The Graph of {final_format}")
    plt.legend()
    plt.grid()
    plt.show()

    input.delete(0, tk.END)

compute_btn = tk.Button(root, text="Graph Equation", font=("Arial Bold", 12), command=draw, 
                        bg="#7B94A0", fg='white', border=2, borderwidth=1)
compute_btn.pack(padx=10, pady=(0, 10), fill="x")

root.mainloop()