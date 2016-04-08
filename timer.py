from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

class Application(Frame):
	def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.pack()
        self.createWidgets()
        
        # TODO: Add time tracking functionality 

    def createWidgets(self):
        self.now = tk.StringVar()
        self.time = tk.Label(self, font=('Helvetica', 24))
        self.time.pack(side="top")
        self.time["textvariable"] = self.now

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

        # initial time display
        self.onUpdate()

    # TODO: Add method to calculate next time out for break

    def onUpdate(self):
        # TODO: Initialize timeout variable if not set
        
        nTime = time.localtime()
        curTime = time.strftime("%H:%M:%S", nTime)
        min = int(time.strftime("%M", nTime))
        
        if min >= self.nextTimeOut:
            # Send Alert to take a work break
            messagebox.showinfo("Title","Alert!")
            # TODO: Call update timeout method
        
        # update displayed time
        self.now.set(current_iso8601())
        # schedule timer to call myself after 1 second
        self.after(1000, self.onUpdate)

root = tk.Tk()
app = Application(master=root)
root.mainloop()
