import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

contacts = []


# Load contacts from file
def load_contacts():
    global contacts
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            contacts = json.load(file)


# Save contacts to file
def save_contacts():
    global contacts
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if not name or not phone or not email:
        messagebox.showerror("Error", "All fields are required.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    refresh_contacts()
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# Edit a selected contact
def edit_contact():
    selected_index = contacts_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Select a contact to edit.")
        return

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if not name or not phone or not email:
        messagebox.showerror("Error", "All fields are required.")
        return

    index = selected_index[0]
    contacts[index] = {"name": name, "phone": phone, "email": email}
    save_contacts()
    refresh_contacts()


# Delete a selected contact
def delete_contact():
    selected_index = contacts_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Select a contact to delete.")
        return

    index = selected_index[0]
    del contacts[index]
    save_contacts()
    refresh_contacts()


# Refresh the contacts listbox
def refresh_contacts():
    contacts_listbox.delete(0, tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")


# Show selected contact details in the entry fields
def show_contact_details(event):
    selected_index = contacts_listbox.curselection()
    if not selected_index:
        return

    index = selected_index[0]
    contact = contacts[index]

    name_entry.delete(0, tk.END)
    name_entry.insert(0, contact['name'])

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact['phone'])

    email_entry.delete(0, tk.END)
    email_entry.insert(0, contact['email'])


# Create the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=5)
style.configure("TEntry", font=("Helvetica", 12))

# Create and place the widgets
ttk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = ttk.Entry(root, width=25)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

ttk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
phone_entry = ttk.Entry(root, width=25)
phone_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

ttk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
email_entry = ttk.Entry(root, width=25)
email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

ttk.Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0, padx=10, pady=10, sticky="e")
ttk.Button(root, text="Edit Contact", command=edit_contact).grid(row=3, column=1, padx=10, pady=10, sticky="w")
ttk.Button(root, text="Delete Contact", command=delete_contact).grid(row=3, column=2, padx=10, pady=10, sticky="w")

contacts_listbox = tk.Listbox(root, height=10, width=50)
contacts_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
contacts_listbox.bind("<<ListboxSelect>>", show_contact_details)

# Load and display contacts
load_contacts()
refresh_contacts()

# Run the application
root.mainloop()
