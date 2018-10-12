import tkinter as tk
import subprocess
cmd = "HTG.exe"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, creationflags=0x08000000)
root = tk.Tk()
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.1, height*0.1))
image_file = 'Configurazione\\assets\\KG-Splash.png'
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.5, width=width*0.5, bg="black")
canvas.create_image(width*0.5/2, height*0.5/2, image=image)
canvas.pack()
root.after(10000, root.destroy)
root.mainloop()
