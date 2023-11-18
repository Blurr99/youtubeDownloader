import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()
        ytobj = YouTube(ytlink, use_oauth=True,
            allow_oauth_cache=True, on_progress_callback=on_progress)
        video = ytobj.streams.get_highest_resolution()

        title.configure(text = ytobj.title, text_color = "white")
        finishedLabel.configure(text = "")
        video.download()
        finishedLabel.configure(text = "Finished Downloading!", text_color = "green")
    except:
        finishedLabel.configure(text = "Download Error", text_color = "red")
    

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text= per+"%")
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)

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

finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack(padx = 10, pady = 10)

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400, corner_radius=10, progress_color="green")
progressBar.set(0)
progressBar.pack(padx = 10, pady = 10)

# Dowload Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady = 10)


# Run app
app.mainloop()
