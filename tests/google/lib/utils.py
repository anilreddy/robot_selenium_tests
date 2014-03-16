import sys
import random
import datetime
import time

class utils:
	"""docstring for utils"""
	
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	__version__ = '0.1'

	def get_todays_date(self):
		now = datetime.datetime.now()
		return now.strftime("%Y-%m-%d")
