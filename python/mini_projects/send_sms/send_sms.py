# ========================================
# Created     : Tue Jun 21 2022
# Author      : s7marsh
# Description : Send an SMS via Semaphore API
# ========================================

# If you don't have the `requests` library
# % python -m pip install requests
import sys, requests, urllib.parse, os.path

# Specify api_key file
this_dir = os.path.dirname(__file__)
path_to_apikey_file = os.path.join(this_dir,"api_key")

# Get API key from file
# github note: it is intentional to not commit the api_key
#              for privacy reasons ;)
f_api = open(path_to_apikey_file,"r")
apikey = f_api.read()

def send_message(message, number):
	'''
	sends a `message` to a `number` thru the Semaphore API
	'''
	print('Sending Message...')
	params = (
		('apikey', apikey),
		('sendername', sendername),
		('message', message),
		('number', number)
	)
	path = 'https://semaphore.co/api/v4/messages?' + urllib.parse.urlencode(params)
	requests.post(path)
	print('Message Sent!')

if __name__ == '__main__':
	sendername = 'SEMAPHORE' # FROM
	message = sys.argv[1]
	number = sys.argv[2] # TO
	send_message(message, number)