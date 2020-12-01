import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

class MlPlayerApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.draw_gui()

    def draw_gui(self):
        
        self.name_label = tk.Label(self.master, text="Name:",bg = "Light Blue")
        self.name_label.grid(row=0,column=0)

        self.name_entry = tk.Entry(self.master,width = 80)
        self.name_entry.grid(row=0,column=1)

        self.ignNumber_label = tk.Label(self.master, text="IGN:",bg = "Light Blue")
        self.ignNumber_label.grid(row=1, column=0)
        self.ignNumber_entry = tk.Entry(self.master, width = 80)
        self.ignNumber_entry.grid(row=1, column=1)

        self.agenumber_label = tk.Label(self.master, text="Age:", bg = "Light Blue")
        self.agenumber_label.grid(row=2, column=0)
        self.agenumber_entry = tk.Entry(self.master,width = 80)
        self.agenumber_entry.grid(row=2, column=1)
        
        self.location_label = tk.Label(self.master, text="Location:", bg = "Light Blue")
        self.location_label.grid(row=3, column=0)
        self.location_entry = tk.Entry(self.master,width = 80)
        self.location_entry.grid(row=3, column=1)

        self.submit_button = tk.Button(self.master,width = 22,height =2, text="Insert", command=self.InsertInfo)
        self.submit_button.grid(row=2, column=3, rowspan = 2)

        self.exit_button = tk.Button(self.master,width = 22,height =2, text="Exit", command=self.master.destroy)
        self.exit_button.grid(row=6, column=3,rowspan = 2)
        
        self.tree = ttk.Treeview(self.master, columns=('Name', 'IGN', 'ID', 'Location'))
        self.tree.delete(*self.tree.get_children())  

        #heading
        self.tree.heading('#0', text='Player')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='IGN')
        self.tree.heading('#3', text='Age')
        self.tree.heading('#4', text='Location')

        #column
        self.tree.column('#0', width = 140,stretch=NO)
        self.tree.column('#1', width = 140,stretch=NO)
        self.tree.column('#2', width = 140,stretch=NO)
        self.tree.column('#3', width = 140,stretch=NO)
        self.tree.column('#4', width = 140,stretch=NO)

        self.tree.grid(row=5, column = 0,columnspan=300)
        self.treeview = self.tree

        self.id = 0
        self.iid = 0
        self.iiid = 0
        self.iiiid = 0

    def InsertInfo(self):
        self.treeview.insert('', 'end', iid=self.iid, text="player" + str(self.id),
                             values=(str(self.name_entry.get()),
                                     self.ignNumber_entry.get(), self.agenumber_entry.get(), self.location_entry.get()))
        self.iid = self.iid + 1
        self.id = self.id + 1
        self.iiid = self.iid + 1
        self.iiiid = self.iid + 1
    def treeDel(self):        
    #self.tree.delete()
        self.tree.destroy()
        self.treeFill()

        self.tree_destroy = tk.Button(self.master, width=5, height=1,text="Reset",relief=FLAT,bg="gray",command = self.tree.destroy) 
        self.tree_destroy.grid(row=7, column=3,rowspan = 2)
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x350")
    root.title("ML Player Application")
    root.config(bg="Light Blue")
    root.resizable(False,False)
    MlPlayerApplication(root).place()
    root.mainloop()
    

        
        
        
