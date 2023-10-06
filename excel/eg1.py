import os
import openpyxl as xl

# Specify the directory path where you want to store the file
directory_path = "D:\\study\\vsc\\excel"

# Create the directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Now you can create and save your Excel file in the specified directory
file_path = os.path.join(directory_path, "student.xlsx")

# Create a new workbook and add a new sheet
workbook = xl.Workbook()
sheet = workbook.active

# Write data to cells
sheet['A1'] = 'NAME'
sheet['B1'] = 'SIR NAME'
sheet['A2'] = "HEMANTH"
sheet['B2'] = "R"

# Save the workbook to the specified file path in .xlsx format
workbook.save(file_path)
 
# Close the workbook when done
workbook.close()
