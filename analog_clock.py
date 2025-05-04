import tkinter as tk
import time
import math

def update_clock():
    now = time.localtime()
    seconds = now.tm_sec
    minutes = now.tm_min + seconds / 60
    hours = now.tm_hour % 12 + minutes / 60

    # Clear canvas
    canvas.delete("hands")

    # Second hand
    second_angle = math.radians(seconds * 6 - 90)
    x_sec = center_x + radius * 0.9 * math.cos(second_angle)
    y_sec = center_y + radius * 0.9 * math.sin(second_angle)
    canvas.create_line(center_x, center_y, x_sec, y_sec, fill="red", width=1, tags="hands")

    # Minute hand
    minute_angle = math.radians(minutes * 6 - 90)
    x_min = center_x + radius * 0.75 * math.cos(minute_angle)
    y_min = center_y + radius * 0.75 * math.sin(minute_angle)
    canvas.create_line(center_x, center_y, x_min, y_min, fill="blue", width=3, tags="hands")

    # Hour hand
    hour_angle = math.radians(hours * 30 - 90)
    x_hour = center_x + radius * 0.5 * math.cos(hour_angle)
    y_hour = center_y + radius * 0.5 * math.sin(hour_angle)
    canvas.create_line(center_x, center_y, x_hour, y_hour, fill="black", width=5, tags="hands")

    root.after(1000, update_clock)

# Window setup
root = tk.Tk()
root.title("Analog Clock")

canvas_size = 400
radius = canvas_size // 2 - 20
center_x = canvas_size // 2
center_y = canvas_size // 2

canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

# Draw clock face
canvas.create_oval(center_x - radius, center_y - radius,
                   center_x + radius, center_y + radius)

for i in range(12):
    angle = math.radians(i * 30 - 90)
    x_outer = center_x + radius * math.cos(angle)
    y_outer = center_y + radius * math.sin(angle)
    x_inner = center_x + (radius - 20) * math.cos(angle)
    y_inner = center_y + (radius - 20) * math.sin(angle)
    canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=2)

update_clock()
root.mainloop()
