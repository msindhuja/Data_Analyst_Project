import tkinter as tk

# Function to handle dropdown selection
def on_select(value):
  print(f"You selected: {value}")

# Create the main window
root = tk.Tk()
root.title("Dropdown Menu Example")

# Create a label
label = tk.Label(root, text="Select an option:")
label.pack()

# List of options for the dropdown menu
options = ["Option 1", "Option 2", "Option 3"]

# Create the dropdown menu with StringVar to hold the selected value
selected_option = tk.StringVar()
selected_option.set(options[0])
dropdown = tk.OptionMenu(root, selected_option, *options, command=on_select)
dropdown.pack()

# Run the main loop
root.mainloop()