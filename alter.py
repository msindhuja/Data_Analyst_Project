import tkinter as tk
from tkinter import messagebox
import pyodbc

# Function to connect to the database
def connect_to_database():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-LEN15YOGA;DATABASE=EmployeeDB;Trusted_Connection=yes;UID = sa;PWD=123')
        return conn
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error connecting to database: {e}")
        return None
#Function to select operation ADD/REMOVE
def alter_table():
    operation = operation_var.get()
    if operation == "ADD":
        alter_add_column()
    elif operation == "REMOVE":
        alter_remove_column()
    else:
        messagebox.showerror("Error", "Please select an operation (Add or Remove).")
    
#Function to add column  
def alter_add_column():
    table_name = table_name_entry.get()
    column_name = column_name_entry.get()
    data_type = data_type_variable.get()

    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(f"ALTER TABLE {table_name} ADD {column_name} {data_type}")
            conn.commit()
            messagebox.showinfo("Success", f"Added column '{column_name}' successfully")
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error adding column: {e}")
        finally:
            conn.close()
            
#Function to remove column from a table
def alter_remove_column():
    table_name = table_name_entry.get()
    column_name = column_name_entry.get()

    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")
            conn.commit()
            messagebox.showinfo("Success", f"Dropped {column_name} successfully")
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error dropping column {e}")
        finally:
            conn.close()

# Main window
root = tk.Tk()
root.title("Alter Table")

# Radio Button Frame
radio_button_frame = tk.Frame(root)
radio_button_frame.pack(pady=10)

operation_var = tk.StringVar(root)  # Variable to store operation (add/remove)

# Radio buttons for Add/Remove operation
add_column_radio = tk.Radiobutton(radio_button_frame, text="Add Column", variable=operation_var, value="ADD")
add_column_radio.grid(row=0, column=0)

remove_column_radio = tk.Radiobutton(radio_button_frame, text="Remove Column", variable=operation_var, value="REMOVE")
remove_column_radio.grid(row=0, column=1)

# table name frame
table_name_frame = tk.Frame(root)
table_name_frame.pack(pady=10)

table_name_label = tk.Label(table_name_frame, text="Table Name:")
table_name_label.grid(row=0, column=0)

table_name_entry = tk.Entry(table_name_frame)
table_name_entry.grid(row=0, column=1)

# Column Name Frame
column_name_frame = tk.Frame(root)
column_name_frame.pack(pady=10)

column_name_label = tk.Label(column_name_frame, text="Column Name:")
column_name_label.grid(row=0, column=0)

column_name_entry = tk.Entry(column_name_frame)
column_name_entry.grid(row=0, column=1)

#List of options to select datatype
data_type_options = ["INT", "INT PRIMARY KEY", "VARCHAR(50)", "DECIMAL(10,2)", "TEXT", "FLOAT"]
data_type_variable = tk.StringVar(root)
data_type_variable.set(data_type_options[0])  # Set default data type
data_type_dropdown = tk.OptionMenu(root, data_type_variable, *data_type_options)
data_type_dropdown.pack(pady=10)

# Alter Button
alter_button = tk.Button(root, text="ALTER TABLE", command= alter_table)
alter_button.pack(pady=10)

# Run the main loop
root.mainloop()