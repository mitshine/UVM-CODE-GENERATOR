# import tkinter module
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox

# creating main tkinter window/toplevel
master = Tk()

master.title("UVM Code Generator")
img = PhotoImage(file='icon.png')
master.iconphoto(False, img)

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def clear():
    [widget.delete(0, END) for widget in master.winfo_children() if isinstance(widget, Entry)]

def OnClick_Reset():
  messagebox.showinfo("Welcome to GFG.",  e1.get()) 

def OnClick_Submit():
  messagebox.showinfo("Welcome to GFG.",  e1.get()) 
  if(e1.get()):
     with open(e1.get()+".sv", "w") as file:
         file.write("class "+e1.get()+" extends uvm_test"+"\n\n\n"+"endclass")
         print("Generated the test class")
  if(e2.get()):
     with open(e2.get()+".sv", "w") as file:
         file.write("class "+e2.get()+" extends uvm_environment"+"\n\n\n"+"endclass")
         print("Generated the environment class")
  if(e3.get()):
     with open(e3.get()+".sv", "w") as file:
         file.write("interface "+e3.get()+"\n\n\n"+"endinterface")
         print("Generated the interface module")
  if(e4.get()):
     with open(e4.get()+".sv", "w") as file:
         file.write("class "+e4.get()+" extends uvm_agent"+"\n\n\n"+"endclass")
         print("Generated the agent class")
  if(e5.get()):
     with open(e5.get()+".sv", "w") as file:
         file.write("class "+e5.get()+" extends uvm_monitor"+"\n\n\n"+"endclass")
         print("Generated the monitor class")
  if(e6.get()):
     with open(e6.get()+".sv", "w") as file:
         file.write("class "+e6.get()+" extends uvm_driver"+"\n\n\n"+"endclass")
         print("Generated the driver class")
  if(e7.get()):
     with open(e7.get()+".sv", "w") as file:
         file.write("class "+e7.get()+" extends uvm_sequencer"+"\n\n\n"+"endclass")
         print("Generated the sequencer class")
  if(e8.get()):
     with open(e8.get()+".sv", "w") as file:
         file.write("class "+e8.get()+" extends uvm_sequence_item"+"\n\n\n"+"endclass")
         print("Generated the sequence_item class")
  if(e9.get()):
     with open(e9.get()+".sv", "w") as file:
         file.write("class "+e9.get()+" extends uvm_sequence"+"\n\n\n"+"endclass")
         print("Generated the sequence class")
  if(e10.get()):
     with open(e10.get()+".sv", "w") as file:
         file.write("class "+e10.get()+" extends uvm_scoreboard"+"\n\n\n"+"endclass")
         print("Generated the scoreboard class")

# this will create a label widget
l1 = Label(master, text = "Test Class Name")
l2 = Label(master, text = "Environment Class Name")
l3 = Label(master, text = "Interface Name")
l4 = Label(master, text = "Agent Name")
l5 = Label(master, text = "Monitor Name")
l6 = Label(master, text = "Driver Name")
l7 = Label(master, text = "Sequencer Name")
l8 = Label(master, text = "Sequence Item Name")
l9 = Label(master, text = "Sequence Name")
l10 = Label(master, text = "Scoreboard Name")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

l3.grid(row = 2, column = 0, sticky = W, pady = 2)
l4.grid(row = 3, column = 0, sticky = W, pady = 2)

l5.grid(row = 4, column = 0, sticky = W, pady = 2)
l6.grid(row = 5, column = 0, sticky = W, pady = 2)

l7.grid(row = 6, column = 0, sticky = W, pady = 2)
l8.grid(row = 7, column = 0, sticky = W, pady = 2)

l9.grid(row = 8, column = 0, sticky = W, pady = 2)
l10.grid(row = 9, column = 0, sticky = W, pady = 2)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

e3.grid(row = 2, column = 1, pady = 2)
e4.grid(row = 3, column = 1, pady = 2)
e5.grid(row = 4, column = 1, pady = 2)
e6.grid(row = 5, column = 1, pady = 2)
e7.grid(row = 6, column = 1, pady = 2)
e8.grid(row = 7, column = 1, pady = 2)
e9.grid(row = 8, column = 1, pady = 2)
e10.grid(row = 9, column = 1, pady = 2)

#sbmitbtn = Button(master, text = "Generate", command = OnClick_Submit).place(x = 350, y = 200)

button1 = Button(master, text ="Reset", command = clear)
button1.grid(row = 10, column = 0,  padx = 10, pady = 10)

button2 = Button(master, text ="Generate", command = OnClick_Submit)
button2.grid(row = 10, column = 1, padx = 10, pady = 10)

# Creating Menubar 
menubar = Menu(master) 
  
# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='New File', command = None) 
file.add_command(label ='Open...', command = None) 
file.add_command(label ='Save', command = None) 
file.add_separator() 
file.add_command(label ='Exit', command = master.destroy) 
  
# Adding Edit Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = None) 
edit.add_command(label ='Copy', command = None) 
edit.add_command(label ='Paste', command = None) 
edit.add_command(label ='Select All', command = None) 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None) 
  
# Adding Help Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None) 
  
# display Menu 
master.config(menu = menubar) 

# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()