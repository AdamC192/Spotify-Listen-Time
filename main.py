import json
import math

def add_file_ms(directory):
    try:
        # Open the JSON file
        with open(directory, encoding="utf-8") as json_file:
            # Returns the JSON object as a list of dictionaries
            data = json.load(json_file)

        # Extracting 'msPlayed' value from each section
        total_ms = sum(entry.get("msPlayed", 0) for entry in data)
        return total_ms
    except FileNotFoundError:
        print("File not found!")
        return 0

# Convert 'msTotal' to mins, hours, days, and then print the data in the console
def display_total_ms(ms_played_total):
    print(f"\n\tTotal MILLISECONDS played: {ms_played_total}")
    print(f"\tTotal SECONDS played: {math.ceil(ms_played_total / 1000)}")
    print(f"\tTotal MINUTES played: {math.ceil(ms_played_total / 60000 * 100)}")
    print(f"\tTotal HOURS played: {math.ceil(ms_played_total / 3.6e+6 * 100) / 100}")
    print(f"\tTotal DAYS played: {math.ceil(ms_played_total / 8.64e+7 * 100) / 100}\n")

# Main loop
ms_played_total = 0

while True:
    input_file = input("Input a file path to add to the total time played, 'RESET' the total >> ")

    if input_file == "RESET":
        ms_played_total = 0
        continue

    ms_played_total += add_file_ms(input_file)
    display_total_ms(ms_played_total)
