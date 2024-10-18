import tkinter as tk
from tkinter import ttk

table = []
def create_task():
    task = []
    for entry in entries:
        task.append(entry.get())
    table.append(task)
    read_data()


# pop up window to input new task information
def task_info_popup():
    task_info = tk.Toplevel(window)
    task_info.title("New Task Information")
    # Create a new frame `frm_form` to contain the Label
    # and Entry widgets for entering address information
    frm_form = tk.Frame(master=task_info, relief=tk.SUNKEN, borderwidth=3)
    # Pack the frame into the window
    frm_form.pack()

    # List of field labels
    labels = [
        "Task Name:",
        "Due Date:",
        "Hours to Complete:",
        "Hours Worked:",
        "Progress:",
        "Importance:",
        "Tag:",
    ]

    
    # Loop over the list of field labels
    for idx, text in enumerate(labels):
        # Create a Label widget with the text from the labels list
        label = tk.Label(master=frm_form, text=text)
        # Create an Entry widget
        entry = tk.Entry(master=frm_form, width=50)
        # Use the grid geometry manager to place the Label and
        # Entry widgets in the row whose index is idx
        label.grid(row=idx, column=0, sticky="e")
        entry.grid(row=idx, column=1)
        entries.append(entry)

    # Create a new frame `frm_buttons` to contain the
    # Submit and Clear buttons. This frame fills the
    # whole window in the horizontal direction and has
    # 5 pixels of horizontal and vertical padding.
    frm_buttons = tk.Frame(master=task_info)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # Create the "Submit" button and pack it to the
    # right side of `frm_buttons`
    btn_submit = tk.Button(master=frm_buttons, text="Submit",command=create_task)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    # Create the "Clear" button and pack it to the
    # right side of `frm_buttons`
    btn_clear = tk.Button(master=frm_buttons, text="Clear")
    btn_clear.pack(side=tk.RIGHT, ipadx=10)



# Create a new window 
window = tk.Tk()
window.title("Task Prioritization Tool")

# menu
menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New Task', command=task_info_popup)


entries = []
# data tree/ table
table = [
   ["Task 1","tomorrow",1,0,0,25,"test",2000],
   ["Task 2","tomorrow",12,6,50,75,"test",50000],
   ["Task 3","tomorrow",2,1,25,25,"test",10000],
   ["Task 4","next week",11,3,40,30,"test",20000],
]
index=0
def read_data():
   for child in tree.get_children():
       tree.delete(child)
   for index, line in enumerate(table):
      tree.insert('', tk.END, iid = index,
         text = line[0], values = line[1:])
columns = ("Due Date", "Hours to Complete", "Hours Worked", "Progress", "Importance", "tag", "Priority")

tree= ttk.Treeview(window, columns=columns ,height = 20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text='Task Name')
tree.heading('Due Date', text='Due Date')
tree.heading('Hours to Complete', text='Hours to Complete')
tree.heading('Hours Worked', text='Hours Worked')
tree.heading('Progress', text='Progress')
tree.heading('Importance', text='Importance')
tree.heading('tag', text='tag')
tree.heading('Priority', text='Priority')


read_data()



# Start the application
window.mainloop()