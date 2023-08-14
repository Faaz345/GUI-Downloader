import tkinter as tk
from tkinter import ttk, filedialog
import requests
import os
# https://file-examples.com/wp-content/storage/2017/04/file_example_MP4_1920_18MG.mp4
# https://download.jetbrains.com/python/pycharm-community-2023.1.2.exe?_gl=1*1bzqx3i*_ga*MTUzMjg2MjIyNC4xNjg0NTg4Njg3*_ga_9J976DJZ68*MTY4NTMyMjM5Mi40LjEuMTY4NTMyMjQwNS40Ny4wLjA.&_ga=2.50487849.182958038.1685257095-1532862224.1684588687
# https://redirector.gvt1.com/edgedl/android/studio/install/2022.2.1.20/android-studio-2022.2.1.20-windows.exe
class Downloader:
    def __init__(self):
        self.saveto = ""
        self.window = tk.Tk()
        self.window.title("Python GUI Downloader")
        self.url_label = tk.Label(text="Enter URL")
        self.url_label.pack()
        self.url_entry = tk.Entry()
        self.url_entry.pack()
        self.browse_button = tk.Button(text="Browse", command=self.browse_file)
        self.browse_button.pack()
        self.download_button = tk.Button(text="Download", command=self.download)
        self.download_button.pack()
        self.window.geometry("844x344")
        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", maximum=100, length=300, mode="determinate")
        self.progress_bar.pack()
        self.window.mainloop()



    def browse_file(self):
        saveto = filedialog.asksaveasfilename(initialfile=self.url_entry.get().split("/")[-1].split("?")[0])
        self.saveto = saveto

    def download(self):
        url = self.url_entry.get()
        response = requests.get(url, stream=True)
        total_size_in_bytes = 100
        if(response.headers.get("content-length")):
            total_size_in_bytes = int(response.headers.get("content-length"))
        block_size = 10000
        self.progress_bar["value"] = 0
        fileName = self.url_entry.get().split("/")[-1].split("?")[0]
        if(self.saveto == ""):
            self.saveto = fileName

        print(self.saveto)
        with open(self.saveto, "wb") as f:
            for data in response.iter_content(block_size):
                self.progress_bar["value"] += (100*block_size)/total_size_in_bytes
                self.window.update()
                f.write(data)

Downloader()