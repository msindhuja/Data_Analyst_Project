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

# Function to add an employee
def add_employee():
    employee_id = employee_id_entry.get()
    name = name_entry.get()
    position = position_entry.get()
    salary = salary_entry.get()
    department = department_entry.get()
    
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Employees (EmployeeID, Name, Position, Salary, Dept_Id) VALUES (?, ?, ?, ?, ?)", (employee_id, name, position,salary, department))
            conn.commit()
            messagebox.showinfo("Success", "Employee added successfully.")
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error adding employee: {e}")
        finally:
            conn.close()

# Function to remove an employee
def remove_employee():
    employee_id = employee_id_remove_entry.get()
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Employees WHERE EmployeeID=?", (employee_id,))
            conn.commit()
            messagebox.showinfo("Success", "Employee removed successfully.")
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error removing employee: {e}")
        finally:
            conn.close()

# Function to display all employees
def display_employees():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employees")
            rows = cursor.fetchall()
            if rows:
                employee_list = "Employee List:\n"
                for row in rows:
                    employee_list += f"EmployeeID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Department: {row[3]}, Salary: {row[4]}\n"
                messagebox.showinfo("Employee List", employee_list)
            else:
                messagebox.showinfo("Employee List", "No employees found.")
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error displaying employees: {e}")
        finally:
            conn.close()

# Main window
root = tk.Tk()
root.title("Employee Management System")

# Add Employee Frame
add_employee_frame = tk.Frame(root)
add_employee_frame.pack(pady=10)

tk.Label(add_employee_frame, text="Employee ID:").grid(row=0, column=0)
employee_id_entry = tk.Entry(add_employee_frame)
employee_id_entry.grid(row=0, column=1)

tk.Label(add_employee_frame, text="Name:").grid(row=1, column=0)
name_entry = tk.Entry(add_employee_frame)
name_entry.grid(row=1, column=1)

tk.Label(add_employee_frame, text="Position:").grid(row=2, column=0)
position_entry = tk.Entry(add_employee_frame)
position_entry.grid(row=2, column=1)

tk.Label(add_employee_frame, text="Salary:").grid(row=4, column=0)
salary_entry = tk.Entry(add_employee_frame)
salary_entry.grid(row=4, column=1)

tk.Label(add_employee_frame, text="Dept_Id:").grid(row=3, column=0)
department_entry = tk.Entry(add_employee_frame)
department_entry.grid(row=3, column=1)

add_button = tk.Button(add_employee_frame, text="Add Employee", command=add_employee)
add_button.grid(row=5, columnspan=2)

# Remove Employee Frame
remove_employee_frame = tk.Frame(root)
remove_employee_frame.pack(pady=10)

tk.Label(remove_employee_frame, text="Employee ID to remove:").grid(row=0, column=0)
employee_id_remove_entry = tk.Entry(remove_employee_frame)
employee_id_remove_entry.grid(row=0, column=1)

remove_button = tk.Button(remove_employee_frame, text="Remove Employee", command=remove_employee)
remove_button.grid(row=1, columnspan=2)

# Display Employees Frame
display_employees_frame = tk.Frame(root)
display_employees_frame.pack(pady=10)

display_button = tk.Button(display_employees_frame, text="Display Employees", command=display_employees)
display_button.pack()

# Run the application
root.mainloop()
