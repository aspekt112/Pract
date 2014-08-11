import subprocess
import re

host = "localhost"

traceroute = subprocess.Popen(
    ["traceroute", "-n", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

route = re.search("\d  (\d+.\d+.\d+.\d+)  (\d+.\d+) ms  (\d+.\d+) ms  (\d+.\d+) ms", traceroute.stdout.read())
#average = re.search("round-trip min/avg/max/stddev = (\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)", ping.stdout.read())
if route: print "Average Round-Trip Time: %s ms -" % route.group(2), host
if route: print route.group(0), host
#result = os.system("traceroute -n "+ str(destination))
#1  127.0.0.1  0.246 ms  0.051 ms  0.033 ms

"""
hostname = "localhost"
for i in range(1, 28):
    pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
    # Send the packet and get a reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        # No reply =(
        break
    elif reply.type == 3:
        # We've reached our destination
        print "Done!", reply.src
        break
    else:
        # We're in the middle somewhere
        print "%d hops away: " % i , reply.src
"""
