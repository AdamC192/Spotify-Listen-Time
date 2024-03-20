import tkinter as tk
import json
import math
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import font


# Variables
file_paths = []
result_total_ms = 0


# Get the import files
def GetFile():
    # Get the file path
    filename = askopenfilename()  # Show an "Open" dialog box and return the path to the selected file
    if filename:  # Check if a file was selected
        # Ensure there are never more than 5 files in the list
        if len(file_paths) == 5:
            file_paths.pop(0)  # Remove the oldest file in the list
        file_paths.append(filename)  # Append the new file path to the list
        
        # Update the label with the joined list of file paths
        uploadedfiles_label.config(text="\n".join(file_paths))
        
# Calculate the result
def CalculateResult():
    # Iterate through each provided file and read the content
    if file_paths:
        for i in file_paths:
            # Open the JSON file
            with open(i, encoding="utf-8") as json_file:
                # Returns the JSON object as a list of dictionaries
                data = json.load(json_file)

                # Extracting 'msPlayed' value from each section
                total_ms = sum(entry.get("msPlayed", 0) for entry in data)
        
        total_ms = math.ceil(total_ms / 60000) / 100
        DisplayResult(total_ms)

def DisplayResult(total_ms):
    result_label.config(text=f"Total Minutes Played: {total_ms}")       

# Reset the program by clearing all variables and values
def ResetProgram():
    for i in file_paths:
        file_paths[i].remove
    result_total_ms = 0
    uploadedfiles_label.config(text=file_paths)
    result_label.config(text="Total Minutes Played: -")


# Define tkinter and the program details
root = tk.Tk()
root.title('Spotify Listen Time')
root.geometry("400x650")
# root.config(bg="") page background

# Interface elements
header1_font = font.Font(family="Helvetica", size=14, weight="bold")

pageheader_label = tk.Label(root, text="SPOTIFY LISTEN TIME", font=header1_font)

addfile_label = tk.Label(root, text="-- Add streaming history JSON files --")
addfile_button = tk.Button(text="ADD FILE", width=25, command=GetFile)

uploadedfiles_label = tk.Label(root, text="No files uploaded", justify=tk.CENTER)

calculate_label = tk.Label(root, text="-- Calculate the total listen result --")
calculate_button = tk.Button(text="CALCULATE TOTAL", width=25, command=CalculateResult)

result_label = tk.Label(root, text="Total Minutes Played: -")

restart_button = tk.Button(text="RESET", width=25, command=ResetProgram)

# Apply interface elements
pageheader_label.pack(padx=30, pady=30)

addfile_label.pack(padx=10, pady=10)
addfile_button.pack()

uploadedfiles_label.pack(padx=30, pady=30)

calculate_label.pack(padx=10, pady=10)
calculate_button.pack()

result_label.pack(padx=30, pady=30)

restart_button.pack()

# The main loop
root.mainloop()
