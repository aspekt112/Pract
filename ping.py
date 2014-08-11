import subprocess
import re

host = "localhost"

ping = subprocess.Popen(
    ["ping", "-c", "4", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

average = re.search("round-trip min/avg/max/stddev = (\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)", ping.stdout.read())

if average: print "Average Round-Trip Time: %s ms -" % average.group(2), host