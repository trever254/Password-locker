import pyperclip
from user_credentials import User, Credentialdef create_user(fname,lname,password):

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user
