import os
import patoolib
from tkinter import *
from tkinter.filedialog import askopenfilename

filename = ""
status = ""
def DisplayDir():
	global status
	status = ""
	stats.configure(text=status)
	global filename
	filename = askopenfilename(initialdir="/",filetypes =(("Rar Files","*.rar"),("All Files","*.*")),title = "Choose a file.")
	name.insert(INSERT,filename)
"""	except Exception as e:
	status += "File Not Found"
	stats.configure(text=status)"""
def start():
	global status
	out = ""
	outdir = os.path.dirname(os.path.abspath(filename))
	tout = os.path.basename(filename)
	for x in range(0,len(tout)-4):
		out += tout[x]
	out = os.path.join(outdir,out)
	if not os.path.exists(out):
		os.makedirs(out)
	patoolib.extract_archive(filename, outdir=out)
	status += "Finished !\n"
	stats.configure(text=status)
	status += "Extrated file is saved in : \n"+out
	stats.configure(text=status)

root = Tk()
root.title("My UnRar")
root.geometry('{}x{}'.format(550, 300))
root.resizable(width=False, height=False)
file = Label(root, text="Choose File : ")
name = Entry(root,bd=2)
selectfile = Button(root, text ="Browse", command = DisplayDir, foreground="white", background="#ff661a")
start = Button(root, text ="Start Process!", command = start, foreground="white", background="#ff661a")
stats = Label(root, text=status)
credits = Label(root, text ="Made by Surya.S",bg="#ff661a", fg="white",width=700)



file.place(relx=0.36, rely=0.3, anchor="c")
name.place(relx=0.6, rely=0.3, anchor="c")
selectfile.place(relx=0.85, rely=0.3, anchor="c")
start.place(relx=0.4, rely=0.5, anchor="c")
stats.place(relx=0.4, rely=0.7, anchor="c")
credits.place(relx=0.5, rely=0.99, anchor="s")
root.mainloop()