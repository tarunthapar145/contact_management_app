from view.contact_view import ContactView
from model.contact_database import ContactDatabase

class ContactController:

	def __init__(self,root):
		self.model=ContactDatabase()
		self.view=ContactView(root,self)

	def get_all_contacts(self):
		return self.model.select_all_contacts()

	def add_contact(self):
		print('add button pressed.')
		record_id=self.view.get_record_id()
		if record_id is not None:
			self.view.show_error('ERROR','Existing record cannot be added again.')
			return
		data=self.view.get_input_data()
		if not data['first_name'] or not data['last_name']:
			self.view.show_error('ERROR','First name and Last name fields cannot be empty.')
			return
		self.model.add_record(data)
		self.view.reset_fields()
		self.view.populate_tree()
		return

	def update_contact(self):
		print('update button pressed.')
		record_id=self.view.get_record_id()
		if record_id is None:
			self.view.show_error('ERROR','No record selected to update.')
			return
		data=self.view.get_input_data()
		self.model.update_record(record_id,data)
		self.view.reset_fields()
		self.view.populate_tree()
		return

	def delete_contact(self):
		print('delete button pressed.')
		record_id=self.view.get_record_id()
		if record_id is None:
			self.view.show_error('ERROR','Please select record to delete.')
			return
		self.model.delete_record(record_id)
		self.view.reset_fields()
		self.view.populate_tree()
		return

if __name__=='__main__':
	print('controller file')
