import tkinter as tk
from tkinter import ttk,messagebox

class ContactView:
	def __init__(self,root,controller):
		self.root=root
		self.controller=controller
		self.root.title('Contact App')
		self.record_id=None
		self.create_widgets()
		self.populate_tree()

	def create_widgets(self):
		self.frm=tk.Frame(master=self.root,bd=3)
		self.frm.pack()

		#First Name
		self.lbl_firstname=tk.Label(self.frm,text='First Name')
		self.ent_firstname=tk.Entry(self.frm,width=40)
		self.lbl_firstname.grid(row=0,column=0,sticky='e',pady=5)
		self.ent_firstname.grid(row=0,column=1)

		#Last Name
		self.lbl_lastname=tk.Label(self.frm,text='Last Name')
		self.ent_lastname=tk.Entry(self.frm,width=40)
		self.lbl_lastname.grid(row=1,column=0,sticky='e',pady=5)
		self.ent_lastname.grid(row=1,column=1)

		#Phone Number
		self.lbl_phonenumber=tk.Label(self.frm,text='Phone Number')
		self.ent_phonenumber=tk.Entry(self.frm,width=40)
		self.lbl_phonenumber.grid(row=2,column=0,sticky='e',pady=5)
		self.ent_phonenumber.grid(row=2,column=1)

		#Email
		self.lbl_email=tk.Label(self.frm,text='Email')
		self.ent_email=tk.Entry(self.frm,width=40)
		self.lbl_email.grid(row=3,column=0,sticky='e',pady=5)
		self.ent_email.grid(row=3,column=1)

		frm_buttons=tk.Frame(master=self.root,bd=10)
		frm_buttons.pack()

		btn_add=tk.Button(frm_buttons,text='Add Contact',command=self.controller.add_contact)
		btn_add.grid(row=0,column=0)
		btn_update=tk.Button(frm_buttons,text='Update Contact',command=self.controller.update_contact)
		btn_update.grid(row=0,column=2)
		btn_delete=tk.Button(frm_buttons,text='Delete Contact',bg='red',fg='white',command=self.controller.delete_contact)
		btn_delete.grid(row=0,column=3)
		btn_reset=tk.Button(frm_buttons,text='Reset',command=self.reset_fields)
		btn_reset.grid(row=0,column=4)

		columns=('id','First Name','Last Name','Phone Number','Email')
		self.tree=ttk.Treeview(self.root,columns=columns,show='headings')
		for pos in range(len(columns)):
			self.tree.heading(columns[pos],text=columns[pos])
			if pos!=0:
				#print('pos')
				self.tree.column(columns[pos],width=210,anchor='center')
			else:
				#print('pos 0')
				self.tree.column(columns[pos],minwidth=0,width=0,anchor='center')
		self.tree.bind('<Double-1>',self.item_selected)
		self.tree.pack()

	def reset_fields(self):
		self.record_id=None
		self.ent_firstname.delete(0,tk.END)
		self.ent_lastname.delete(0,tk.END)
		self.ent_phonenumber.delete(0,tk.END)
		self.ent_email.delete(0,tk.END)

	def show_data(self,record):
		self.record_id=record[0]
		print(f'Record ID - {self.record_id}')
		self.ent_firstname.insert(0,record[1])
		self.ent_lastname.insert(0,record[2])
		self.ent_phonenumber.insert(0,record[3])
		self.ent_email.insert(0,record[4])

	def populate_tree(self):
		for item in self.tree.get_children():
			self.tree.delete(item)
		contacts=self.controller.get_all_contacts()
		for contact in contacts:
			self.tree.insert('',tk.END,values=contact)

	def item_selected(self,event):
		self.reset_fields()
		for selected_item in self.tree.selection():
			item=self.tree.item(selected_item)
			record=item['values']
		self.show_data(record)

	def get_record_id(self):
		return self.record_id

	def get_input_data(self):
		return {
		'first_name':self.ent_firstname.get(),
		'last_name':self.ent_lastname.get(),
		'phone_number':self.ent_phonenumber.get(),
		'email':self.ent_email.get()
		}

	def show_error(self,title,message):
		tk.messagebox.showerror(title,message)

if __name__=='__main__':
	print('view file')