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
    total_ms = 0

    # Iterate through each provided file and read the content
    if file_paths:
        for i in file_paths:
            try:
                # Open the JSON file
                with open(i, encoding="utf-8") as json_file:
                    # Returns the JSON object as a list of dictionaries
                    data = json.load(json_file)

                    # Extracting 'msPlayed' value from each section
                    ms = sum(entry.get("msPlayed", 0) for entry in data)
                
                total_ms += math.ceil(ms / 3.6e+6 * 100) / 100
                print(math.ceil(ms / 3.6e+6 * 100) / 100)

            except FileNotFoundError:
                print(f"Error: File '{i}' not found.")
                DisplayResult(-2)
            except json.JSONDecodeError:
                print(f"Error: File '{i}' is not a valid JSON file.")
                DisplayResult(-1)
            except Exception as e:
                print(f"An error occurred while processing file '{i}': {e}")
                DisplayResult(0)
        
        DisplayResult(total_ms)

def DisplayResult(total_ms):
    if total_ms > 0:
        result_label.config(text=f"Total Hours Played: {total_ms}")       
    elif total_ms == 0:
        result_label.config(text="Invalid file provided")
    elif total_ms == -1:
        result_label.config(text="Provided file not a valid JSON")
    elif total_ms == -2:
        result_label.config(text="Provided file not found")

# Reset the program by clearing all variables and values
def ResetProgram():
    global file_paths
    file_paths = []
    result_total_ms = 0
    uploadedfiles_label.config(text="No files uploaded")
    result_label.config(text="Total Hours Played: -")


# Define tkinter and the program details
root = tk.Tk()
root.title('Spotify Listen Time')
root.geometry("450x600")
# root.config(bg="") page background

# Interface elements
header1_font = font.Font(family="Helvetica", size=14, weight="bold")

pageheader_label = tk.Label(root, text="SPOTIFY LISTEN TIME", font=header1_font)

addfile_label = tk.Label(root, text="-- Add streaming history JSON files --")
addfile_button = tk.Button(text="ADD FILE", width=25, command=GetFile)

uploadedfiles_label = tk.Label(root, text="No files uploaded", justify=tk.CENTER)

calculate_label = tk.Label(root, text="-- Calculate the total listen result --")
calculate_button = tk.Button(text="CALCULATE TOTAL", width=25, command=CalculateResult)

result_label = tk.Label(root, text="Total Hours Played: -")

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
