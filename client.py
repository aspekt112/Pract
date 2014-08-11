import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:8080')

destination = "127.0.0.1"

print proxy.ping(destination)
print proxy.traceroute(destination)
print proxy.nmap(destination)