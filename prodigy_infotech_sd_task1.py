import tkinter as tk
from tkinter import ttk, messagebox


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "C":
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            result_label.config(text=f"{temp}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K")
        elif unit == "F":
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            result_label.config(text=f"{temp}°F is {celsius:.2f}°C and {kelvin:.2f}K")
        elif unit == "K":
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            result_label.config(text=f"{temp}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")
        else:
            messagebox.showerror("Invalid Unit", "Please select a valid temperature unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


# Create the main window
root = tk.Tk()
root.title("Temperature Conversion Program")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TRadiobutton", font=("Helvetica", 12))

# Create and place the widgets
ttk.Label(root, text="Enter Temperature:").pack(pady=10)
entry_temp = ttk.Entry(root, width=10, font=("Helvetica", 12))
entry_temp.pack(pady=5)

ttk.Label(root, text="Select Unit:").pack(pady=10)
unit_var = tk.StringVar(value="C")
frame_units = ttk.Frame(root)
frame_units.pack(pady=5)
ttk.Radiobutton(frame_units, text="Celsius", variable=unit_var, value="C").pack(side="left", padx=10)
ttk.Radiobutton(frame_units, text="Fahrenheit", variable=unit_var, value="F").pack(side="left", padx=10)
ttk.Radiobutton(frame_units, text="Kelvin", variable=unit_var, value="K").pack(side="left", padx=10)

ttk.Button(root, text="Convert", command=convert_temperature).pack(pady=20)

result_label = ttk.Label(root, text="", background="#f0f0f0", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
