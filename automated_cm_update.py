#!/usr/bin/python
import commands
import sys

device_name = "Anutham Adiga's Nexus 4"
device_adb_id = "004fcd422211d058"

#Reject if less than 1 or more than 2 devices are conected
no_of_devs_connected = commands.getoutput("adb devices | awk '/List of devices attached/,0' | sed 1d | head -n -1 | wc -l")
if ( int(no_of_devs_connected) < 1):
	print "No device connected. Please ensure that device is ADB enabled." 
	sys.exit(0)
elif( int(no_of_devs_connected) > 1):
	print "Kindly disconnect all devices other than: %s\nFor update to proceed\n" (device_name)
	sys.exit(0)

#List all the devices connected
list_of_attached_devs = 'adb devices | awk \'/List of devices attached/,0\' | sed 1d | head -n -1'
exCode,op_list_of_attached_devs = commands.getstatusoutput(list_of_attached_devs)

#Filter error with executing ADB
if (exCode != 0):
	print "Error executing 'adb devices'"
	sys.exit(1)
else:
	print op_list_of_attached_devs


#Get Device ID
comm_get_device_id = "cut -d$\'\\t\' -f1 %s" %(op_list_of_attached_devs)
print comm_get_device_id
exCode,input_device_id = commands.getstatusoutput(comm_get_device_id)

#Filter error
print input_device_id
if (exCode != 0):
        print "Error confirming device ID"
        sys.exit(1)

#Confirm it is your device
if (input_device_id != device_adb_id):
	print "The connected device is not: %s" (device_name)
	sys.exit(1)


print "Initiating process CM Update\nDevice %s identity confirmed\n" %(device_name)

sys.exit(0)
