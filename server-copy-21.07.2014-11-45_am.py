# Threaded xml-rpc server
import SocketServer
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler

# Ping, Traceroute
import subprocess
import re

# Threaded mix-in
class AsyncXMLRPCServer(SocketServer.ThreadingMixIn,SimpleXMLRPCServer): pass

def ping(destination):
	ping = subprocess.Popen(
		["ping", "-c", "4", destination],
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE
	)
	average = re.search("round-trip min/avg/max/stddev = (\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)", ping.stdout.read())
	if average: result = "Average Round-Trip Time: %s ms -" % average.group(2), destination
	else: result = "Inaccesible state"
	return result

def traceroute(destination):
	traceroute = subprocess.Popen(
	    ["traceroute", "-n", destination],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)
	route = re.search("\d  (\d+.\d+.\d+.\d+)  (\d+.\d+) ms  (\d+.\d+) ms  (\d+.\d+) ms", traceroute.stdout.read())
	if route: result = route.group(0), destination
	else: result = "Inaccesible state"
	return result

# Instantiate and bind to localhost:8080
server = AsyncXMLRPCServer(('', 8080), SimpleXMLRPCRequestHandler)
print "Listening on port 8080..."

server.register_function(ping, "ping")
server.register_function(traceroute, "traceroute")
# run!
print "Press Control-C to exit"
server.serve_forever()