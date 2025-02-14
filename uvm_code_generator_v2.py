# import tkinter module
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
import os
import shutil
from tkinter import ttk 

# creating main tkinter window/toplevel
master = Tk()

master.eval('tk::PlaceWindow . center')

val1=""
val2=""
val3=""
val4=""
val5=""
val6=""
val7=""
val8=""
val9=""
val10=""

master.title("UVM Code Generator")
img = PhotoImage(file='icon.png')
master.iconphoto(False, img)
#var = 0

def print_all():
    var = 0
    for i in check_box_list:
        var = var + 1
        if 'selected' in i.state():
            print("Checkbutton: C%d is selected!, i.state(): %s" % (var, i.state()))
    #print(CheckVar1.get())

def check_all():
    for i in check_box_list:
        i.state(["selected"])
    
def uncheck_all():
    for i in check_box_list:
        i.state(['!alternate'])
    for i in check_box_list:
        i.state(["!selected"])
    
def uncheck():
    C1.state(['!alternate'])
    C2.state(['!alternate'])
    C3.state(['!alternate'])
    C4.state(['!alternate'])
    C5.state(['!alternate'])
    C6.state(['!alternate'])
    C7.state(['!alternate'])
    C8.state(['!alternate'])
    C9.state(['!alternate'])
    C10.state(['!alternate'])
    C11.state(['!alternate'])
    C12.state(['!alternate'])
    C13.state(['!alternate'])
    C14.state(['!alternate'])
    C15.state(['!alternate'])
    C16.state(['!alternate'])
    C17.state(['!alternate'])
    C18.state(['!alternate'])
    C19.state(['!alternate'])
    C20.state(['!alternate'])
    C21.state(['!alternate'])
    C22.state(['!alternate'])
    '''
    C23.state(['!alternate'])
    C24.state(['!alternate'])
    C25.state(['!alternate'])
    C26.state(['!alternate'])
    C27.state(['!alternate'])
    C28.state(['!alternate'])
    C29.state(['!alternate'])
    C30.state(['!alternate'])
    '''
    C31.state(['!alternate'])
    C32.state(['!alternate'])
    C33.state(['!alternate'])
    C34.state(['!alternate'])
    C35.state(['!alternate'])
    C36.state(['!alternate'])
    C37.state(['!alternate'])
    C38.state(['!alternate'])
    C39.state(['!alternate'])
    C40.state(['!alternate'])
    C41.state(['!alternate'])
    C42.state(['!alternate'])
    C43.state(['!alternate'])
    C44.state(['!alternate'])
    C45.state(['!alternate'])
    C46.state(['!alternate'])
    C47.state(['!alternate'])
    C48.state(['!alternate'])
    C49.state(['!alternate'])
    C50.state(['!alternate'])
    C51.state(['!alternate'])
    C52.state(['!alternate'])
    C53.state(['!alternate'])
    C54.state(['!alternate'])
    C55.state(['!alternate'])
    C56.state(['!alternate'])
    C57.state(['!alternate'])
    C58.state(['!alternate'])
    C59.state(['!alternate'])
    C60.state(['!alternate'])
    C61.state(['!alternate'])
    C62.state(['!alternate'])
    C63.state(['!alternate'])
    C64.state(['!alternate'])
    C65.state(['!alternate'])
    C66.state(['!alternate'])
    C67.state(['!alternate'])
    C68.state(['!alternate'])
    C69.state(['!alternate'])
    C70.state(['!alternate'])
    C71.state(['!alternate'])
    C72.state(['!alternate'])
    C73.state(['!alternate'])
    C74.state(['!alternate'])
    C75.state(['!alternate'])
    C76.state(['!alternate'])
    C77.state(['!alternate'])
    C78.state(['!alternate'])
    C79.state(['!alternate'])
    C80.state(['!alternate'])
    C81.state(['!alternate'])
    C82.state(['!alternate'])
    C83.state(['!alternate'])
    C84.state(['!alternate'])
    C85.state(['!alternate'])
    C86.state(['!alternate'])
    C87.state(['!alternate'])
    C88.state(['!alternate'])
    C89.state(['!alternate'])
    C90.state(['!alternate'])
    C91.state(['!alternate'])
    C92.state(['!alternate'])
    C93.state(['!alternate'])
    C94.state(['!alternate'])
    C95.state(['!alternate'])
    C96.state(['!alternate'])
    C97.state(['!alternate'])
    C98.state(['!alternate'])
    C99.state(['!alternate'])
    C100.state(['!alternate'])

def center_window_geometry(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def center_window_screen(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")

def save_dict_to_file(dic):
    # Check whether a path pointing to a file
    isFile = os.path.isfile("user.txt")
    if(isFile):
       f = open('user.txt','a')
       f.write("\n"+str(dic)+"\n")
       f.close()
    else:
       f = open('user.txt','w')
       f.write(str(dic)+"\n")
       f.close()
    print("Data is written into the file.")
    print_all()

def OnClick_Quit():
  answer = messagebox.askquestion("askquestion", "Are you sure?") 
  #if answer == "yes":

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def clear():
    [widget.delete(0, END) for widget in master.winfo_children() if isinstance(widget, Entry)]
    #Clear all the selected checkbozes - TODO

def OnClick_Reset():
  messagebox.showinfo("Welcome to GFG.",  e1.get()) 

def OnClick_Submit():
  messagebox.showinfo("Welcome!",  "UVM Source Code is successfully generated!") 
  #print("VALARA: ", e1.get())
  val1 = e1.get()
  val2 = e2.get()
  val3 = e3.get()
  val4 = e4.get()
  val5 = e5.get()
  val6 = e6.get()
  val7 = e7.get()
  val8 = e8.get()
  val9 = e9.get()
  val10 = e10.get()

  dict1 = {"Test Class Name": val1, "Environment Class Name": val2, "Interface Name": val3, "Agent Name": val4, "Monitor Name": val5, "Driver Name": val6, "Sequencer Name": val7, "Sequence Item Name": val8, "Sequence Name": val9, "Scoreboard Name": val10}

  save_dict_to_file(dict1)

  #if not os.path.exists("uvm_hierarchy_files"):     
  # if the demo_folder directory is not present  
  # then create it. 
  #os.makedirs("path/to/demo_folder")
  #os.mkdir("uvm_hierarchy_files")

  dir = 'uvm_hierarchy_files'
  if os.path.exists(dir):
    shutil.rmtree(dir)
  os.makedirs(dir)

  '''
  # Create four checkbuttons inside the frame
  C1 = Checkbutton(master, text="new", cursor="hand2")
  C1.grid(column=2, row=0, padx=10, pady=10)

  C2 = Checkbutton(master, text = "build", cursor="hand2")
  C2.grid(column=3, row=0, padx=10, pady=10)

  C3 = Checkbutton(master, text = "connect", cursor="hand2")
  C3.grid(column=4, row=0, padx=10, pady=10)

  C4 = Checkbutton(master, text = "run", cursor="hand2")
  C4.grid(column=5, row=0, padx=10, pady=10)

  C5 = Checkbutton(master, text = "check", cursor="hand2")
  C5.grid(column=6, row=0, padx=10, pady=10)

  C6 = Checkbutton(master, text = "report", cursor="hand2")
  C6.grid(column=7, row=0, padx=10, pady=10)
  '''

  if(e1.get()):
     with open("uvm_hierarchy_files/"+e1.get()+".sv", "w") as file:
         file.write("class "+e1.get()+" extends uvm_test;\n\n")
         file.write("  `uvm_component_utils("+e1.get()+")\n\n")
         if(C1.instate(['selected'])):
             file.write("  function new(string name = "+e1.get()+", uvm_component parent = null);\n")
             file.write("    super.new(name, parent);\n")
             file.write("  endfunction\n\n")
         if(C2.instate(['selected'])):
             file.write("  function void build_phase(uvm_phase phase);\n")
             file.write("    super.build_phase(phase);\n")
             #// component creation
             #compA = mycomponent::type_id::create("compA", this); 
             #compB = param_component #(8, 1)::type_id::create("compB", this); 
             file.write("  endfunction\n\n")
         if(C6.instate(['selected'])):
             file.write("  task run_phase(uvm_phase phase);\n\n")
             file.write("  endtask")

         file.write("\n\n\n"+"endclass")

         print("Generated the test class")
  if(e2.get()):
     with open("uvm_hierarchy_files/"+e2.get()+".sv", "w") as file:
         file.write("class "+e2.get()+" extends uvm_environment;"+"\n\n")
         file.write("  `uvm_component_utils("+e2.get()+")\n\n")
         if(C11.instate(['selected'])):
             file.write("  function new(string name = "+e2.get()+", uvm_component parent = null);\n")
             file.write("    super.new(name, parent);\n")
             file.write("  endfunction\n\n")
         if(C12.instate(['selected'])):
             file.write("  function void build_phase(uvm_phase phase);\n")
             file.write("    super.build_phase(phase);\n")
             #// component creation
             #compA = mycomponent::type_id::create("compA", this); 
             #compB = param_component #(8, 1)::type_id::create("compB", this); 
             file.write("  endfunction\n\n")
         if(C16.instate(['selected'])):
             file.write("  task run_phase(uvm_phase phase);\n\n")
             file.write("  endtask")

         file.write("\n\n\n"+"endclass")

         print("Generated the environment class")
  if(e3.get()):
     with open("uvm_hierarchy_files/"+e3.get()+".sv", "w") as file:
         file.write("interface "+e3.get()+"(input clk);\n\n\n")
         if(C21.instate(['selected'])):
             file.write("   clocking_block\n\n")
             file.write("   endclocking\n\n")
         if(C22.instate(['selected'])):
             file.write("   modport\n\n")
             file.write("   endmodport\n\n")
         file.write("\n\n"+"endinterface")
         print("Generated the interface module")
  if(e4.get()):
     with open("uvm_hierarchy_files/"+e4.get()+".sv", "w") as file:
         file.write("class "+e4.get()+" extends uvm_agent;"+"\n\n")
         file.write("  `uvm_component_utils("+e4.get()+")\n\n")
         if(C31.instate(['selected'])):
             file.write("  function new(string name = "+e4.get()+", uvm_component parent = null);\n")
             file.write("    super.new(name, parent);\n")
             file.write("  endfunction\n\n")
         if(C32.instate(['selected'])):
             file.write("  function void build_phase(uvm_phase phase);\n")
             file.write("    super.build_phase(phase);\n")
             #// component creation
             #compA = mycomponent::type_id::create("compA", this); 
             #compB = param_component #(8, 1)::type_id::create("compB", this); 
             file.write("  endfunction\n\n")
         if(C36.instate(['selected'])):
             file.write("  task run_phase(uvm_phase phase);\n\n")
             file.write("  endtask")

         file.write("\n\n\n"+"endclass")

         print("Generated the agent class")
  if(e5.get()):
     with open("uvm_hierarchy_files/"+e5.get()+".sv", "w") as file:
         file.write("class "+e5.get()+" extends uvm_monitor;"+"\n\n")
         file.write("  `uvm_component_utils("+e5.get()+")\n\n")
         if(C41.instate(['selected'])):
             file.write("  function new(string name = "+e5.get()+", uvm_component parent = null);\n")
             file.write("    super.new(name, parent);\n")
             file.write("  endfunction\n\n")
         if(C42.instate(['selected'])):
             file.write("  function void build_phase(uvm_phase phase);\n")
             file.write("    super.build_phase(phase);\n")
             #// component creation
             #compA = mycomponent::type_id::create("compA", this); 
             #compB = param_component #(8, 1)::type_id::create("compB", this); 
             file.write("  endfunction\n\n")
         if(C46.instate(['selected'])):
             file.write("  task run_phase(uvm_phase phase);\n\n")
             file.write("  endtask")

         file.write("\n\n\n"+"endclass")

         print("Generated the monitor class")
  if(e6.get()):
     with open("uvm_hierarchy_files/"+e6.get()+".sv", "w") as file:
         file.write("class "+e6.get()+" extends uvm_driver;"+"\n\n")
         file.write("  `uvm_component_utils("+e6.get()+")\n\n")
         if(C51.instate(['selected'])):
             file.write("  function new(string name = "+e6.get()+", uvm_component parent = null)\n")
             file.write("    super.new(name, parent);\n")
             file.write("  endfunction\n\n")
         if(C52.instate(['selected'])):
             file.write("  function void build_phase(uvm_phase phase);\n")
             file.write("    super.build_phase(phase);\n")
             #// component creation
             #compA = mycomponent::type_id::create("compA", this); 
             #compB = param_component #(8, 1)::type_id::create("compB", this); 
             file.write("  endfunction\n\n")
         if(C56.instate(['selected'])):
             file.write("  task run_phase(uvm_phase phase);\n\n")
             file.write("  endtask")

         file.write("\n\n\n"+"endclass")

         print("Generated the driver class")
  if(e7.get()):
     with open("uvm_hierarchy_files/"+e7.get()+".sv", "w") as file:
         file.write("class "+e7.get()+" extends uvm_sequencer;"+"\n\n")
         file.write("  `uvm_component_utils("+e7.get()+")\n\n")
         if(C61.instate(['selected'])):
             file.write("  function new(string name = "+e7.get()+", uvm_component parent = null);\n")
             file.write("    super.new(name, parent);\n")
             file.write("  endfunction\n\n")
         if(C62.instate(['selected'])):
             file.write("  function void build_phase(uvm_phase phase);\n")
             file.write("    super.build_phase(phase);\n")
             #// component creation
             #compA = mycomponent::type_id::create("compA", this); 
             #compB = param_component #(8, 1)::type_id::create("compB", this); 
             file.write("  endfunction\n\n")
         if(C66.instate(['selected'])):
             file.write("  task run_phase(uvm_phase phase);\n\n")
             file.write("  endtask")

         file.write("\n\n\n"+"endclass")

         print("Generated the sequencer class")
  if(e8.get()):
     with open("uvm_hierarchy_files/"+e8.get()+".sv", "w") as file:
         file.write("class "+e8.get()+" extends uvm_sequence_item;"+"\n\n")
         file.write("  `uvm_component_utils("+e8.get()+")\n\n")
         if(C71.instate(['selected'])):
             file.write("  function new(string name = "+e8.get()+", uvm_component parent = null);\n")
             file.write("    super.new(name, parent);\n")
             file.write("  endfunction\n\n")
         if(C72.instate(['selected'])):
             file.write("  function void build_phase(uvm_phase phase);\n")
             file.write("    super.build_phase(phase);\n")
             #// component creation
             #compA = mycomponent::type_id::create("compA", this); 
             #compB = param_component #(8, 1)::type_id::create("compB", this); 
             file.write("  endfunction\n\n")
         if(C76.instate(['selected'])):
             file.write("  task run_phase(uvm_phase phase);\n\n")
             file.write("  endtask")

         file.write("\n\n\n"+"endclass")

         print("Generated the sequence_item class")
  if(e9.get()):
     with open("uvm_hierarchy_files/"+e9.get()+".sv", "w") as file:
         file.write("class "+e9.get()+" extends uvm_sequence;"+"\n\n")
         file.write("  `uvm_component_utils("+e9.get()+")\n\n")
         if(C81.instate(['selected'])):
             file.write("  function new(string name = "+e9.get()+", uvm_component parent = null);\n")
             file.write("    super.new(name, parent);\n")
             file.write("  endfunction\n\n")
         if(C82.instate(['selected'])):
             file.write("  function void build_phase(uvm_phase phase);\n")
             file.write("    super.build_phase(phase);\n")
             #// component creation
             #compA = mycomponent::type_id::create("compA", this); 
             #compB = param_component #(8, 1)::type_id::create("compB", this); 
             file.write("  endfunction\n\n")
         if(C86.instate(['selected'])):
             file.write("  task run_phase(uvm_phase phase);\n\n")
             file.write("  endtask")
         if(C109.instate(['selected'])):
             file.write("  virtual task body();\n")
             file.write("    req = mem_seq_item::type_id::create('req');\n")
             file.write("    wait_for_grant();\n")
             file.write("    assert(req.randomize());\n")                    
             file.write("    send_request(req);\n")
             file.write("    wait_for_item_done();\n")
             file.write("    get_response(rsp);\n")
             file.write("  endtask")

         file.write("\n\n\n"+"endclass")

         print("Generated the sequence class")
  if(e10.get()):
     with open("uvm_hierarchy_files/"+e10.get()+".sv", "w") as file:
         file.write("class "+e10.get()+" extends uvm_scoreboard;"+"\n\n")
         file.write("  `uvm_component_utils("+e10.get()+")\n\n")
         if(C91.instate(['selected'])):
             file.write("  function new(string name = "+e10.get()+", uvm_component parent = null);\n")
             file.write("    super.new(name, parent);\n")
             file.write("  endfunction\n\n")
         if(C92.instate(['selected'])):
             file.write("  function void build_phase(uvm_phase phase);\n")
             file.write("    super.build_phase(phase);\n")
             #// component creation
             #compA = mycomponent::type_id::create("compA", this); 
             #compB = param_component #(8, 1)::type_id::create("compB", this); 
             file.write("  endfunction\n\n")
         if(C96.instate(['selected'])):
             file.write("  task run_phase(uvm_phase phase);\n\n")
             file.write("  endtask")

         file.write("\n\n\n"+"endclass")

         print("Generated the scoreboard class")

#CheckVar1 = IntVar()

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
l1.grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
l2.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

l3.grid(row = 2, column = 0, sticky = W, padx = 10, pady = 10)
l4.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 10)

l5.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 10)
l6.grid(row = 5, column = 0, sticky = W, padx = 10, pady = 10)

l7.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 10)
l8.grid(row = 7, column = 0, sticky = W, padx = 10, pady = 10)

l9.grid(row = 8, column = 0, sticky = W, padx = 10, pady = 10)
l10.grid(row = 9, column = 0, sticky = W, padx = 10, pady = 10)

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
e1.grid(row = 0, column = 1, pady = 10)
e2.grid(row = 1, column = 1, pady = 10)

e3.grid(row = 2, column = 1, pady = 10)
e4.grid(row = 3, column = 1, pady = 10)
e5.grid(row = 4, column = 1, pady = 10)
e6.grid(row = 5, column = 1, pady = 10)
e7.grid(row = 6, column = 1, pady = 10)
e8.grid(row = 7, column = 1, pady = 10)
e9.grid(row = 8, column = 1, pady = 10)
e10.grid(row = 9, column = 1, pady = 10)

check_box_list = []

#sbmitbtn = Button(master, text = "Generate", command = OnClick_Submit).place(x = 350, y = 200)

#button0 = Button(master, text ="Reset Checkbox", command = clear, cursor="hand2")
#button0.grid(row = 10, column = 0,  padx = 10, pady = 10)

button1 = Button(master, text ="Reset", command = clear, cursor="hand2")
button1.grid(row = 10, column = 0,  padx = 10, pady = 10)

button2 = Button(master, text ="Generate", command = OnClick_Submit, cursor="hand2")
button2.grid(row = 10, column = 1, padx = 10, pady = 10)

button3 = Button(master, text ="Quit", command = master.destroy, cursor="hand2")
button3.grid(column=0, row = 11, columnspan=2, sticky = W+E, padx = 10, pady = 10)

button4 = Button(master, text='Uncheck All', command = uncheck_all, cursor="hand2")
button4.grid(column=6, row=10, padx=10, pady=10)

button5 = Button(master, text='Check All', command = check_all, cursor="hand2")
button5.grid(column=7, row=10, padx=10, pady=10)

# Create four checkbuttons inside the frame
C1 = Checkbutton(master, text="new", cursor="hand2") #, variable = CheckVar1)
C1.grid(column=2, row=0, padx=10, pady=10)

C2 = Checkbutton(master, text = "build", cursor="hand2")
C2.grid(column=3, row=0, padx=10, pady=10)

C3 = Checkbutton(master, text = "connect", cursor="hand2")
C3.grid(column=4, row=0, padx=10, pady=10)

C4 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C4.grid(column=5, row=0, padx=10, pady=10)

C5 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C5.grid(column=6, row=0, padx=10, pady=10)

C6 = Checkbutton(master, text = "run", cursor="hand2")
C6.grid(column=7, row=0, padx=10, pady=10)

C7 = Checkbutton(master, text = "extract", cursor="hand2")
C7.grid(column=8, row=0, padx=10, pady=10)

C8 = Checkbutton(master, text = "check", cursor="hand2")
C8.grid(column=9, row=0, padx=10, pady=10)

C9 = Checkbutton(master, text = "report", cursor="hand2")
C9.grid(column=10, row=0, padx=10, pady=10)

C10 = Checkbutton(master, text = "final", cursor="hand2")
C10.grid(column=11, row=0, padx=10, pady=10)

C101 = Checkbutton(master, text = "task body", cursor="hand2")
C101.grid(column=12, row=0, padx=10, pady=10)

C11 = Checkbutton(master, text="new", cursor="hand2")
C11.grid(column=2, row=1, padx=10, pady=10)

C12 = Checkbutton(master, text = "build", cursor="hand2")
C12.grid(column=3, row=1, padx=10, pady=10)

C13 = Checkbutton(master, text = "connect", cursor="hand2")
C13.grid(column=4, row=1, padx=10, pady=10)

C14 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C14.grid(column=5, row=1, padx=10, pady=10)

C15 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C15.grid(column=6, row=1, padx=10, pady=10)

C16 = Checkbutton(master, text = "run", cursor="hand2")
C16.grid(column=7, row=1, padx=10, pady=10)

C17 = Checkbutton(master, text = "extract", cursor="hand2")
C17.grid(column=8, row=1, padx=10, pady=10)

C18 = Checkbutton(master, text = "check", cursor="hand2")
C18.grid(column=9, row=1, padx=10, pady=10)

C19 = Checkbutton(master, text = "report", cursor="hand2")
C19.grid(column=10, row=1, padx=10, pady=10)

C20 = Checkbutton(master, text = "final", cursor="hand2")
C20.grid(column=11, row=1, padx=10, pady=10)

C102 = Checkbutton(master, text = "task body", cursor="hand2")
C102.grid(column=12, row=1, padx=10, pady=10)

C21 = Checkbutton(master, text="clocking block", cursor="hand2")
C21.grid(column=3, row=2, padx=10, pady=10)

C22 = Checkbutton(master, text = "modport", cursor="hand2")
C22.grid(column=4, row=2, padx=10, pady=10)

'''
C23 = Checkbutton(master, text = "connect", cursor="hand2")
C23.grid(column=4, row=2, padx=10, pady=10)

C24 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C24.grid(column=5, row=2, padx=10, pady=10)

C25 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C25.grid(column=6, row=2, padx=10, pady=10)

C26 = Checkbutton(master, text = "run", cursor="hand2")
C26.grid(column=7, row=2, padx=10, pady=10)

C27 = Checkbutton(master, text = "extract", cursor="hand2")
C27.grid(column=8, row=2, padx=10, pady=10)

C28 = Checkbutton(master, text = "check", cursor="hand2")
C28.grid(column=9, row=2, padx=10, pady=10)

C29 = Checkbutton(master, text = "report", cursor="hand2")
C29.grid(column=10, row=2, padx=10, pady=10)

C30 = Checkbutton(master, text = "final", cursor="hand2")
C30.grid(column=11, row=2, padx=10, pady=10)

C103 = Checkbutton(master, text = "task body", cursor="hand2")
C103.grid(column=12, row=2, padx=10, pady=10)
'''

C31 = Checkbutton(master, text="new", cursor="hand2")
C31.grid(column=2, row=3, padx=10, pady=10)

C32 = Checkbutton(master, text = "build", cursor="hand2")
C32.grid(column=3, row=3, padx=10, pady=10)

C33 = Checkbutton(master, text = "connect", cursor="hand2")
C33.grid(column=4, row=3, padx=10, pady=10)

C34 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C34.grid(column=5, row=3, padx=10, pady=10)

C35 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C35.grid(column=6, row=3, padx=10, pady=10)

C36 = Checkbutton(master, text = "run", cursor="hand2")
C36.grid(column=7, row=3, padx=10, pady=10)

C37 = Checkbutton(master, text = "extract", cursor="hand2")
C37.grid(column=8, row=3, padx=10, pady=10)

C38 = Checkbutton(master, text = "check", cursor="hand2")
C38.grid(column=9, row=3, padx=10, pady=10)

C39 = Checkbutton(master, text = "report", cursor="hand2")
C39.grid(column=10, row=3, padx=10, pady=10)

C40 = Checkbutton(master, text = "final", cursor="hand2")
C40.grid(column=11, row=3, padx=10, pady=10)

C104 = Checkbutton(master, text = "task body", cursor="hand2")
C104.grid(column=12, row=3, padx=10, pady=10)

C41 = Checkbutton(master, text="new", cursor="hand2")
C41.grid(column=2, row=4, padx=10, pady=10)

C42 = Checkbutton(master, text = "build", cursor="hand2")
C42.grid(column=3, row=4, padx=10, pady=10)

C43 = Checkbutton(master, text = "connect", cursor="hand2")
C43.grid(column=4, row=4, padx=10, pady=10)

C44 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C44.grid(column=5, row=4, padx=10, pady=10)

C45 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C45.grid(column=6, row=4, padx=10, pady=10)

C46 = Checkbutton(master, text = "run", cursor="hand2")
C46.grid(column=7, row=4, padx=10, pady=10)

C47 = Checkbutton(master, text = "extract", cursor="hand2")
C47.grid(column=8, row=4, padx=10, pady=10)

C48 = Checkbutton(master, text = "check", cursor="hand2")
C48.grid(column=9, row=4, padx=10, pady=10)

C49 = Checkbutton(master, text = "report", cursor="hand2")
C49.grid(column=10, row=4, padx=10, pady=10)

C50 = Checkbutton(master, text = "final", cursor="hand2")
C50.grid(column=11, row=4, padx=10, pady=10)

C105 = Checkbutton(master, text = "task body", cursor="hand2")
C105.grid(column=12, row=4, padx=10, pady=10)

C51 = Checkbutton(master, text="new", cursor="hand2")
C51.grid(column=2, row=5, padx=10, pady=10)

C52 = Checkbutton(master, text = "build", cursor="hand2")
C52.grid(column=3, row=5, padx=10, pady=10)

C53 = Checkbutton(master, text = "connect", cursor="hand2")
C53.grid(column=4, row=5, padx=10, pady=10)

C54 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C54.grid(column=5, row=5, padx=10, pady=10)

C55 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C55.grid(column=6, row=5, padx=10, pady=10)

C56 = Checkbutton(master, text = "run", cursor="hand2")
C56.grid(column=7, row=5, padx=10, pady=10)

C57 = Checkbutton(master, text = "extract", cursor="hand2")
C57.grid(column=8, row=5, padx=10, pady=10)

C58 = Checkbutton(master, text = "check", cursor="hand2")
C58.grid(column=9, row=5, padx=10, pady=10)

C59 = Checkbutton(master, text = "report", cursor="hand2")
C59.grid(column=10, row=5, padx=10, pady=10)

C60 = Checkbutton(master, text = "final", cursor="hand2")
C60.grid(column=11, row=5, padx=10, pady=10)

C106 = Checkbutton(master, text = "task body", cursor="hand2")
C106.grid(column=12, row=5, padx=10, pady=10)

C61 = Checkbutton(master, text="new", cursor="hand2")
C61.grid(column=2, row=6, padx=10, pady=10)

C62 = Checkbutton(master, text = "build", cursor="hand2")
C62.grid(column=3, row=6, padx=10, pady=10)

C63 = Checkbutton(master, text = "connect", cursor="hand2")
C63.grid(column=4, row=6, padx=10, pady=10)

C64 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C64.grid(column=5, row=6, padx=10, pady=10)

C65 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C65.grid(column=6, row=6, padx=10, pady=10)

C66 = Checkbutton(master, text = "run", cursor="hand2")
C66.grid(column=7, row=6, padx=10, pady=10)

C67 = Checkbutton(master, text = "extract", cursor="hand2")
C67.grid(column=8, row=6, padx=10, pady=10)

C68 = Checkbutton(master, text = "check", cursor="hand2")
C68.grid(column=9, row=6, padx=10, pady=10)

C69 = Checkbutton(master, text = "report", cursor="hand2")
C69.grid(column=10, row=6, padx=10, pady=10)

C70 = Checkbutton(master, text = "final", cursor="hand2")
C70.grid(column=11, row=6, padx=10, pady=10)

C107 = Checkbutton(master, text = "task body", cursor="hand2")
C107.grid(column=12, row=6, padx=10, pady=10)

C71 = Checkbutton(master, text="new", cursor="hand2")
C71.grid(column=2, row=7, padx=10, pady=10)

C72 = Checkbutton(master, text = "build", cursor="hand2")
C72.grid(column=3, row=7, padx=10, pady=10)

C73 = Checkbutton(master, text = "connect", cursor="hand2")
C73.grid(column=4, row=7, padx=10, pady=10)

C74 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C74.grid(column=5, row=7, padx=10, pady=10)

C75 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C75.grid(column=6, row=7, padx=10, pady=10)

C76 = Checkbutton(master, text = "run", cursor="hand2")
C76.grid(column=7, row=7, padx=10, pady=10)

C77 = Checkbutton(master, text = "extract", cursor="hand2")
C77.grid(column=8, row=7, padx=10, pady=10)

C78 = Checkbutton(master, text = "check", cursor="hand2")
C78.grid(column=9, row=7, padx=10, pady=10)

C79 = Checkbutton(master, text = "report", cursor="hand2")
C79.grid(column=10, row=7, padx=10, pady=10)

C80 = Checkbutton(master, text = "final", cursor="hand2")
C80.grid(column=11, row=7, padx=10, pady=10)

C108 = Checkbutton(master, text = "task body", cursor="hand2")
C108.grid(column=12, row=7, padx=10, pady=10)

C81 = Checkbutton(master, text="new", cursor="hand2")
C81.grid(column=2, row=8, padx=10, pady=10)

C82 = Checkbutton(master, text = "build", cursor="hand2")
C82.grid(column=3, row=8, padx=10, pady=10)

C83 = Checkbutton(master, text = "connect", cursor="hand2")
C83.grid(column=4, row=8, padx=10, pady=10)

C84 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C84.grid(column=5, row=8, padx=10, pady=10)

C85 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C85.grid(column=6, row=8, padx=10, pady=10)

C86 = Checkbutton(master, text = "run", cursor="hand2")
C86.grid(column=7, row=8, padx=10, pady=10)

C87 = Checkbutton(master, text = "extract", cursor="hand2")
C87.grid(column=8, row=8, padx=10, pady=10)

C88 = Checkbutton(master, text = "check", cursor="hand2")
C88.grid(column=9, row=8, padx=10, pady=10)

C89 = Checkbutton(master, text = "report", cursor="hand2")
C89.grid(column=10, row=8, padx=10, pady=10)

C90 = Checkbutton(master, text = "final", cursor="hand2")
C90.grid(column=11, row=8, padx=10, pady=10)

C109 = Checkbutton(master, text = "task body", cursor="hand2")
C109.grid(column=12, row=8, padx=10, pady=10)

C91 = Checkbutton(master, text="new", cursor="hand2")
C91.grid(column=2, row=9, padx=10, pady=10)

C92 = Checkbutton(master, text = "build", cursor="hand2")
C92.grid(column=3, row=9, padx=10, pady=10)

C93 = Checkbutton(master, text = "connect", cursor="hand2")
C93.grid(column=4, row=9, padx=10, pady=10)

C94 = Checkbutton(master, text = "end_of_elaboration", cursor="hand2")
C94.grid(column=5, row=9, padx=10, pady=10)

C95 = Checkbutton(master, text = "start_of_simulation", cursor="hand2")
C95.grid(column=6, row=9, padx=10, pady=10)

C96 = Checkbutton(master, text = "run", cursor="hand2")
C96.grid(column=7, row=9, padx=10, pady=10)

C97 = Checkbutton(master, text = "extract", cursor="hand2")
C97.grid(column=8, row=9, padx=10, pady=10)

C98 = Checkbutton(master, text = "check", cursor="hand2")
C98.grid(column=9, row=9, padx=10, pady=10)

C99 = Checkbutton(master, text = "report", cursor="hand2")
C99.grid(column=10, row=9, padx=10, pady=10)

C100 = Checkbutton(master, text = "final", cursor="hand2")
C100.grid(column=11, row=9, padx=10, pady=10)

C110 = Checkbutton(master, text = "task body", cursor="hand2")
C110.grid(column=12, row=9, padx=10, pady=10)

check_box_list.append(C1)  # add checkbutton
check_box_list.append(C2)
check_box_list.append(C3)
check_box_list.append(C4)
check_box_list.append(C5)
check_box_list.append(C6)
check_box_list.append(C7)
check_box_list.append(C8)
check_box_list.append(C9)
check_box_list.append(C10)
check_box_list.append(C11)
check_box_list.append(C12)
check_box_list.append(C13)
check_box_list.append(C14)
check_box_list.append(C15)
check_box_list.append(C16)
check_box_list.append(C17)
check_box_list.append(C18)
check_box_list.append(C19)
check_box_list.append(C20)
check_box_list.append(C21)
check_box_list.append(C22)
'''
check_box_list.append(C23)
check_box_list.append(C24)
check_box_list.append(C25)
check_box_list.append(C26)  # add checkbutton
check_box_list.append(C27)
check_box_list.append(C28)
check_box_list.append(C29)
check_box_list.append(C30)
'''
check_box_list.append(C31)
check_box_list.append(C32)
check_box_list.append(C33)
check_box_list.append(C34)
check_box_list.append(C35)
check_box_list.append(C36)
check_box_list.append(C37)
check_box_list.append(C38)
check_box_list.append(C39)
check_box_list.append(C40)
check_box_list.append(C41)
check_box_list.append(C42)
check_box_list.append(C43)
check_box_list.append(C44)
check_box_list.append(C45)
check_box_list.append(C46)
check_box_list.append(C47)
check_box_list.append(C48)
check_box_list.append(C49)
check_box_list.append(C50)
check_box_list.append(C51)  # add checkbutton
check_box_list.append(C52)
check_box_list.append(C53)
check_box_list.append(C54)
check_box_list.append(C55)
check_box_list.append(C56)
check_box_list.append(C57)
check_box_list.append(C58)
check_box_list.append(C59)
check_box_list.append(C60)
check_box_list.append(C61)
check_box_list.append(C62)
check_box_list.append(C63)
check_box_list.append(C64)
check_box_list.append(C65)
check_box_list.append(C66)
check_box_list.append(C67)
check_box_list.append(C68)
check_box_list.append(C69)
check_box_list.append(C70)
check_box_list.append(C71)
check_box_list.append(C72)
check_box_list.append(C73)
check_box_list.append(C74)
check_box_list.append(C75)
check_box_list.append(C76)  # add checkbutton
check_box_list.append(C77)
check_box_list.append(C78)
check_box_list.append(C79)
check_box_list.append(C80)
check_box_list.append(C81)
check_box_list.append(C82)
check_box_list.append(C83)
check_box_list.append(C84)
check_box_list.append(C85)
check_box_list.append(C86)
check_box_list.append(C87)
check_box_list.append(C88)
check_box_list.append(C89)
check_box_list.append(C90)
check_box_list.append(C91)
check_box_list.append(C92)
check_box_list.append(C93)
check_box_list.append(C94)
check_box_list.append(C95)
check_box_list.append(C96)
check_box_list.append(C97)
check_box_list.append(C98)
check_box_list.append(C99)
check_box_list.append(C100)
check_box_list.append(C101)
check_box_list.append(C102)
#check_box_list.append(C103)
check_box_list.append(C104)
check_box_list.append(C105)
check_box_list.append(C106)
check_box_list.append(C107)
check_box_list.append(C108)
check_box_list.append(C109)
check_box_list.append(C110)

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

#print("val1: ", val1, "\ne1: ", e1.get())

#f = open("user.txt", "w") 
#f.write("Test Class Name: %s\nEnvironment Class Name: %s" % (e1.get(), e2.get())) 
#f.close()

#dict1 = {"Test Class Name": val1, "Environment Class Name": val2, "Interface Name": val3, "Agent Name": val4, "Monitor Name": val5, "Driver Name": val6, "Sequencer Name": val7, "Sequence Item Name": val8, "Sequence Name": val9, "Scoreboard Name": val10}

#str1 = '"Test Class Name": val1, "Environment Class Name": val2, "Interface Name": val3, "Agent Name": val4, "Monitor Name": val5, "Driver Name": val6, "Sequencer Name": val7, "Sequence Item Name": val8, "Sequence Name": val9, "Scoreboard Name": val10'

#save_dict_to_file(dict1)

# display Menu 
master.config(menu = menubar) 

#with open("user.txt", 'w') as f: 
#    for classes, names in dict.items():
#        #print(classes, ":", names)
#        f.write('%s:%s\n' % (classes, names))

#with open("user.txt", 'w') as f:  
#    for key, value in dict.items():  
#        f.write('%s:%s\n' % (key, value))    
#f.close() 

# label 
#ttk.Label(master, text = "Select the Month :", 
#          font = ("Times New Roman", 10)).grid(column = 0, 
#          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
#n = tk.StringVar() 
#monthchoosen1 = ttk.Combobox(master, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
#monthchoosen1['values'] = (' build',  
#                          ' connect', 
#                          ' end_of_elaboration', 
#                          ' start_of_simulation', 
#                          ' run', 
#                          ' extract', 
#                          ' check', 
#                          ' report', 
#                          ' final') 
  
#monthchoosen1.grid(column = 3, row = 0, padx = 10, pady = 10)
#print(monthchoosen1.get())
#monthchoosen1.current() 

# Combobox creation 
#n = tk.StringVar() 
#monthchoosen2 = ttk.Combobox(master, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
#monthchoosen2['values'] = (' build',  
#                          ' connect', 
#                          ' end_of_elaboration', 
#                          ' start_of_simulation', 
#                          ' run', 
#                          ' extract', 
#                          ' check', 
#                          ' report', 
#                          ' final') 
  
#monthchoosen2.grid(column = , row = 0, padx = 10, pady = 10)
#print(monthchoosen2.get())
#monthchoosen2.current()

center_window_geometry(master)

#print_all()
# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()
