###########################
###########################
#File: send_sms.py
###########################
#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
"""
Use this to call the sms function
It is for sending SMS using AT commands - version v3
"""
## The packges below must be installed in advance
## sudo apt-get install python-setuptools
## easy_install pyserial

import serial
import time
import sys

from at_cmds import TextMessage

if len(sys.argv) == 1:
	message = ""
	
if len(sys.argv) >= 2:
	message = ""
	phoneNumber = sys.argv[1]
	for i in range(2, len(sys.argv)):
		message = message + " " + sys.argv[i]

	message = message.strip()
	print "number = " + phoneNumber + ", message = " + message
	sms = TextMessage(phoneNumber, message)
	
else:
	print "Please enter a phone number and message"

sms.sendMessage()

#Main function that calls other functions - Makes script reusable
def main():
	pass

if __name__ == "__main__":
	main()
