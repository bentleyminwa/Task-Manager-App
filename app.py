import mysql.connector
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, messagebox

# connect to mysql database
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Bentleys05",
    database = "task_manager"
)
cursor = db.cursor()

def create_task(title, description):
    query = "INSERT INTO tasks (title, description) VALUES (%s, %s)"
    values = (title, description)
    cursor.execute(query, values)
    db.commit()
    print("Task created successfully!")

# Task Manager app
class TaskManagerApp():

    def __init__(self, window):
        self.window = window
        self.window.title("Task Manager")

        # Labels
        Label(window, text="Title: ").grid(row=0, column=0, padx=10, pady=10)
        Label(window, text="Description: ").grid(row=1, column=0, padx=10, pady=10)

        # Entry widgets
        self.title_entry = Entry(window)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)
        self.description_entry = Entry(window)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        Button(window, text="Add Task", command=self.add_task).grid(row=2, column=0, columnspan=2, pady=10)
        Button(window, text="Show Tasks", command=self.show_tasks).grid(row=3, column=0, columnspan=2, pady=10)

        # Listbox to display tasks
        self.task_listbox = Listbox(window, width=50, height=10)
        self.task_listbox.grid(row=4, column=0, columnspan=2, pady=10)

        # Scrollbar for listbox
        scrollbar = Scrollbar(window, command=self.task_listbox.yview)
        scrollbar.grid(row=4, column=2, sticky="ns")
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        
    
    # add_task
    def add_task(self):

        title = self.title_entry.get()
        description = self.description_entry.get()

        # check that title is not empty before adding
        if title:
            create_task(title, description)
            messagebox.showinfo("Success, Task added successfully!")
            self.title_entry.delete(0, "end")
            self.description_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning, please enter a title for the task")
        
    
    # show tasks
    def show_tasks(self):
        self.task_listbox.delete(0, "end")
        query = "SELECT * FROM tasks"
        cursor.execute(query)
        tasks = cursor.fetchall()
        for task in tasks:
            task_text = f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}"
            self.task_listbox.insert("end", task_text)


# Main program
if __name__ == "__main__":
    window = Tk()
    app = TaskManagerApp(window)
    window.mainloop()


# Close the database connection
cursor.close()
db.close()
    