import tkinter as tk
from controller.contact_controller import ContactController

if __name__=='__main__':
	root=tk.Tk()
	controller=ContactController(root)
	root.mainloop()
