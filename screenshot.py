import pyautogui 
import time
import tkinter as tk

def main():
    name = int(round(time.time())*1000)
    time.sleep(2)
    img = pyautogui.screenshot()
    name = f"C:/Users/Pranav/Desktop/python projects/screenshots/{name}.png"
    img.save(name
    )
    img.show()
root =tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Click me", command=main)
button.pack(side=tk.LEFT)
close = tk.Button(frame, text="Close", command=quit)
close.pack(side=tk.RIGHT)
root.mainloop()
