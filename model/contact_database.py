import psycopg2
from psycopg2 import OperationalError
import json

class ContactDatabase:

	def __init__(self):
		with open('config/config.json','r') as config_file:
			config=json.load(config_file)
		self.host=config['database']['host']
		self.database=config['database']['database']
		self.user=config['database']['user']
		self.password=config['database']['password']
		self.connection=None

	def create_connection(self):
		try:
			self.connection=psycopg2.connect(
				database=self.database,
				user=self.user,
				password=self.password,
				host=self.host
			)
			print("Connection to PostgreSQL DB successful")
		except OperationalError as e:
			print(f"The error '{e}' occurred")
			self.connection=None
		return self.connection

	def execute_query(self,query,parameters=None,fetch=False):
		try:
			conn=self.create_connection()
			cur=conn.cursor()
			cur.execute(query,parameters)
			if fetch:
				results=cur.fetchall()
			else:
				results=None
			conn.commit()
			cur.close()
			conn.close()
			return results
		except Exception as error:
			print(error)
			return None

	def add_record(self,data):
		insert_query='''
		insert into test_data
		(first_name,last_name,phone_number,email) 
		values(%s,%s,%s,%s)
		'''
		self.execute_query(insert_query,(data['first_name'],data['last_name'],data['phone_number'],data['email']))
		print('RECORD INSERTED.')

	def select_all_contacts(self):
		select_query='''
		select * from test_data
		'''
		return self.execute_query(select_query,fetch=True)

	def update_record(self,record_id,data):
		update_query='''
		update test_data set
		first_name=%s,
		last_name=%s,
		phone_number=%s,
		email=%s WHERE data_id=%s
		'''
		self.execute_query(update_query,(data['first_name'],data['last_name'],data['phone_number'],data['email'],record_id))
		print('RECORD UPDATED.')

		
	def delete_record(self,record_id):
		delete_query='''
		delete from test_data where data_id=%s
		'''
		self.execute_query(delete_query,(record_id,))
		print('RECORD DELETED.')

if __name__=='__main__':
	print('db file')