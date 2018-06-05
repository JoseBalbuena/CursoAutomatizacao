#!/usr/bin/python3

from jsonrpclib import Server

switch = Server( "http://admin:admin@172.16.1.2:8000/command-api" ) 
response = switch.runCmds( 1, [ "show hostname" ] ) 
print "Hello, my name is: ", response[0][ "hostname" ] 
response = switch.runCmds( 1, [ "show version" ] ) 
print "My MAC address is: ", response[0][ "systemMacAddress" ] 
print "My version is: ", response[0][ "version" ]

