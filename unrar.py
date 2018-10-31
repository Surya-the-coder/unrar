import os
import sys
import patoolib
import subprocess

# Checking python version

if sys.version_info[0] < 3:
	from Tkinter import *
	from tkFileDialog import askopenfilename
else:
	from tkinter import *
	from tkinter.filedialog import askopenfilename

filename = ""
status = ""
def DisplayDir():
	global status
	status = ""
	stats.configure(text=status)
	global filename
	filename = askopenfilename(initialdir="/Users/surya/Desktop/Entertainment",filetypes =(("Rar Files","*.rar"),("Zip Files","*.zip"),("All Files","*.*")),title = "Choose a file.")
	name.configure(text=filename)
	status += "File Selected !\n"
	stats.configure(text=status)
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
name = Label(root, text=filename)
selectfile = Button(root, text ="Choose File", command = DisplayDir, background="#ff661a")
start = Button(root, text ="Start Process!", command = start, background="#ff661a")
stats = Label(root, text=status)
credits = Label(root, text ="Made by Surya.S",bg="#ff661a", fg="white",width=700)


name.place(relx=0.33, rely=0.4, anchor="c")
selectfile.place(relx=0.3, rely=0.3, anchor="c")
start.place(relx=0.3, rely=0.5, anchor="c")
stats.place(relx=0.3, rely=0.7, anchor="c")
credits.place(relx=0.5, rely=0.99, anchor="s")
root.mainloop()
