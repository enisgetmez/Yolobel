from tkinter import *
from tkinter import filedialog
from yolobel import enums
from yolobel import processing


def openfile():
	global input_file_txt
	filepath = filedialog.askopenfilename(title="Select Video File",filetypes=(("Video Files",".mp4 .avi .wmv"),))
	enums.input_vid = filepath
	input_file_txt.delete("1.0", END)
	input_file_txt.insert(END,enums.input_vid)

def draw():
	enums.draw=True

def savefile():
	global save_file_txt
	savepath = filedialog.askdirectory(title="Select Directory")
	enums.out_directory = savepath
	save_file_txt.delete("1.0", END)
	save_file_txt.insert(END,enums.out_directory)

def run_video():
	global input_file_txt
	global save_file_txt
	global out_name_txt
	try:
		enums.input_vid = int(input_file_txt.get("1.0",END).replace("\n",""))
	except:
		enums.input_vid = str(input_file_txt.get("1.0",END).replace("\n",""))
	enums.out_directory = str(save_file_txt.get("1.0",END)).replace("\n","")
	enums.out_name = str(out_name_txt.get("1.0",END)).replace("\n","")
	processing.video_proc(enums.input_vid)


def register_window():
	register = Tk()
	register.title("Configuration")
	register.geometry("400x350")

########################open########################
	label = Label(register,text="Video file or camera port")
	label.pack()
	label.place(x=5,y=5)

	global input_file_txt
	input_file_txt = Text(width = 50,height = 1)
	input_file_txt.insert(END,enums.input_vid)
	input_file_txt.pack()
	input_file_txt.place(x =5,y=30)

	select_file_btn = Button(text = "Select file",command=openfile,width=53,height=1)
	select_file_btn.pack()
	select_file_btn.place(x=5,y=60)

########################Save########################
	label2 = Label(register,text="Save Directory")
	label2.pack()
	label2.place(x=5,y=90)

	global save_file_txt
	save_file_txt = Text(width = 50,height = 1)
	save_file_txt.pack()
	save_file_txt.place(x =5,y=120)

	save_file_btn = Button(text = "Select save directory",command=savefile,width=53,height=1)
	save_file_btn.pack()
	save_file_btn.place(x=5,y=160)
########################Run########################

	label3 = Label(register,text="Out Name")
	label3.pack()
	label3.place(x=5,y=190)

	global out_name_txt
	out_name_txt = Text(width = 50,height = 1)
	out_name_txt.pack()
	out_name_txt.place(x =5,y=220)

	run_btn = Button(text = "Run!",command=run_video,width=53,height=1)
	run_btn.pack()
	run_btn.place(x=5,y=260)

	info_label = Label(register,text="After pressing the 'run' button, press the esc key to make a selection.")
	info_label.pack()
	info_label.place(x=5,y=290)

	register.mainloop()