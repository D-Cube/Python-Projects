import tkinter as ttk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

# tkinter widgets


def Widgets():

    linkLabel = Label(root, text="Youtube Link :  ", bg="#f5ffff")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=55, textvariable=videoLink)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    destinationLabel = Label(root, text="Destionation :  ", bg="#f5ffff")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)
    
    root.destinationText = Entry(root, width = 40, textvariable = downloadPath)
    root.destinationText.grid(row = 2, column = 1, pady = 5, padx = 5)

    browseButton = ttk.Button(root, text="Browse", command = Browse, width=10, bg="#05E8E0")
    browseButton.grid(row=2, column=2, padx=1, pady=1)

    downloadButton = ttk.Button(root, text="Download", command=Download, width = 0, bg="#05E8E0")
    downloadButton.grid(row=3, column=1, pady=3, padx=3)

# browse function


def Browse():

    # pop-up to choose directory
    downloadDirectory = filedialog.askdirectory(initialdir="C:\\Users\\siddh\\Downloads\\youtube_video_downloads")
    # display directory in directory text box
    downloadPath.set(downloadDirectory)

# download function


def Download():

    # user input link
    youtubeLink = videoLink.get()
    # optimal location for saving file
    downloadFolder = downloadPath.get()
    # YouTube() object
    getVideo = YouTube(youtubeLink)
    # get all available streams of the video and select first
    videoStream = getVideo.streams.first()
    videoStream.download(downloadFolder)
    messagebox.showinfo("Done!", "Downloaded and saved in : " + downloadFolder)


# object of tk class
root = ttk.Tk()
root.geometry("600x120")
root.resizable(False, False)
root.title("Youtube_Video_Downloader")
root.config(background="#ffffff")

videoLink = StringVar()
downloadPath = StringVar()

Widgets()
# defining infinite loop to run the application
root.mainloop()
