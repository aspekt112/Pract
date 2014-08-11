import xmlrpclib
from nodes.models import Node, Ping, Traceroute, Nmap
import time
"""
proxy = xmlrpclib.ServerProxy('http://localhost:8080')

start_time = time.time()

new_test = models.Model.Node.new()

new_ping = Ping.new(node = new_test.id, ttl = proxy.ping(destination))
new_ping.save()

new_traceroute = Traceroute.new(node = new_test.id, hop = proxy.traceroute(destination))
new_traceroute.save()

# Nmap testing should be here
"""
"""
new_nmap = Nmap.new(node = new_test.id, ...)
new_nmap.save()
"""
"""
new_test = Node.new(name = destination, start = start_time, finish = time.time()) # destination = google.com, localhost
new_test.save()

"""