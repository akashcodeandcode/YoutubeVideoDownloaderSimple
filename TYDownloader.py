from tkinter import *
from tkinter import ttk, messagebox
from pytube import YouTube
import _thread

storagePath = "D:\AkYt"

root = Tk()
root.geometry("500x350")
root.title("AK YT Downloader")
root.resizable(0, 0)


def showProgress(stream, chunk, bytes_remaining):
    progress = int(((stream.filesize - bytes_remaining) / stream.filesize) * 100)
    p_bar['value'] = progress


# Download Function
def download():
    quality = ytQuality.get()
    url = link.get()
    if len(url) > 0:
        msg["text"] = "Extracting Video..."
        yt_url = YouTube(url, on_progress_callback=showProgress)
        video = yt_url.streams.filter(progressive=True, file_extension='mp4').order_by("resolution").desc()
        msg["text"] = "Downloading..." + yt_url.title

        if quality == choices[0]:
            video.last().download(storagePath)
        else:
            video.first().download(storagePath)
        msg["text"] = "Downloaded Successfully!!!"
        messagebox.showinfo("Download info", "Downloaded Successfully!!! and Saved in  \n" + storagePath)

    else:
        urlErr["text"] = "Paste your link here..."


# Header
lbl = Label(root, text="Ak YT Downloader", font='arial 20 bold')
lbl.pack()
# URL Section
lblUrl = Label(root, font='arial 13 bold')
lblUrl.pack()

link = StringVar()
urlEntry = Entry(root, textvariable=link, width=70)
urlEntry.pack()
# URL Error
urlErr = Label(root, text="Please enter the url", font="arial 12", fg="red")
urlErr.pack()
# Quality
lblQuality = Label(root, text="Select Quality:",  font="arial 12 bold")
lblQuality.pack(pady=10)

choices = ["low", "high"]
ytQuality = ttk.Combobox(root, values=choices)
ytQuality.pack()

# ProgressBar
p_bar = ttk.Progressbar(root, length=350)
p_bar.pack(pady=10)

# Message
msg = Label(root, font="arial 12", fg="green")
msg.pack()

# Download Button
downloadBtn = Button(root, text="DOWNLOAD", fg="white", command=lambda: _thread.start_new_thread(download, ()), bg="#E21720", width=20, height=2)
downloadBtn.pack(pady=10)


root.mainloop()
