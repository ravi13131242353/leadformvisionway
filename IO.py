import tkinter as tk
from tkinter import messagebox
import yt_dlp
import os

# Function to download the video
def download_video():
    # Get the URL from the entry widget
    video_url = url_entry.get()

    if not video_url:
        messagebox.showerror("Error", "Please enter a valid YouTube video URL.")
        return

    # Directory for saving the video
    download_folder = folder_entry.get()
    
    if not download_folder:
        messagebox.showerror("Error", "Please specify a download folder.")
        return

    # Ensure the folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download the best available quality
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save the video in the specified folder
    }

    # Try to download the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to open a folder dialog to select the download folder
def choose_folder():
    folder = tk.filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Set window size
root.geometry("500x250")

# Create the URL label and entry widget
url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create the download folder label and entry widget
folder_label = tk.Label(root, text="Select Download Folder:")
folder_label.pack(pady=10)

folder_entry = tk.Entry(root, width=50)
folder_entry.pack(pady=5)

# Create the Browse button for folder selection
browse_button = tk.Button(root, text="Browse", command=choose_folder)
browse_button.pack(pady=5)

# Create the download button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
