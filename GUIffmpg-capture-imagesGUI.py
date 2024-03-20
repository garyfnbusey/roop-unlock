import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def capture_frames():
    # Get video file path
    video_path = video_entry.get()

    # Get start time (in seconds)
    start_time = int(start_time_entry.get())

    # Get end time (in seconds)
    end_time = int(end_time_entry.get())

    # Get frames per second (fps)
    fps = int(fps_entry.get())

    # Get output folder path to store captured frames
    output_folder = output_entry.get()

    # Calculate the total number of frames to capture
    total_frames = (end_time - start_time) * fps

    # Calculate the time interval between frames
    frame_interval = 1 / fps

    # Iterate through the frames to be captured
    for i in range(int(total_frames)):
        # Calculate the current time for capturing the frame
        current_time = start_time + i * frame_interval

        # Generate the output file name based on the frame index
        output_file = os.path.join(output_folder, f"frame_{i}.png")

        # Run ffmpeg command to capture the frame
        ffmpeg_cmd = ["ffmpeg", "-ss", str(current_time), "-i", video_path, "-vframes", "1", output_file]
        subprocess.run(ffmpeg_cmd, check=True)

    result_label.config(text="Frame capturing complete.")

# Create the GUI window
window = tk.Tk()
window.title("Frame Capture")

# Create label and entry for video path
video_label = tk.Label(window, text="Video Path:")
video_label.pack()
video_entry = tk.Entry(window, width=50)
video_entry.pack()

# Create button to browse and select video file
def browse_video_path():
    video_path = filedialog.askopenfilename(title="Select the video file")
    video_entry.delete(0, tk.END)
    video_entry.insert(tk.END, video_path)

browse_button = tk.Button(window, text="Browse", command=browse_video_path)
browse_button.pack()

# Create label and entry for start time
start_time_label = tk.Label(window, text="Start Time (in seconds):")
start_time_label.pack()
start_time_entry = tk.Entry(window, width=50)
start_time_entry.pack()

# Create label and entry for end time
end_time_label = tk.Label(window, text="End Time (in seconds):")
end_time_label.pack()
end_time_entry = tk.Entry(window, width=50)
end_time_entry.pack()

# Create label and entry for frames per second (fps)
fps_label = tk.Label(window, text="Frames per Second (fps):")
fps_label.pack()
fps_entry = tk.Entry(window, width=50)
fps_entry.pack()

# Create label and entry for output images path
output_label = tk.Label(window, text="Output Images Path:")
output_label.pack()
output_entry = tk.Entry(window, width=50)
output_entry.pack()

# Create button to browse and select output folder
def browse_output_path():
    output_path = filedialog.askdirectory(title="Select the output folder to store captured frames")
    output_entry.delete(0, tk.END)
    output_entry.insert(tk.END, output_path)

browse_output_button = tk.Button(window, text="Browse", command=browse_output_path)
browse_output_button.pack()

# Create button to trigger frame capturing
capture_button = tk.Button(window, text="Capture Frames", command=capture_frames)
capture_button.pack()

# Create label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the GUI window
window.mainloop()
