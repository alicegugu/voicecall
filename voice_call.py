###########################
###########################
#  File: voice_call.py
###########################
#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
"""
Voice call using AT commands
Calls the at_cmds class definitions - version v3
"""
## The packges below must be installed in advance
## sudo apt-get install python-setuptools
## easy_install pyserial

import serial
import time
import sys
from at_cmds import VoiceCall


if len(sys.argv) > 1:
	phoneNumber = sys.argv[1]
	callPhone = VoiceCall(phoneNumber)
	callPhone.dialNumber()
else:
	print "Please enter a phone number"


#Main function that calls other functions - Makes script reusable
def main():
	pass

if __name__ == "__main__":
	main()