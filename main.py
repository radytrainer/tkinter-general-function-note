import tkinter as tk
window = tk.Tk()
window.geometry("300x300")
window.title("kkk")
frame = tk.Frame(window, width=300, height=300)
frame.pack()
canvas = tk.Canvas(frame, width=200, height=200, bg="blue")
canvas.pack()
window.mainloop()