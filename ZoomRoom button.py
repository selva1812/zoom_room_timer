import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Sausage Roll")

current_timer = None

# Set the size of the window to match an iPad screen in landscape (2048x1536)
root.geometry("1024x768")  # Scaling down to half size for tkinter's resolution handling
samsara_blue = "#00263E"
root.configure(bg=samsara_blue)

# Load the logo image for the bottom-right corner
try:
    logo_image = Image.open("samsara_vertical_logo_white.png")  # Replace with your logo image path
    logo_image = logo_image.resize((100, 100), Image.LANCZOS)  # Resize to fit the corner
    logo_image_tk = ImageTk.PhotoImage(logo_image)
except Exception as e:
    print(f"Error loading image: {e}")
    logo_image_tk = None


# Create a frame to hold other widgets
frame = tk.Frame(root, bg=samsara_blue)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a label
initial_text = "Sausage Roll"
label = tk.Label(root, text=initial_text, bg=samsara_blue, fg="white", font=("Roboto", 50))
label.pack(pady=50)

# Timer label to display remaining time
timer_label = tk.Label(root, text="", bg=samsara_blue, fg="red", font=("Roboto", 45))
timer_label.pack(pady=20)

# Function to update the timer
def update_timer(remaining_seconds):
    if remaining_seconds > 0:
        minutes, seconds = divmod(remaining_seconds, 60)
        timer_label.config(text=f"Reserved for {minutes:02}:{seconds:02}")
        global current_timer
        current_timer = root.after(1000, update_timer, remaining_seconds - 1)
    else:
        timer_label.config(text="")
        label.config(text=initial_text)

# Define the button click event
def on_button_click(delay_ms, display_time):
    global current_timer
    if current_timer is not None:
        root.after_cancel(current_timer)  # Cancel the previous timer if running
        current_timer = None
    label.config(text="Room is reserved for " + display_time)
    # Convert delay from milliseconds to seconds
    delay_seconds = delay_ms // 1000
    # Start the timer
    update_timer(delay_seconds)

# Create a button
button_15_min = tk.Button(root, text="Reserve for 15mins", bg=samsara_blue, fg="black", font=("Roboto", 28), command=lambda: on_button_click(15 * 60 * 1000, "15mins"))
button_15_min.pack(pady=30)

button_30_min = tk.Button(root, text="Reserve for 30mins", bg=samsara_blue, fg="black", font=("Roboto", 28), command=lambda: on_button_click(30 * 60 * 1000, "30mins"))
button_30_min.pack(pady=30)

button_60_min = tk.Button(root, text="Reserve for 1hr", bg=samsara_blue, fg="black", font=("Roboto", 28), command=lambda: on_button_click(60 * 60 * 1000, "1hr"))
button_60_min.pack(pady=30)

button_120_min = tk.Button(root, text="Reserve for 2hrs", bg=samsara_blue, fg="black", font=("Roboto", 28), command=lambda: on_button_click(120 * 60 * 1000, "2hr"))
button_120_min.pack(pady=30)

# Add logo image to the bottom-right corner, after packing all other widgets
if logo_image_tk:
    logo_label = tk.Label(root, image=logo_image_tk, bg=samsara_blue)
    logo_label.place(x=1024 - 110, y=768 - 110)  # Position at bottom-right

# Run the application
root.mainloop()
