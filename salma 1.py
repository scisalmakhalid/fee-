import tkinter as tk
from tkinter import messagebox

def calculate_fee():
    try:
        base_fee = float(entry_base.get())
        tax = float(entry_tax.get())
        discount = float(entry_discount.get())
        
        total = base_fee + (base_fee * tax / 100) - (base_fee * discount / 100)
        label_result.config(text=f"Total Fee: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Fee Calculator")
root.geometry("300x300")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Base Fee ($):").pack(pady=5)
entry_base = tk.Entry(root)
entry_base.pack()

tk.Label(root, text="Tax (%) :").pack(pady=5)
entry_tax = tk.Entry(root)
entry_tax.pack()

tk.Label(root, text="Discount (%) :").pack(pady=5)
entry_discount = tk.Entry(root)
entry_discount.pack()

tk.Button(root, text="Calculate", command=calculate_fee).pack(pady=15)

label_result = tk.Label(root, text="Total Fee: $0.00", font=("Helvetica", 12, "bold"))
label_result.pack(pady=10)

# Run the app
root.mainloop()



























