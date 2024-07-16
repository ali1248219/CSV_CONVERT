import os
import tkinter as tk
from tkinter import filedialog

def convert_csv(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Perform replacements in the specified order
    content = content.replace(',', '|').replace(':', '.').replace(';', ',')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    input_file = filedialog.askopenfilename(title="Select input CSV file", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if not input_file:
        print("No input file selected.")
        return

    output_file = filedialog.asksaveasfilename(title="Select output CSV file", defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if not output_file:
        print("No output file selected.")
        return

    convert_csv(input_file, output_file)
    print(f"Conversion completed. Output file saved as {output_file}")

# Run the file selection and conversion
select_files()
