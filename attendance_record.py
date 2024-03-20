import os
from openpyxl import Workbook
import datetime

# Create a directory called 'attendance' if it doesn't exist
attendance_dir = "attendance"
if not os.path.exists(attendance_dir):
    os.makedirs(attendance_dir)

# Set the path for saving the workbook in the 'attendance' directory
file_path = os.path.join(attendance_dir, "sample.xlsx")

# Create a new workbook
wb = Workbook()

# Grab the active worksheet
ws = wb.active


ws.append(["Name", "Surname", "Time In", "Time Out"])


# Save the workbook in the 'attendance' directory
wb.save(file_path)

print(f"Workbook saved successfully in the '{attendance_dir}' directory as 'sample.xlsx'")
