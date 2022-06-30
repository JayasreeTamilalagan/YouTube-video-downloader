import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


def Download():

	Youtube_link = vlink.get()
	downFolder = downPath.get()

	getVideo = YouTube(Youtube_link)

	video = getVideo.streams.first()
	video.download(downFolder)

	messagebox.showinfo("DOWNLOADED SUCCESSFULLY", "FIND THE VIDEO IN\n" + downFolder)
	
def gui_info():
	main_title = Label(master, text="Start downloading YouTube videos now!", padx=10, pady=10, font="TimesNewRoman 14 bold", bg="slategray1", fg="blue")
	main_title.grid(row=1, column=1, pady=10, padx=0, columnspan=3)

	link_input = Label(master, text="Paste the link here :", bg="pink", pady=5, padx=5)
	link_input.grid(row=2, column=0, pady=5, padx=5)
	master.textlink = Entry(master, width=35, textvariable=vlink, font="TimesNewRoman 14 bold")
	master.textlink.grid(row=2, column=1, pady=5, padx=5, columnspan=2)


	location_input = Label(master, text="Destination :", bg="pink", pady=5, padx=9)
	location_input.grid(row=3, column=0, pady=5, padx=5)
	master.textlocation = Entry(master, width=27, textvariable=downPath, font="TimesNewRoman 14 bold")
	master.textlocation.grid(row=3, column=1, pady=5, padx=5)

	browse_button = Button(master, text="Browse", command=Browse, width=10, bg="aquamarine1", relief=GROOVE)
	browse_button.grid(row=3, column=2, pady=1, padx=1)

	download_button = Button(master, text="Download Video", command=Download, width=20, bg="aquamarine4", pady=10, padx=15, relief=GROOVE, font="TimesNewRoman 13 bold")
	download_button.grid(row=4, column=1, pady=20, padx=20)

def Browse():
	downDirectory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video in")
	downPath.set(downDirectory)


master = tk.Tk()

master.geometry("535x280")
master.resizable(False, False)
master.title("Free YouTube Video Downloader")
master.config(background="slategray1")

vlink = StringVar()
downPath = StringVar()

gui_info()

master.mainloop()

