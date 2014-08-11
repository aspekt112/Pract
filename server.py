# -*- coding: utf-8 -*-
# Threaded xml-rpc server
import SocketServer
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler

# Ping, Traceroute
import subprocess
import re

# Threaded mix-in
class AsyncXMLRPCServer(SocketServer.ThreadingMixIn,SimpleXMLRPCServer): pass

error = "Адрес недоступен"

def ping(destination):
	ping = subprocess.Popen(
		["ping", "-c", "4", destination],
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE
	)
	average = re.search("round-trip min/avg/max/stddev = (\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)", ping.stdout.read())
	if average: result = average.group(2)
	else: result = error
	return result

def traceroute(destination):
	traceroute = subprocess.Popen(
	    ["traceroute", "-n", destination],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)
	#found = re.search("(\d+)  (\d+.\d+.\d+.\d+)  (\d+.\d+) ms  (\d+.\d+) ms  (\d+.\d+) ms", traceroute.stdout.read())
	result = traceroute.stdout.read()
	#if found: result = route
	#else: result = error
	print result
	return result

def nmap(destination):
	nmap = subprocess.Popen(
	    ["nmap", destination],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)
	#route = re.search("Nmap done: (\d+) IP address ((\d+) host up) scanned in (\d+.\d+) seconds", nmap.stdout.read())
	result = nmap.stdout.read()
	print result
	return result

# Instantiate and bind to localhost:8080
server = AsyncXMLRPCServer(('', 8080), SimpleXMLRPCRequestHandler)
print "Прослушивается порт 8080..."
server.register_function(ping, "ping")
server.register_function(traceroute, "traceroute")
server.register_function(nmap, "nmap")

# run!
print "Нажмите Control-C для выхода"
server.serve_forever()


