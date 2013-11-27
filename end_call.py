###########################
###########################
#File: end_call.py
###########################
#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
"""
Terminate voice call using AT commands
Calls the at_cmds class definitions - version v4
"""
## The packges below must be installed in advance
## sudo apt-get install python-setuptools
## easy_install pyserial

import serial
import time
import sys
from at_cmds import ATcommands
from at_cmds import VoiceCall

currentCall = VoiceCall()
currentCall.endCall()

#Main function that calls other functions - Makes script reusable
def main():
	pass

if __name__ == "__main__":
	main()