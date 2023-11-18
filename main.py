import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    # try:
    ytlink = link.get()
    ytobj = YouTube(ytlink)
    video = ytobj.streams.get_highest_resolution()
    video.download()
    # except:
    #     print('YouTube link is invalid')
    
    print("Download complete")

# System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, placeholder_text="youtube.com/watch/")
link.pack()

# Dowload Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady = 10)


# Run app
app.mainloop()
