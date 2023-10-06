import openpyxl
import tkinter as tk
from tkinter import messagebox

# Load the Excel workbook
workbook = openpyxl.load_workbook('excel/Accenture NIE 2.8.23.xlsx')
sheet = workbook['Sheet1']

# Function to search data based on phone number, name, or USN
def search_data():
    search_query = search_entry.get().strip().lower()

    found_records = []
    for row in sheet.iter_rows(values_only=True):
        if search_query in (str(row[0]).strip().lower(),
                           str(row[1]).strip().lower(),
                           str(row[3]).strip()):
            found_records.append(row)

    if found_records:
        # Display the details in a message box
        details = ""
        for record in found_records:
            details += f"Name: {record[0]}\nUSN: {record[1]}\nEmail: {record[2]}\nPhone Number: {record[3]}\n\n"
        messagebox.showinfo("Search Result", details)
    else:
        # If no match found
        messagebox.showinfo("Search Result", "No matching records found.")

# Create the form
root = tk.Tk()
root.title("Student Details Search")

# Labels
tk.Label(root, text="Search (Name, USN, or Phone Number):").grid(row=0, column=0, columnspan=2)

# Entry field
search_entry = tk.Entry(root)
search_entry.grid(row=1, column=0, columnspan=2)

# Search button
tk.Button(root, text="Search", command=search_data).grid(row=2, column=0, columnspan=2)

root.mainloop()
